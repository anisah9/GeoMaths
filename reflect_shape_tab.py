import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import turtle


class Turtle:
    def __init__(self, canvas, output_display):
        self.canvas = canvas
        self.output_display = output_display
        self.turtle = turtle.RawTurtle(canvas)
        self.turtle.speed(1)

        self.grid_turtle = turtle.RawTurtle(canvas)
        self.grid_turtle.speed(0)
        self.grid_turtle.penup()
        self.grid_turtle.hideturtle()
        self.draw_grid()

    def execute_code(self, code):
        self.turtle.clear()  # Clear previous drawing without removing the grid
        lines = code.split('\n')
        for line in lines:
            result = self.execute_line(line.strip())
            if result and "Invalid command" in result:
                self.output_display.config(state=tk.NORMAL)
                self.output_display.insert(tk.END, result + "\n", "error")
                self.output_display.config(state=tk.DISABLED)
                return  # Exit on first error encountered
        self.output_display.config(state=tk.NORMAL)
        self.output_display.insert(tk.END, "Code executed successfully.\n", "success")
        self.output_display.config(state=tk.DISABLED)

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
        elif tokens[0] == "goto" and len(tokens) == 3:  # Handle goto command
            try:
                x = float(tokens[1])
                y = float(tokens[2])
                self.goto(x, y)
            except ValueError:
                return f"Invalid command: {line}"
        else:
            return f"Invalid command: {line}"


    def move_forward(self, distance):
        self.turtle.forward(distance)

    def turn_right(self, angle):
        self.turtle.right(angle)
    
    def goto(self, x, y):
        self.turtle.penup()  # Lift the pen to move without drawing
        self.turtle.goto(x, y)  # Move the turtle to the specified coordinates
        self.turtle.pendown()  # Put the pen down to resume drawing


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


class ReflectShapeTab(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#ecf0f1")

        # Setup label, text editor, and buttons 
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

    def execute_code(self):
        # Retrieve the code directly from the code_editor widget
        code = self.code_editor.get("1.0", tk.END)
        execution_result = self.turtle.execute_code(code)
    
    def clear_drawing(self):
        # Clear turtle's drawings without removing the grid
        self.turtle.turtle.clear()  
        self.turtle.turtle.penup()
        self.turtle.turtle.goto(0, 0)
        self.turtle.turtle.setheading(0)
        self.turtle.turtle.pendown()
        self.turtle.draw_grid()

    
    
if __name__ == "__main__":
    app = ReflectShapeTab(None)
    app.geometry("800x600")
    app.mainloop()


