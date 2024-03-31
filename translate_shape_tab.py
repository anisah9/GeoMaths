import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import turtle 
import io

from tkinter import filedialog
from tkinter import messagebox



class Turtle:
    def __init__(self, canvas, output_display):
        self.canvas = canvas
        self.output_display = output_display
        self.turtle = turtle.RawTurtle(canvas)
        self.turtle.speed(0)  # Draw as fast as possible
        self.turtle.penup()
        self.turtle.pencolor('#e0e0e0')  # Light grey for the grid lines
        self.draw_grid()  # Draw the grid
        self.turtle.speed(1)  # Reset drawing speed for user commands
        self.turtle.pencolor('black')

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

    def draw_grid(self):
        # Set the screen to update only when .update() is called
        self.canvas.update()
        self.turtle.speed(0)  # Temporarily set speed to fastest for grid drawing
        # Draw vertical lines
        for x in range(-250, 251, 50):  # Adjust range and step for grid size and spacing
            self.turtle.penup()
            self.turtle.goto(x, -250)
            self.turtle.pendown()
            self.turtle.goto(x, 250)
        # Draw horizontal lines
        for y in range(-250, 251, 50):
            self.turtle.penup()
            self.turtle.goto(-250, y)
            self.turtle.pendown()
            self.turtle.goto(250, y)
        self.turtle.penup()
        self.turtle.home()  # Return to the center
        # Ensure the turtle's initial state is ready for drawing
        self.turtle.pendown()



class TranslateShapeTab(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#ecf0f1")
        self.winfo_toplevel().title("Geometry Tool")


       # Add a label next to the text editor
        editor_info_label = tk.Label(self, text="Enter your drawing instructions below:", font=("Arial", 13), bg="#ecf0f1")
        editor_info_label.grid(row=1, column=1, pady=10, padx=10, sticky=tk.W)


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

        # Initialize mode
        self.drawing_mode = True

    

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


    def clear_turtle_canvas(self):
        self.turtle_canvas.delete("all")

    def clear_drawing(self):
        print("Clear Drawing method called.")
        self.turtle.turtle.clear()
        self.turtle.turtle.penup()
        self.turtle.turtle.goto(0, 0)
        self.turtle.turtle.pendown()
        self.turtle.turtle.pen(pencolor='black', pensize=2)  # Reapply pen settings for visibility



if __name__ == "__main__":
    app = TranslateShapeTab(None)
    app.geometry("800x600")
    app.mainloop()



