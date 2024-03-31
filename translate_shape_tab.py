import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import turtle

class Turtle:
    def __init__(self, canvas, output_display):
        self.canvas = canvas
        self.output_display = output_display
        # Separate turtles for grid and user drawings
        self.grid_turtle = turtle.RawTurtle(canvas)
        self.user_turtle = turtle.RawTurtle(canvas)
        self.setup_turtles()
        self.draw_grid()

    def setup_turtles(self):
        # Setup for grid turtle
        self.grid_turtle.speed(0)
        self.grid_turtle.penup()
        self.grid_turtle.pencolor('#e0e0e0')
        self.grid_turtle.hideturtle()

        # Setup for user turtle
        self.user_turtle.speed(1)
        self.user_turtle.pencolor('black')
        self.user_turtle.penup()
        self.user_turtle.goto(0, 0)
        self.user_turtle.pendown()

    def draw_grid(self):
        self.grid_turtle.speed(0)  # Draw grid fast
        for x in range(-250, 251, 50):
            self.grid_turtle.penup()
            self.grid_turtle.goto(x, -250)
            self.grid_turtle.pendown()
            self.grid_turtle.goto(x, 250)
        for y in range(-250, 251, 50):
            self.grid_turtle.penup()
            self.grid_turtle.goto(-250, y)
            self.grid_turtle.pendown()
            self.grid_turtle.goto(250, y)

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

        try:
            if tokens[0] == "forward" and len(tokens) == 2:
                distance = float(tokens[1])
                self.user_turtle.forward(distance)
            elif tokens[0] == "right" and len(tokens) == 2:
                angle = float(tokens[1])
                self.user_turtle.right(angle)
            else:
                return f"Invalid command: {line}"
        except ValueError:
            return f"Invalid command: {line}"

    def clear_user_drawings(self):
        self.user_turtle.clear()

class TranslateShapeTab(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#ecf0f1")
        self.winfo_toplevel().title("Geometry Tool")

        editor_info_label = tk.Label(self, text="Enter your drawing instructions below:", font=("Arial", 13), bg="#ecf0f1")
        editor_info_label.grid(row=1, column=1, pady=10, padx=10, sticky=tk.W)

        self.clear_drawing_button = tk.Button(self, text="Clear Drawing", command=self.clear_user_drawings)
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

    def execute_code(self):
        code = self.code_editor.get("1.0", tk.END)
        self.output_display.config(state=tk.NORMAL)
        self.output_display.delete("1.0", tk.END)

        result = self.turtle.execute_code(code)

        if "Invalid command" in result:
            self.output_display.insert(tk.END, result, "error")
        else:
            self.output_display.insert(tk.END, "Code executed successfully.", "success")

        self.output_display.config(state=tk.DISABLED)

    def clear_user_drawings(self):
        self.turtle.clear_user_drawings()

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslateShapeTab(root)
    app.pack(fill="both", expand=True)
    root.geometry("800x600")
    root.mainloop()



