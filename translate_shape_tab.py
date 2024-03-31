import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import turtle
import random


class Turtle:
    def __init__(self, canvas, output_display):
        self.canvas = canvas
        self.output_display = output_display

        self.grid_turtle = turtle.RawTurtle(canvas)
        self.grid_turtle.speed(0) 
        self.grid_turtle.penup()
        self.grid_turtle.hideturtle()  
        self.draw_grid() 

        self.drawing_turtle = turtle.RawTurtle(canvas)
        self.drawing_turtle.speed(1) 
        self.drawing_turtle.pencolor('black')

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

        command = tokens[0]
        if command in ["forward", "right"] and len(tokens) == 2:
            try:
                value = float(tokens[1])
                if command == "forward":
                    self.move_forward(value)
                elif command == "right":
                    self.turn_right(value)
            except ValueError:
                return f"Invalid command: {line}"
        else:
            return f"Invalid command: {line}"

    def move_forward(self, distance):
        self.drawing_turtle.forward(distance)

    def turn_right(self, angle):
        self.drawing_turtle.right(angle)

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

        # Drawing axes with a different color and pen size
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
    
    def draw_random_shape(self):
        shape = random.choice(['square', 'triangle', 'rectangle'])
        grid_size = 50  # Grid spacing

        # Adjust starting point to align with the grid
        x = random.randint(-200, 200) // grid_size * grid_size
        y = random.randint(-200, 200) // grid_size * grid_size

        self.drawing_turtle.penup()
        self.drawing_turtle.goto(x, y)
        self.drawing_turtle.pendown()

        if shape == 'square':
            # Ensure side length is a multiple of grid_size
            side = random.randint(1, 4) * grid_size
            for _ in range(4):
                self.drawing_turtle.forward(side)
                self.drawing_turtle.right(90)
        elif shape == 'triangle':
            # Ensure base length is a multiple of grid_size
            side = random.randint(1, 4) * grid_size
            for _ in range(3):
                self.drawing_turtle.forward(side)
                self.drawing_turtle.right(120)
        elif shape == 'rectangle':
            # Ensure length and width are multiples of grid_size
            length = random.randint(1, 6) * grid_size
            width = random.randint(1, 3) * grid_size
            for _ in range(2):
                self.drawing_turtle.forward(length)
                self.drawing_turtle.right(90)
                self.drawing_turtle.forward(width)
                self.drawing_turtle.right(90)





class TranslateShapeTab(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#ecf0f1")
        self.winfo_toplevel().title("Geometry Tool")

        # Setup label, text editor, and buttons as before
        editor_info_label = tk.Label(self, text="Enter your drawing instructions below:", font=("Arial", 13), bg="#ecf0f1")
        editor_info_label.grid(row=1, column=1, pady=10, padx=10, sticky=tk.W)

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

        self.draw_random_shape_button = tk.Button(self, text="Draw Random Shape", command=self.draw_random_shape)
        self.draw_random_shape_button.grid(row=8, column=1, pady=5, padx=10, sticky=tk.W)


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

    def clear_drawing(self):
        # This method now correctly clears only the user's drawings, not the grid or axes
        self.turtle.drawing_turtle.clear()
    
    def draw_random_shape(self):
        self.turtle.draw_random_shape()

if __name__ == "__main__":
    app = TranslateShapeTab(None)
    app.geometry("800x600")
    app.mainloop()