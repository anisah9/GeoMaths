import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import turtle
import random


class Turtle:
    def __init__(self, canvas, output_display):
        self.canvas = canvas
        self.output_display = output_display
        self.turtle = turtle.RawTurtle(canvas)
        self.turtle.speed(1)
        self.vertices = []  # To store shape vertices

        self.grid_turtle = turtle.RawTurtle(canvas)
        self.grid_turtle.speed(0)
        self.grid_turtle.penup()
        self.grid_turtle.hideturtle()
        self.draw_grid()

        self.vertices = []  # To store shape vertices

    def execute_code(self, code):
        self.vertices.clear() 

        lines = code.split('\n')
        for line in lines:
            result = self.execute_line(line.strip())
            if result and "Invalid command" in result:
                self.output_display.config(state=tk.NORMAL)
                self.output_display.insert(tk.END, result + "\n", "error")
                self.output_display.config(state=tk.DISABLED)
                return  # Exit on first error encountered
            
        if hasattr(self, 'expected_vertices') and self.expected_vertices:
            if self.compare_shapes(self.expected_vertices):
                feedback = "Congratulations! The reflection was performed correctly."
            else:
                feedback = "The reflection did not match the expected outcome. Please try again."
            # Provide feedback based on the comparison
            self.output_display.config(state=tk.NORMAL)
            self.output_display.insert(tk.END, feedback + "\n", "feedback")
            self.output_display.config(state=tk.DISABLED)
        else:
            # If no reflection was expected/attempted, just confirm successful execution
            self.output_display.config(state=tk.NORMAL)
            self.output_display.insert(tk.END, "Code executed successfully.\nVertices: " + str(self.vertices) + "\n", "success")
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
        elif tokens[0] == "goto" and len(tokens) == 3:
            try:
                x = float(tokens[1])
                y = float(tokens[2])
                self.goto(x, y)
            except ValueError:
                return f"Invalid command: {line}"
        elif tokens[0] == "reflect" and len(tokens) == 2:
            if tokens[1] in ['x', 'y']:
                self.reflect_shape(tokens[1])
            else:
                return f"Invalid reflection axis: {line}"
        else:
            return f"Invalid command: {line}"


    def move_forward(self, distance):
        start_pos = self.turtle.pos()
        self.turtle.forward(distance)
        end_pos = self.turtle.pos()
        self.vertices.extend([start_pos, end_pos])  # Store both start and end vertices

    def turn_right(self, angle):
        self.turtle.right(angle)
    
    def goto(self, x, y):
        self.turtle.penup()  # Lift the pen to move without drawing
        self.turtle.goto(x, y)  # Move the turtle to the specified coordinates
        self.vertices.append((x, y))  # Store the vertex
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
    
    def reflect_shape(self, axis):
        if axis == 'x':
            self.vertices = [(x, -y) for x, y in self.vertices]
        elif axis == 'y':
            self.vertices = [(-x, y) for x, y in self.vertices]

    def calculate_reflected_vertices(self, axis):

        reflected_vertices = []
        if axis == 'x':
            reflected_vertices = [(x, -y) for x, y in self.vertices]
        elif axis == 'y':
            reflected_vertices = [(-x, y) for x, y in self.vertices]
        return reflected_vertices
    
    def simplify_vertices(self, vertices):
        if not vertices:
            return []
        simplified = [vertices[0]]
        for current_vertex in vertices[1:]:
            if current_vertex != simplified[-1]:
                simplified.append(current_vertex)
        return simplified


    
    def compare_shapes(self, expected_vertices, actual_vertices):
        tolerance = 1e-5
        
        actual_simplified = self.simplify_vertices(actual_vertices)
        expected_simplified = self.simplify_vertices(expected_vertices)
        
        if len(actual_simplified) != len(expected_simplified):
            return False
        for (ax, ay), (ex, ey) in zip(actual_simplified, expected_simplified):
            if abs(ax - ex) > tolerance or abs(ay - ey) > tolerance:
                return False
        return True
    

    def draw_expected_reflection(self, expected_vertices):
        self.grid_turtle.color("blue")  
        self.grid_turtle.penup()
        for vertex in expected_vertices:
            self.grid_turtle.goto(vertex)
            self.grid_turtle.pendown()

        self.grid_turtle.goto(expected_vertices[0])
        self.grid_turtle.penup()



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

        # Modified to include drawing and question generation
        self.draw_random_shape_button = tk.Button(self, text="Draw Random Shape", command=self.draw_random_shape_and_question)
        self.draw_random_shape_button.grid(row=8, column=1, pady=5, padx=10, sticky=tk.W)

        # Label to display the reflection question
        self.question_label = tk.Label(self, text="", font=("Arial", 13), bg="#ecf0f1")
        self.question_label.grid(row=9, column=1, pady=10, padx=10, sticky=tk.W)


    def execute_code(self):
        code = self.code_editor.get("1.0", tk.END)
        self.turtle.execute_code(code)

        # Draw the expected reflection for visual comparison
        self.turtle.draw_expected_reflection(self.expected_vertices)

        actual_simplified = self.turtle.simplify_vertices(self.turtle.vertices)
        expected_simplified = self.turtle.simplify_vertices(self.expected_vertices)

        if self.turtle.compare_shapes(expected_simplified, actual_simplified):
            feedback = "Congratulations! The reflection was performed correctly."
        else:
            feedback = "Please adjust your drawing to match the blue outline."
        self.output_display.config(state=tk.NORMAL)
        self.output_display.insert(tk.END, feedback + "\n", "feedback")
        self.output_display.config(state=tk.DISABLED)

    
    def clear_drawing(self):
        self.turtle.turtle.clear()
        self.turtle.vertices.clear()
        self.turtle.turtle.penup()
        self.turtle.turtle.goto(0, 0)
        self.turtle.turtle.setheading(0)
        self.turtle.turtle.pendown()
        self.turtle.draw_grid()
    
    def draw_random_shape(self):
        shapes = ['square', 'rectangle', 'triangle']
        # Choose a random shape
        shape = random.choice(shapes)

        grid_positions = range(-250, 251, 50)  
        start_x = random.choice(grid_positions)
        start_y = random.choice(grid_positions)

        self.turtle.turtle.clear() 
        self.turtle.goto(start_x, start_y) 

        if shape == 'square':
            side_length = 50  
            for _ in range(4):
                self.turtle.move_forward(side_length)
                self.turtle.turn_right(90)
        elif shape == 'rectangle':
            length = 100  
            width = 50 
            for _ in range(2):
                self.turtle.move_forward(length)  
                self.turtle.turn_right(90)
                self.turtle.move_forward(width) 
                self.turtle.turn_right(90)
        elif shape == 'triangle':
            side_length = 50  
            for _ in range(3):
                self.turtle.move_forward(side_length)
                self.turtle.turn_right(120)

        # self.turtle.turtle.penup()
        # self.turtle.turtle.goto(0, 0)
        # self.turtle.turtle.setheading(0)
        self.turtle.turtle.pendown()
    
    def draw_random_shape_and_question(self):
        self.draw_random_shape()
        questions = ["Reflect the shape in the x-axis.", "Reflect the shape in the y-axis."]
        selected_question = random.choice(questions)
        self.question_label.config(text=selected_question)

        reflection_axis = 'x' if "x-axis" in selected_question else 'y'
        self.expected_vertices = self.turtle.calculate_reflected_vertices(reflection_axis)
    
if __name__ == "__main__":
    app = ReflectShapeTab(None)
    app.geometry("800x600")
    app.mainloop()


