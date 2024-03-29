import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import turtle 
import io
import Pmw

from tkinter import filedialog
from tkinter import messagebox
from PIL import Image


# List of math challenges for the Geometry Tool
math_challenges = [
        {"description": "Draw a square with each side measuring 100 pixels.",
        "hints": ["Use the forward and right commands", "A square has equal sides and each angle is 90 degrees."],
        "commands": ["forward 100", "right 90", "forward 100", "right 90", "forward 100", "right 90", "forward 100"]},
        {"description": "Draw a right-angled triangle with sides 50, 120, 130 pixels.",
        "hints": ["Use the Pythagorean theorem to verify the sides.", "The sum of angles in a triangle is 180 degrees."],
        "commands": ["forward 50", "right 90", "forward 120", "right 135", "forward 130"]}
    
]
class Turtle:
    def __init__(self, canvas, output_display):
        self.canvas = canvas
        self.output_display = output_display
        self.turtle = turtle.RawTurtle(canvas)
        self.turtle.speed(1)

    def execute_code(self, code):
        lines = code.split('\n')
        for line in lines:
            result = self.execute_line(line.strip())
            if result and "Invalid command" in result:
                return result
        return "Code executed successfully."

    def execute_line(self, line):
        tokens = line.split()

        if not tokens:
            return None  # Ignore empty lines

        if tokens[0] == "forward" and len(tokens) == 2:
            try:
                distance = float(tokens[1])
                self.move_forward(distance)
            except ValueError:
                return f"Invalid command: {line}"
        elif tokens[0] == "right" and len(tokens) == 2:
            try:
                angle = float(tokens[1])
                self.turn_right(angle)
            except ValueError:
                return f"Invalid command: {line}"
        else:
            return f"Invalid command: {line}"

    def move_forward(self, distance):
        self.turtle.forward(distance)

    def turn_right(self, angle):
        self.turtle.right(angle)


class GeometryTool(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#ecf0f1")
        self.winfo_toplevel().title("Geometry Tool")


        

        self.welcome_message_shown = False
        self.bind("<Enter>", self.on_page_enter)

        # Add buttons for saving and exporting drawings
        self.save_drawing_button = tk.Button(self, text="Save Drawing", command=self.save_drawing)
        self.save_drawing_button.grid(row=8, column=1, pady=5, padx=10, sticky=tk.W)

        # Balloon tooltips setup
        self.balloon = Pmw.Balloon(self)
        self.balloon.bind(self.save_drawing_button, 'Save the current drawing to a file.')

        self.export_drawing_button = tk.Button(self, text="Export Drawing", command=self.export_drawing)
        self.export_drawing_button.grid(row=8, column=2, pady=5, padx=10, sticky=tk.W)

        self.instructions = tk.StringVar()
        self.instructions.set("")

       # Add a label next to the text editor
        editor_info_label = tk.Label(self, text="Enter your drawing instructions below:", font=("Arial", 13), bg="#ecf0f1")
        editor_info_label.grid(row=1, column=1, pady=10, padx=10, sticky=tk.W)

        # Add a button to clear the instructions
        self.clear_button = tk.Button(self, text="Clear Instructions", command=self.clear_instructions)
        self.clear_button.grid(row=0, column=4, pady=5, padx=10, sticky=tk.W)

        # Add a button to clear the drawing
        self.clear_drawing_button = tk.Button(self, text="Clear Drawing", command=self.clear_drawing)
        self.clear_drawing_button.grid(row=1, column=4, pady=5, padx=10, sticky=tk.W)

        # Add buttons for specific shape activities to the right side
        self.square_button = tk.Button(self, text="Draw Square", command=self.draw_square)
        self.square_button.grid(row=1, column=2, pady=10, padx=10, sticky=tk.W)

        self.circle_button = tk.Button(self, text="Draw Circle", command=self.draw_circle)
        self.circle_button.grid(row=2, column=2, pady=5, padx=10, sticky=tk.W)

        self.rectangle_button = tk.Button(self, text="Draw Rectangle", command=self.draw_rectangle)
        self.rectangle_button.grid(row=3, column=2, pady=5, padx=10, sticky=tk.W)

        self.triangle_button = tk.Button(self, text="Draw Triangle", command=self.draw_triangle)
        self.triangle_button.grid(row=4, column=2, pady=5, padx=10, sticky=tk.W)

        self.custom_button = tk.Button(self, text="Draw Custom Shape", command=self.draw_custom)
        self.custom_button.grid(row=5, column=2, pady=5, padx=10, sticky=tk.W)

        self.code_editor = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=15)
        self.code_editor.grid(row=1, column=1, rowspan=5, pady=10, padx=10, sticky=tk.W)

        self.execute_button = tk.Button(self, text="Run Code", command=self.execute_code)
        self.execute_button.grid(row=6, column=1, pady=5, padx=10, sticky=tk.W)

        self.output_display = tk.Text(self, wrap=tk.WORD, state=tk.DISABLED, width=50, height=10)
        self.output_display.grid(row=7, column=1, pady=10, padx=10, sticky=tk.W)

        self.turtle_canvas = tk.Canvas(self, width=500, height=500, bg="white")
        self.turtle_canvas.grid(row=1, column=3, rowspan=7, pady=10, padx=10, sticky=tk.W)

        self.turtle = Turtle(self.turtle_canvas, self.output_display)

        self.output_display.tag_config("error", foreground="red")
        self.output_display.tag_config("success", foreground="green")

        self.turtle_canvas.bind("<Button-1>", self.on_canvas_click) 

        # Initialize mode
        self.drawing_mode = True


        self.turtle_canvas.bind("<B1-Motion>", self.on_canvas_move)

        # Attributes for math challenges
        self.current_challenge_index = 0
        self.challenge_label = tk.Label(self, text="", font=("Arial", 12), wraplength=400, bg="#ecf0f1")
        self.challenge_label.grid(row=9, column=1, columnspan=3, sticky="w", pady=5, padx=10)
        self.hint_label = tk.Label(self, text="", font=("Arial", 10), wraplength=400, bg="#ecf0f1", fg="blue")
        self.hint_label.grid(row=10, column=1, columnspan=3, sticky="w", pady=5, padx=10)
        self.next_challenge_button = tk.Button(self, text="Next Challenge", command=self.next_challenge)
        self.next_challenge_button.grid(row=11, column=1, pady=5, padx=10, sticky="w")

        self.display_current_challenge()  # Display the first challenge
        self.current_guide_step = 0  # Tracks the current step of the guide
        self.follow_guide = True  # User can decide to follow the guide or not

        self.next_step_button = tk.Button(self, text="Next Step", command=self.next_guide_step)
        self.next_step_button.grid(row=12, column=1, pady=5, padx=10, sticky=tk.W)
        self.repeat_step_button = tk.Button(self, text="Repeat Step", command=self.display_guide_step)
        self.repeat_step_button.grid(row=12, column=2, pady=5, padx=10, sticky=tk.W)
        self.exit_guide_button = tk.Button(self, text="Exit Guide", command=self.exit_guide)
        self.exit_guide_button.grid(row=12, column=3, pady=5, padx=10, sticky=tk.W)

        # Initialize and display the first guide step
        self.display_guide_step()
        
    def display_guide_step(self):
        guide_steps = [
            "Welcome to the Geometry Tool! Click 'Next' to start learning.",
            "First, let's draw a square. Enter the commands in the code editor.",
            "Great! Now let's try drawing a triangle.",
            # Add as many steps as you need
            "You have completed the guide!"
        ]
        if self.current_guide_step < len(guide_steps):
            self.instructions.set(guide_steps[self.current_guide_step])
        else:
            self.instructions.set("Guide completed. Feel free to explore!")
            self.follow_guide = False  # Guide is complete, user can explore freely
    
    def next_guide_step(self):
        self.current_guide_step += 1
        self.display_guide_step()

    def exit_guide(self):
        self.follow_guide = False
        self.instructions.set("Guide exited. You can use the tool freely now.")




    def display_current_challenge(self):
        if self.current_challenge_index < len(math_challenges):
            challenge = math_challenges[self.current_challenge_index]
            self.challenge_label.config(text="Challenge: " + challenge["description"])
            self.hint_label.config(text="Hints: " + "; ".join(challenge["hints"]))
        else:
            self.challenge_label.config(text="You have completed all challenges!")
            self.hint_label.config(text="")
            self.next_challenge_button.config(state="disabled")  # Disable button if no more challenges

    def next_challenge(self):
        self.current_challenge_index += 1
        self.display_current_challenge()
        
    
    def on_canvas_click(self, event):
            # Handle drawing mode
            x, y = event.x, event.y

            # Get the code from the code editor
            code = self.code_editor.get("1.0", tk.END)

            # Execute the code and draw the shape at the mouse click position
            self.turtle.turtle.penup()  # Lift the pen to move without drawing
            self.turtle.turtle.goto(x - 250, 250 - y)  # Adjust coordinates to match the turtle canvas
            self.turtle.turtle.pendown()  # Put the pen down to start drawing again
        

    def on_canvas_move(self, event):
        if not self.drawing_mode and self.selected_shape:
            dx = event.x - self.last_click_x
            dy = event.y - self.last_click_y
            self.selected_shape.move(dx, dy)  # You need to implement this method
            self.last_click_x = event.x
            self.last_click_y = event.y
            self.update_canvas()  # You need to implement this method to redraw shapes


    def draw_square(self):
        instructions = "forward 50\nright 90\nforward 50\nright 90\nforward 50\nright 90\nforward 50"
        self.instructions.set(instructions)
        self.code_editor.delete("1.0", tk.END)
        self.code_editor.insert(tk.END, instructions)



    def draw_circle(self):
        radius = 50
        self.turtle.penup()
        self.turtle.goto(-radius, 0)
        self.turtle.pendown()
        self.turtle.circle(radius)



    def draw_rectangle(self):
        instructions = "forward 100\nright 90\nforward 50\nright 90\nforward 100\nright 90\nforward 50"
        self.instructions.set(instructions)
        self.code_editor.delete("1.0", tk.END)
        self.code_editor.insert(tk.END, instructions)

    def draw_triangle(self):
        instructions = "forward 100\nright 120\nforward 100\nright 120\nforward 100"
        self.instructions.set(instructions)
        self.code_editor.delete("1.0", tk.END)
        self.code_editor.insert(tk.END, instructions)

    def draw_custom(self):
        instructions = "# Try drawing your own shapes!\n# Use commands like move_forward, turn_right, etc.\n# Example: move_forward 50\nturn_right 90\nmove_forward 50"
        self.instructions.set(instructions)

    def execute_code(self):
        code = self.code_editor.get("1.0", tk.END)
        self.output_display.config(state=tk.NORMAL)
        self.output_display.delete("1.0", tk.END)

        result = self.turtle.execute_code(code)

        if "Invalid command" in result:
            # Display the error message in red
            self.output_display.insert(tk.END, result, "error")
        else:
            # Display the success message in green
            self.output_display.insert(tk.END, "Code executed successfully.", "success")


        self.output_display.config(state=tk.DISABLED)

    def execute_instructions(self):
        instructions = self.instructions.get()
        self.output_display.config(state=tk.NORMAL)
        self.output_display.delete("1.0", tk.END)
        result = self.turtle.execute_code(instructions)
        self.output_display.insert(tk.END, result)
        self.output_display.config(state=tk.DISABLED)

    def clear_instructions(self):
        self.instructions.set("")
        self.code_editor.delete("1.0", tk.END)

    def clear_turtle_canvas(self):
        self.turtle_canvas.delete("all")

    def clear_drawing(self):
        print("Clear Drawing method called.")
        self.turtle.turtle.clear()
        self.turtle.turtle.penup()  # Lift the pen to move without drawing
        self.turtle.turtle.goto(0, 0)  # Move back to the original position
        self.turtle.turtle.pendown()  # Put the pen down to start drawing again



    def on_page_enter(self, event):
        if not self.welcome_message_shown and self.follow_guide:
            self.display_guide_step()  # Start the guide when the page is first entered
            self.welcome_message_shown = True


    def show_welcome_message(self):
        welcome_message = (
            "Welcome to the Learn 2D Shapes page!\n\n"
            "Click on the shape buttons to see how to draw some shapes, copy the text and then click 'Run Code' to see the result!\n\nPress the Draw Custom shape to draw a custom shape! "
        )
        messagebox.showinfo("Learn 2D Shapes", welcome_message)

    def save_drawing(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")])

        if file_path:
            try:
                # Capture the drawing on the canvas as an image
                image = self.capture_drawing()

                # Save the image to the specified file path
                image.save(file_path)

                messagebox.showinfo("Save Drawing", f"Drawing saved successfully at {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while saving the drawing: {str(e)}")

    def export_drawing(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")])

        if file_path:
            try:
                # Capture the drawing on the canvas as an image
                image = self.capture_drawing()

                # Save the image to the specified file path
                image.save(file_path)

                messagebox.showinfo("Export Drawing", f"Drawing exported successfully at {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while exporting the drawing: {str(e)}")


    def capture_drawing(self):
        try:
            # Capture the drawing on the canvas as an image
            drawing_data = self.turtle_canvas.postscript(colormode='color')
            image = Image.open(io.BytesIO(drawing_data.encode('utf-8')))
            return image
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the drawing: {str(e)}")

        return None


if __name__ == "__main__":
    app = GeometryTool(None)
    app.geometry("800x600")
    app.mainloop()