import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import math

class Turtle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.turtle_id = self.canvas.create_line(250, 250, 250, 250, width=2, fill="black")
        self.pen_down = True
        self.angle = 0  # Initial angle

    def execute_code(self, code):
        lines = code.split('\n')
        for line in lines:
            self.execute_line(line.strip())

        return "Code executed successfully."

    def execute_line(self, line):
        tokens = line.split()

        if not tokens:
            print("Invalid command: Empty line")
            return
        
        if tokens[0] == "move_forward" and len(tokens) == 2:
            try:
                distance = float(tokens[1])
                self.move_forward(distance)
            except ValueError:
                print(f"Invalid command: {line}")
        elif tokens[0] == "turn_right" and len(tokens) == 2:
            try:
                angle = float(tokens[1])
                self.turn_right(angle)
            except ValueError:
                print(f"Invalid command: {line}")
        else:
            print(f"Invalid command: {line}")
            self.canvas.create_text(
                10, 10, anchor=tk.NW,
                text=f"Error: Invalid command - {line}", font=("Arial", 12), fill="red"
            )


    def draw_line(self, distance):
        angle_radians = self.angle * (3.141592653589793 / 180.0)
        new_x = self.canvas.coords(self.turtle_id)[2] + distance * math.cos(angle_radians)
        new_y = self.canvas.coords(self.turtle_id)[3] + distance * math.sin(angle_radians)

        if self.pen_down:
            self.canvas.create_line(
                self.canvas.coords(self.turtle_id)[2],
                self.canvas.coords(self.turtle_id)[3],
                new_x,
                new_y,
                width=2,
                fill="black"
            )

        self.canvas.coords(self.turtle_id, new_x - 1, new_y - 1, new_x + 1, new_y + 1)

    def move_forward(self, distance):
        self.draw_line(distance)

    def turn_right(self, angle):
        self.angle -= angle


class GeometryTool(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#ecf0f1")
        self.winfo_toplevel().title("Geometry Tool")

        self.welcome_message_shown = False
        self.bind("<Enter>", self.on_page_enter)
    
        

        # Add a set of instructions
        self.instructions_label = tk.Label(self, text="Instructions:", font=("Arial", 13), bg="#ecf0f1")
        self.instructions_label.grid(row=0, column=0, pady=10, sticky=tk.W)

        self.instructions = tk.StringVar()
        self.instructions.set("")

       # Add a label next to the text editor
        editor_info_label = tk.Label(self, text="Enter your drawing instructions below:", font=("Arial", 13), bg="#ecf0f1")
        editor_info_label.grid(row=1, column=1, pady=10, padx=10, sticky=tk.W)

        self.instructions_entry = tk.Entry(self, textvariable=self.instructions, width=50)
        self.instructions_entry.grid(row=0, column=1, pady=5, padx=10, sticky=tk.W, ipady=10)  # Adjust ipady as needed

        # # Add a button to execute the instructions
        # self.execute_instructions_button = tk.Button(self, text="Execute Instructions", command=self.execute_instructions)
        # self.execute_instructions_button.grid(row=0, column=2, pady=5, padx=10, sticky=tk.W)

        # Add a button to copy instructions to clipboard
        self.copy_instructions_button = tk.Button(self, text="Copy Instructions", command=self.copy_instructions)
        self.copy_instructions_button.grid(row=0, column=3, pady=5, padx=10, sticky=tk.W)

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

        self.turtle = Turtle(self.turtle_canvas)

    def draw_square(self):
        instructions = "move_forward 50\nturn_right 90\nmove_forward 50\nturn_right 90\nmove_forward 50\nturn_right 90\nmove_forward 50"
        self.instructions.set(instructions)

    def draw_circle(self):
        instructions = "repeat 360 [move_forward 1\nturn_right 1]"
        self.instructions.set(instructions)

    def draw_rectangle(self):
        instructions = "move_forward 100\nturn_right 90\nmove_forward 50\nturn_right 90\nmove_forward 100\nturn_right 90\nmove_forward 50"
        self.instructions.set(instructions)

    def draw_triangle(self):
        instructions = "move_forward 100\nturn_right 120\nmove_forward 100\nturn_right 120\nmove_forward 100"
        self.instructions.set(instructions)

    def draw_custom(self):
        instructions = "# Try drawing your own shapes!\n# Use commands like move_forward, turn_right, etc.\n# Example: move_forward 50\nturn_right 90\nmove_forward 50"
        self.instructions.set(instructions)

    def execute_code(self):
        code = self.code_editor.get("1.0", tk.END)
        self.output_display.config(state=tk.NORMAL)
        self.output_display.delete("1.0", tk.END)
        result = self.turtle.execute_code(code)
        self.output_display.insert(tk.END, result)
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

    def copy_instructions(self):
        instructions_text = self.instructions.get()
        if instructions_text:
            self.clipboard_clear()
            self.clipboard_append(instructions_text)
            messagebox.showinfo("Copy Instructions", "Instructions copied to clipboard.")
        else:
            messagebox.showwarning("Copy Instructions", "No instructions to copy.")


    def clear_drawing(self):
        print("Clear Drawing method called.")
        self.turtle_canvas.delete("all")

    def on_page_enter(self, event):
        if not self.welcome_message_shown:
            self.show_welcome_message()
            self.welcome_message_shown = True

    def show_welcome_message(self):
        welcome_message = (
            "Welcome to the Learn 2D Shapes page!\n\n"
            "Click on the shape buttons to see how to draw some shapes, copy the text and then click 'Run Code' to see the result!\n\nPress the Draw Custom shape to draw a custom shape! "
        )
        messagebox.showinfo("Learn 2D Shapes", welcome_message)


if __name__ == "__main__":
    app = GeometryTool(None)
    app.geometry("800x600")
    app.mainloop()