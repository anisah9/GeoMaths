import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import math
import turtle

class Turtle:
    def __init__(self, canvas, output_display):
        self.canvas = canvas
        self.output_display = output_display
        self.turtle = turtle.RawTurtle(canvas)
        self.turtle.speed(1)
        self.current_position = (0, 0)

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
        elif tokens[0] == "rotate" and len(tokens) == 2:
            try:
                angle = float(tokens[1])
                self.rotate(angle)
            except ValueError:
                return f"Invalid command: {line}"
        elif tokens[0] == "rotate_shape" and len(tokens) == 2:
            try:
                angle = float(tokens[1])
                self.rotate_shape(angle)
            except ValueError:
                return f"Invalid command: {line}"
        else:
            return f"Invalid command: {line}"

    def move_forward(self, distance):
        self.turtle.forward(distance)
        x, y = self.turtle.position()
        self.current_position = (x, y)

    def turn_right(self, angle):
        self.turtle.right(angle)

    def rotate(self, angle):
        self.turtle.setheading(angle)

    def rotate_shape(self, angle):
        current_x, current_y = self.current_position
        self.turtle.penup()
        self.turtle.goto(0, 0)
        self.turtle.pendown()
        self.turtle.setheading(angle)
        self.turtle.penup()
        self.turtle.goto(current_x, current_y)
        self.turtle.pendown()

    def move_to(self, x, y):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        self.current_position = (x, y)
        self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black")

    def get_current_position(self):
        return self.current_position


class CoordinateTool(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#ecf0f1")
        self.winfo_toplevel().title("Coordinate Tool")

        # Add a button to clear the drawing
        self.clear_drawing_button = tk.Button(self, text="Clear Drawing", command=self.clear_drawing)
        self.clear_drawing_button.grid(row=1, column=4, pady=5, padx=10, sticky=tk.W)

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

        # Inside the __init__ method of the CoordinateTool class, after creating other buttons
        self.move_turtle_button = tk.Button(self, text="Move Turtle", command=self.move_turtle_to_position)
        self.move_turtle_button.grid(row=2, column=4, pady=5, padx=10, sticky=tk.W)

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

    def clear_drawing(self):
        self.turtle_canvas.delete("all")
        self.turtle.turtle.clear()
        self.turtle.turtle.penup()
        self.turtle.turtle.goto(0, 0)
        self.turtle.turtle.pendown()

    def move_turtle_to_position(self):
        input_window = tk.Toplevel(self)
        input_window.title("Enter Coordinates")

        x_label = tk.Label(input_window, text="Enter the x-coordinate:")
        x_label.grid(row=0, column=0, padx=5, pady=5)
        x_entry = tk.Entry(input_window)
        x_entry.grid(row=0, column=1, padx=5, pady=5)

        y_label = tk.Label(input_window, text="Enter the y-coordinate:")
        y_label.grid(row=1, column=0, padx=5, pady=5)
        y_entry = tk.Entry(input_window)
        y_entry.grid(row=1, column=1, padx=5, pady=5)

        def on_button_click():
            try:
                x = float(x_entry.get())
                y = float(y_entry.get())
                input_window.destroy()

                self.turtle.move_to(x, y)
                current_position = self.turtle.get_current_position()

                self.output_display.config(state=tk.NORMAL)
                self.output_display.insert(tk.END, f"Turtle moved to {current_position}\n", "success")
                self.output_display.config(state=tk.DISABLED)
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

        confirm_button = tk.Button(input_window, text="Confirm", command=on_button_click)
        confirm_button.grid(row=2, column=0, columnspan=2, pady=10)


if __name__ == "__main__":
    app = CoordinateTool(None)
    app.geometry("800x600")
    app.mainloop()











