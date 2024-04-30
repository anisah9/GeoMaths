import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import turtle 
import io

from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

class Turtle:
    def __init__(self, canvas, output_display):
        self.canvas = canvas
        self.output_display = output_display
        self.turtle = turtle.RawTurtle(canvas)
        self.turtle.speed(3)
        self.turtle.pencolor('orange')
        self.turtle.pensize(3)
        
        self.grid_turtle = turtle.RawTurtle(canvas)
        self.grid_turtle.speed(0)
        self.grid_turtle.penup()
        self.grid_turtle.hideturtle()
        self.draw_grid()
               
            
    def execute_code(self, code):
        lines = code.split('\n')
        for line in lines:
            success, result = self.execute_line(line.strip())
            if not success:
                return result  
        return "Code executed successfully."
            

    def execute_line(self, line):
        tokens = line.split()
        if not tokens:
            return False, "Empty line"

        command, *args = tokens

        if command == "forward" and len(args) == 1 and args[0].isdigit():
            self.move_forward(float(args[0]))
        elif command == "right" and len(args) == 1 and args[0].isdigit():
            self.turn_right(float(args[0]))
        elif command == "goto" and len(args) == 2 and all(arg.isdigit() for arg in args):
            self.goto(float(args[0]), float(args[1]))
        else:
            return False, f"Invalid command or wrong number of arguments: {line}"

        return True, ""

    def move_forward(self, distance):
        self.turtle.forward(distance)

    def turn_right(self, angle):
        self.turtle.right(angle)
    
    def goto(self, x, y):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()


    def draw_grid(self):
        self.grid_turtle.speed(0)  
        self.grid_turtle.pencolor('#e0e0e0')  
        self.grid_turtle.pensize(1)  

        # Draw vertical grid lines
        for x in range(-250, 251, 50):
            self.grid_turtle.penup()
            self.grid_turtle.goto(x, -250)
            self.grid_turtle.pendown()
            self.grid_turtle.goto(x, 250)

        # Draw horizontal grid lines
        for y in range(-250, 251, 50):
            self.grid_turtle.penup()
            self.grid_turtle.goto(-250, y)
            self.grid_turtle.pendown()
            self.grid_turtle.goto(250, y)

        self.grid_turtle.pencolor('black')  # Black color for axes
        self.grid_turtle.pensize(2)  # Thicker lines for the axes

        # Draw x-axis
        self.grid_turtle.penup()
        self.grid_turtle.goto(-250, 0)
        self.grid_turtle.pendown()
        self.grid_turtle.goto(250, 0)

        # Draw y-axis
        self.grid_turtle.penup()
        self.grid_turtle.goto(0, -250)
        self.grid_turtle.pendown()
        self.grid_turtle.goto(0, 250)

        self.grid_turtle.penup()  

                # Numbering the x-axis
        for x in range(-250, 251, 50):
            self.grid_turtle.penup()
            self.grid_turtle.goto(x, -10)  
            self.grid_turtle.pendown()
            if x != 0:  
                self.grid_turtle.write(str(x), align="center", font=("Arial", 8, "normal"))

        # Numbering the y-axis
        for y in range(-250, 251, 50):
            self.grid_turtle.penup()
            self.grid_turtle.goto(-20, y)  
            self.grid_turtle.pendown()
            if y != 0:  
                self.grid_turtle.write(str(y), align="right", font=("Arial", 8, "normal"))

class DrawShapeTab(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#ecf0f1")
        self.winfo_toplevel().title("GeoMaths")
 
        self.welcome_message_shown = False

        self.instructions = tk.StringVar()
        self.instructions.set("")

        # Add a button to clear the drawing
        self.clear_drawing_button = tk.Button(self, text="Clear Drawing", command=self.clear_drawing)
        self.clear_drawing_button.grid(row=1, column=0, pady=5, padx=10, sticky=tk.W)

        # Add a button to export the drawing
        self.export_drawing_button = tk.Button(self, text="Export Drawing", command=self.export_drawing)
        self.export_drawing_button.grid(row=2, column=0, pady=5, padx=10, sticky=tk.W)

        # Create panel box
        panel_box = tk.Frame(self, bg="#dfe6e9", bd=2, relief=tk.GROOVE)
        panel_box.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Set the width of the contents inside the panel box
        panel_box.grid_propagate(False)
        panel_box.config(width=310, height=680)

        # Welcome message
        welcome_message = "Welcome to the Draw Shapes Tab!"

        # Information text
        information_text = """
        Embark on a geometric journey exploring various shapes.
        Learn geometry fundamentals, logic, and unleash creativity.
        See math in action and get started with programming basics.
        Whether you're a beginner or just curious, enjoy drawing and learning!
        """

       # Label for welcome message
        welcome_label_font = ("Arial", 17, "bold")
        welcome_label = tk.Label(panel_box, text=welcome_message, bg="#dfe6e9", fg="#2c3e50", font=welcome_label_font)
        welcome_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Center both vertically and horizontally


        # Label for information text
        information_box = tk.Label(panel_box, text=information_text, wraplength=300, bg="#dfe6e9", fg="#2c3e50", font=("Arial", 13))
        information_box.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Code Instructions Label
        code_instructions_label = tk.Label(panel_box, text="Enter your code instructions below:", bg="#dfe6e9", fg="#2c3e50", font=("Arial", 13))
        code_instructions_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        

        # Code editor
        self.code_editor = scrolledtext.ScrolledText(panel_box, wrap=tk.WORD, width=35, height=15)
        self.code_editor.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        # Run code button
        self.execute_button = tk.Button(panel_box, text="Run Code", command=self.execute_code)
        self.execute_button.grid(row=4, column=0, pady=5, padx=10, sticky=tk.W)
        
        self.clear_instructions_button = tk.Button(panel_box, text="Clear Instructions", command=self.clear_instructions)  # width in characters
        self.clear_instructions_button.grid(row=4, column=0, padx=5, pady=10, sticky="e")  # Adjust padx and sticky


        # Output display
        self.output_display = tk.Text(panel_box, wrap=tk.WORD, state=tk.DISABLED, width=35, height=10)
        self.output_display.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)

        # Configure text tags for coloring
        self.output_display.tag_configure("error", foreground="red")
        self.output_display.tag_configure("success", foreground="green")

        self.turtle_canvas = tk.Canvas(self, width=570, height=570, bg="white")
        self.turtle_canvas.grid(row=0, column=1, rowspan=5, pady=10, padx=10, sticky='nw')

        self.turtle = Turtle(self.turtle_canvas, self.output_display)

        self.create_commands_and_shapes_panel()

    def create_commands_and_shapes_panel(self):
        commands_and_shapes_panel = tk.LabelFrame(self, text="Commands and Shapes",
                                                  bg="#ecf0f1", fg="#2c3e50",
                                                  font=("Arial", 20, "bold"),
                                                  labelanchor='n',
                                                  highlightbackground="#34495e",
                                                  highlightcolor="#34495e",
                                                  highlightthickness=2)
        commands_and_shapes_panel.grid(row=0, column=2, rowspan=8, pady=10, padx=10, sticky="nsew")

        for i in range(20): 
            commands_and_shapes_panel.grid_rowconfigure(i, weight=1)
            commands_and_shapes_panel.grid_columnconfigure(i, weight=1)

        # Subheading for key commands
        key_commands_subheading = tk.Label(commands_and_shapes_panel, text="Key Commands",
                                           bg="#dfe6e9", fg="#2c3e50", font=("Arial", 18, "bold"))
        key_commands_subheading.grid(row=0, column=0, sticky="w")

        # Add key command labels and buttons
        self.add_command_button(commands_and_shapes_panel, "Forward: Move Turtle forward by specified distance",
                                self.show_forward, 1)
        self.add_command_button(commands_and_shapes_panel, "Right: Turn Turtle right by specified angle",
                                self.show_right, 3)
        self.add_command_button(commands_and_shapes_panel, "Go To: Move Turtle to specified coordinates (x, y)",
                                self.show_goto, 5)

        # Add space between sections
        spacer_label = tk.Label(commands_and_shapes_panel, bg="#ecf0f1", height=2)
        spacer_label.grid(row=6, column=0, columnspan=2, sticky="ew")

        # Subheading for shape selection
        shape_selection_subheading = tk.Label(commands_and_shapes_panel, text="Select Shape to Draw",
                                              bg="#dfe6e9", fg="#2c3e50", font=("Arial", 18, "bold"))
        shape_selection_subheading.grid(row=7, column=0, sticky="w")

        # Add shape buttons
        self.add_shape_button(commands_and_shapes_panel, "Draw Square", self.draw_square, 8)
        self.add_shape_button(commands_and_shapes_panel, "Draw Circle", self.draw_circle, 9)
        self.add_shape_button(commands_and_shapes_panel, "Draw Rectangle", self.draw_rectangle, 10)
        self.add_shape_button(commands_and_shapes_panel, "Draw Triangle", self.draw_triangle, 11)
        self.add_shape_button(commands_and_shapes_panel, "Draw Parallelogram", self.draw_parallelogram, 12)
        self.add_shape_button(commands_and_shapes_panel, "Draw Rhombus", self.draw_rhombus, 13)
        self.add_shape_button(commands_and_shapes_panel, "Draw Trapezium", self.draw_trapezium, 14)
        self.add_shape_button(commands_and_shapes_panel, "Draw Pentagon", self.draw_pentagon, 15)
        self.add_shape_button(commands_and_shapes_panel, "Draw Hexagon", self.draw_hexagon, 16)
        self.add_shape_button(commands_and_shapes_panel, "Draw Heptagon", self.draw_heptagon, 17)
        self.add_shape_button(commands_and_shapes_panel, "Draw Octagon", self.draw_octagon, 18)
        self.add_shape_button(commands_and_shapes_panel, "Draw Custom Shape", self.draw_custom, 19)

    def add_command_button(self, panel, text, command, row):
        label_font = ("Arial", 13)
        wrap_length = 250
        label = tk.Label(panel, text=text, anchor="center", justify="center",
                         wraplength=wrap_length, font=label_font, bg="#dfe6e9")
        label.grid(row=row, column=0, padx=10, pady=2, sticky="ew")

        button = tk.Button(panel, text="Show", command=command, padx=10, pady=5,
                           bg="#3498db", fg="black", relief=tk.RAISED)
        button.grid(row=row, column=1, padx=10, pady=2, sticky="ew")

    def add_shape_button(self, panel, text, command, row):
        button = tk.Button(panel, text=text, command=command, padx=10, pady=5,
                           bg="#3498db", fg="black", relief=tk.RAISED)
        button.grid(row=row, column=0, padx=10, pady=2, sticky="ew")


    def show_forward(self):
        self.turtle.turtle.reset()
        self.turtle.turtle.pencolor('blue')  # Set the line color to blue for moving forward
        self.turtle.turtle.pensize(3)  # Set the pen thickness to 3
        self.turtle.move_forward(100)

    def show_right(self):
        self.turtle.turtle.reset()
        self.turtle.turtle.pencolor('red')  # Set the line color to red for turning right
        self.turtle.turtle.pensize(3)  # Set the pen thickness to 3
        self.turtle.move_forward(60)
        self.turtle.turn_right(90)
        self.turtle.move_forward(60)

    def show_goto(self):
        self.turtle.turtle.reset()
        self.turtle.turtle.pencolor('green')  # Set the line color to green for going to a position
        self.turtle.turtle.pensize(3)  # Set the pen thickness to 3
        self.turtle.goto(100, 100)
        self.turtle.turtle.dot(10, 'green')  # Draw a green dot 


    def draw_square(self):
        self.turtle.turtle.reset()
        self.turtle.turtle.pencolor('orange')  # Setting color for square
        self.turtle.turtle.pensize(3)  # Setting line thickness for square
        instructions = "forward 50\nright 90\nforward 50\nright 90\nforward 50\nright 90\nforward 50"
        self.instructions.set(instructions)
        self.code_editor.delete("1.0", tk.END)
        self.code_editor.insert(tk.END, instructions)
        self.execute_code()

    def draw_circle(self):
        self.turtle.turtle.reset()
        self.turtle.turtle.pencolor('orange')  # Setting color for circle
        self.turtle.turtle.pensize(3)  # Setting line thickness for circle
        radius = 50
        self.turtle.turtle.penup()  # Use penup method on the turtle attribute
        self.turtle.turtle.goto(-radius, 0)  # Use goto method on the turtle attribute
        self.turtle.turtle.pendown()  # Use pendown method on the turtle attribute
        self.turtle.turtle.circle(radius)  # Use circle method on the turtle attribute


    def draw_rectangle(self):
        self.turtle.turtle.reset()
        self.turtle.turtle.pencolor('orange')  # Setting color for rectangle
        self.turtle.turtle.pensize(3)  # Setting line thickness for rectangle
        instructions = "forward 100\nright 90\nforward 50\nright 90\nforward 100\nright 90\nforward 50"
        self.instructions.set(instructions)
        self.code_editor.delete("1.0", tk.END)
        self.code_editor.insert(tk.END, instructions)
        self.execute_code()

    def draw_triangle(self):
        self.turtle.turtle.reset()
        self.turtle.turtle.pencolor('orange')  # Setting color for triangle
        self.turtle.turtle.pensize(3)  # Setting line thickness for triangle
        instructions = "forward 100\nright 120\nforward 100\nright 120\nforward 100"
        self.instructions.set(instructions)
        self.code_editor.delete("1.0", tk.END)
        self.code_editor.insert(tk.END, instructions)
        self.execute_code()
    
    def draw_parallelogram(self):
        self.turtle.turtle.reset()
        self.turtle.turtle.pencolor('orange')  
        self.turtle.turtle.pensize(3)
        instructions = "forward 100\nright 60\nforward 50\nright 120\nforward 100\nright 60\nforward 50\nright 120"
        self.instructions.set(instructions)
        self.code_editor.delete("1.0", tk.END)
        self.code_editor.insert(tk.END, instructions)
        self.execute_code()

    def draw_rhombus(self):
        self.turtle.turtle.reset()
        self.turtle.turtle.pencolor('orange')  
        self.turtle.turtle.pensize(3)
        instructions = "forward 100\nright 45\nforward 100\nright 135\nforward 100\nright 45\nforward 100\nright 135"
        self.instructions.set(instructions)
        self.code_editor.delete("1.0", tk.END)
        self.code_editor.insert(tk.END, instructions)
        self.execute_code()

    def draw_trapezium(self):
        self.turtle.turtle.reset()
        self.turtle.turtle.pencolor('orange')  
        self.turtle.turtle.pensize(3)
        instructions = "forward 100\nright 120\nforward 50\nright 60\nforward 80\nright 60\nforward 50\nright 120"
        self.instructions.set(instructions)
        self.code_editor.delete("1.0", tk.END)
        self.code_editor.insert(tk.END, instructions)
        self.execute_code()

    def draw_pentagon(self):
        self.turtle.turtle.reset()
        self.turtle.turtle.pencolor('orange') 
        self.turtle.turtle.pensize(3)
        instructions = "forward 100\nright 72\nforward 100\nright 72\nforward 100\nright 72\nforward 100\nright 72\nforward 100"
        self.instructions.set(instructions)
        self.code_editor.delete("1.0", tk.END)
        self.code_editor.insert(tk.END, instructions)
        self.execute_code()

    def draw_hexagon(self):
        self.turtle.turtle.reset()
        self.turtle.turtle.pencolor('orange')  
        self.turtle.turtle.pensize(3)
        instructions = "forward 100\nright 60\nforward 100\nright 60\nforward 100\nright 60\nforward 100\nright 60\nforward 100\nright 60\nforward 100"
        self.instructions.set(instructions)
        self.code_editor.delete("1.0", tk.END)
        self.code_editor.insert(tk.END, instructions)
        self.execute_code()

    def draw_heptagon(self):
        self.turtle.turtle.reset()
        self.turtle.turtle.pencolor('orange') 
        self.turtle.turtle.pensize(3)
        instructions = "forward 100\nright 51.43\nforward 100\nright 51.43\nforward 100\nright 51.43\nforward 100\nright 51.43\nforward 100\nright 51.43\nforward 100\nright 51.43\nforward 100"
        self.instructions.set(instructions)
        self.code_editor.delete("1.0", tk.END)
        self.code_editor.insert(tk.END, instructions)
        self.execute_code()

    def draw_octagon(self):
        self.turtle.turtle.reset()
        self.turtle.turtle.pencolor('orange')  
        self.turtle.turtle.pensize(3)
        instructions = "forward 100\nright 45\nforward 100\nright 45\nforward 100\nright 45\nforward 100\nright 45\nforward 100\nright 45\nforward 100\nright 45\nforward 100\nright 45\nforward 100"
        self.instructions.set(instructions)
        self.code_editor.delete("1.0", tk.END)
        self.code_editor.insert(tk.END, instructions)
        self.execute_code()

    def draw_custom(self):
        self.turtle.turtle.reset()
        instructions = ("# Try drawing your own shapes!\n"
                        "# Use commands like move_forward, turn_right, etc.\n"
                        "# Example: \n"
                        "# move_forward 50\n"
                        "# turn_right 90\n"
                        "# move_forward 50")
        self.instructions.set(instructions)  
        self.code_editor.delete("1.0", tk.END) 
        self.code_editor.insert(tk.END, instructions)

    def execute_code(self):
        code = self.code_editor.get("1.0", tk.END).strip()  # Retrieve code from the editor
        self.output_display.config(state=tk.NORMAL)
        self.output_display.delete("1.0", tk.END)

        result = self.turtle.execute_code(code)

        if result != "Code executed successfully.":
            self.output_display.insert(tk.END, result, "error")  # Display error in red
        else:
            self.output_display.insert(tk.END, result, "success")  # Display success in green

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
        self.turtle.turtle.setheading(0)
        self.turtle.turtle.pendown()  # Put the pen down to start drawing again

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
    app = DrawShapeTab(None)
    app.geometry("800x600")
    app.mainloop()