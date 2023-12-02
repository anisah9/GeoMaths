import tkinter as tk
from tkinter import scrolledtext
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
        print("GeometryTool __init__ method")
        tk.Frame.__init__(self, master)
        self.winfo_toplevel().title("Geometry Tool") 

        self.code_editor = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=20)
        self.code_editor.pack(padx=10, pady=10)

        self.execute_button = tk.Button(self, text="Run Code", command=self.execute_code)
        self.execute_button.pack(pady=5)

        self.output_display = tk.Text(self, wrap=tk.WORD, state=tk.DISABLED, width=50, height=10)
        self.output_display.pack(padx=10, pady=10)

        self.turtle_canvas = tk.Canvas(self, width=500, height=500, bg="white")
        self.turtle_canvas.pack(padx=10, pady=10)

        self.turtle = Turtle(self.turtle_canvas)

    def execute_code(self):
        code = self.code_editor.get("1.0", tk.END)
        self.output_display.config(state=tk.NORMAL)
        self.output_display.delete("1.0", tk.END)
        result = self.turtle.execute_code(code)
        self.output_display.insert(tk.END, result)
        self.output_display.config(state=tk.DISABLED)



