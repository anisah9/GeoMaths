# reflect_shape_tab.py
import tkinter as tk
from tkinter import scrolledtext
from tkinter.font import Font
import turtle
import random

class Turtle:
    def __init__(self, canvas, output_display):
        self.canvas = canvas    # Initialise the canvas
        self.output_display = output_display    # Initialise the output display widget
        self.turtle = turtle.RawTurtle(canvas)  # Create a turtle object for drawing
        self.turtle.speed(1)    # Set the speed of the turtle
        self.pen_color = 'black'    # Set the default pen color
        self.vertices = []  # To store shape vertices

        # Create a turtle object for drawing the grid
        self.grid_turtle = turtle.RawTurtle(canvas)
        self.grid_turtle.speed(0)   # Set the speed of the grid turtle
        self.grid_turtle.penup()    # Lift the pen up
        self.grid_turtle.hideturtle()   # Hide the grid turtle
        self.draw_grid()    # Draw the grid on the canvas

        self.vertices = []  # To store shape vertices

    def execute_code(self, code):
        self.turtle.pencolor('green') 
        self.turtle.pensize(3)
        self.vertices.clear() 

        # Split the code into individual lines
        lines = code.split('\n')
        for line in lines:
            # Execute each line of code
            result = self.execute_line(line.strip())
            if result and "Invalid command" in result:
                # Display error message if an invalid command is encountered
                self.output_display.config(state=tk.NORMAL)
                self.output_display.insert(tk.END, result + "\n", "error")
                self.output_display.config(state=tk.DISABLED)
                return  # Exit on first error encountered
        
        # Check if expected vertices are defined and compare shapes if so
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
            # Display success message along with vertices if no expected vertices are defined
            self.output_display.config(state=tk.NORMAL)
            self.output_display.insert(tk.END, "Code executed successfully.\nVertices: " + str(self.vertices) + "\n", "success")
            self.output_display.config(state=tk.DISABLED)

    def execute_line(self, line):
        # Split the line into tokens
        tokens = line.split()

        # Ignore empty lines
        if not tokens:
            return None  

        # Check the command and its arguments
        if tokens[0] == "forward" and len(tokens) == 2:
            try:
                # Move the turtle forward by the specified distance
                distance = float(tokens[1])
                self.move_forward(distance)
            except ValueError:
                # Handle invalid command if distance is not a number
                return f"Invalid command: {line}"
        elif tokens[0] == "right" and len(tokens) == 2:
            try:
                # Turn the turtle right by the specified angle
                angle = float(tokens[1])
                self.turn_right(angle)
            except ValueError:
                # Handle invalid command if angle is not a number
                return f"Invalid command: {line}"
        elif tokens[0] == "goto" and len(tokens) == 3:
            try:
                # Move the turtle to the specified coordinates
                x = float(tokens[1])
                y = float(tokens[2])
                self.goto(x, y)
            except ValueError:
                # Handle invalid command if coordinates are not numbers
                return f"Invalid command: {line}"
        elif tokens[0] == "reflect" and len(tokens) == 2:
            if tokens[1] in ['x', 'y']:
                # Reflect the shape along the specified axis
                self.reflect_shape(tokens[1])
            else:
                # Handle invalid reflection axis
                return f"Invalid reflection axis: {line}"
        else:
            return f"Invalid command: {line}"


    def move_forward(self, distance):
        # Record the starting position
        start_pos = self.turtle.pos()
        # Move the turtle forward by the specified distance
        self.turtle.forward(distance)
        # Record the ending position
        end_pos = self.turtle.pos()
         # Store both the start and end vertices
        self.vertices.extend([start_pos, end_pos])  

    def turn_right(self, angle):
        # Turn the turtle to the right by the specified angle
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

        self.grid_turtle.pencolor('black')  
        self.grid_turtle.pensize(2)  

        # Draw x-axis
        self.grid_turtle.penup()
        self.grid_turtle.goto(-250, 0)
        self.grid_turtle.pendown()
        self.grid_turtle.goto(250, 0)

        self.grid_turtle.penup()
        self.grid_turtle.goto(0, -250)
        self.grid_turtle.pendown()
        self.grid_turtle.goto(0, 250)

        self.grid_turtle.penup()  

        for x in range(-250, 251, 50):
            self.grid_turtle.penup()
            self.grid_turtle.goto(x, -10)  
            self.grid_turtle.pendown()
            if x != 0:  
                self.grid_turtle.write(str(x), align="center", font=("Arial", 8, "normal"))

        for y in range(-250, 251, 50):
            self.grid_turtle.penup()
            self.grid_turtle.goto(-20, y)  
            self.grid_turtle.pendown()
            if y != 0:  
                self.grid_turtle.write(str(y), align="right", font=("Arial", 8, "normal"))
    
    def reflect_shape(self, axis):
        # Reflect the shape vertices across the specified axis
        if axis == 'x':
            self.vertices = [(x, -y) for x, y in self.vertices]
        elif axis == 'y':
            self.vertices = [(-x, y) for x, y in self.vertices]

    def calculate_reflected_vertices(self, axis):
        # Calculate the vertices of the reflected shape without modifying the original vertices
        reflected_vertices = []
        if axis == 'x':
            reflected_vertices = [(x, -y) for x, y in self.vertices]
        elif axis == 'y':
            reflected_vertices = [(-x, y) for x, y in self.vertices]
        return reflected_vertices
    
    def simplify_vertices(self, vertices):
        # Remove duplicate consecutive vertices to simplify the shape representation
        if not vertices:
            return []
        simplified = [vertices[0]]
        for current_vertex in vertices[1:]:
            if current_vertex != simplified[-1]:
                simplified.append(current_vertex)
        return simplified
    
    def compare_shapes(self, expected_vertices, actual_vertices):
        # Compare two sets of vertices for equality with a specified tolerance
        tolerance = 1e-5
        
        # Simplify both sets of vertices to remove duplicate consecutive vertices
        actual_simplified = self.simplify_vertices(actual_vertices)
        expected_simplified = self.simplify_vertices(expected_vertices)
        
        # If the simplified sets have different lengths, shapes are not equal
        if len(actual_simplified) != len(expected_simplified):
            return False
        
        # Compare corresponding vertices in both sets with tolerance
        for (ax, ay), (ex, ey) in zip(actual_simplified, expected_simplified):
            if abs(ax - ex) > tolerance or abs(ay - ey) > tolerance:
                return False
        return True
    
    def draw_expected_reflection(self, expected_vertices):
        # Draw the expected reflected shape on the grid
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

        # Left Panel
        left_panel = tk.Frame(self, bg="white", width=350)
        left_panel.grid(row=0, column=0, rowspan=10, padx=5, pady=5, sticky="nsew")

        # Text widget for displaying information
        text_widget = tk.Text(left_panel, height=15, width=50, wrap=tk.WORD)
        text_widget.grid(row=0, column=0, padx=10, pady=10)

        # Define font styles
        title_font = Font(family="Arial", size=16, weight="bold")
        text_font = Font(family="Arial", size=14)

        # Insert text content
        text_widget.insert(tk.END, "Welcome to the Reflect Shape Tab\n", "title")
        text_widget.insert(tk.END, "\n")  
        text_widget.insert(tk.END, "Welcome to the Reflect Shape Tab! Dive into an interactive space designed to enhance your understanding of shape reflection through coding. Embark on a hands-on journey where you can manipulate shapes across the canvas using coding commands. Delight in exploring how coding can transform geometric configurations and deepen your comprehension of coordinate systems. To begin, click the 'Draw Random Shape' button and follow the instructions provided below.", "text")

        # Configure text tags
        text_widget.tag_configure("title", font=title_font)
        text_widget.tag_configure("text", font=text_font)
        # Disable text widget for viewing only
        text_widget.configure(state='disabled') 

        # Label for editor information
        editor_info_label = tk.Label(left_panel, text="Enter your drawing instructions below:", font=("Arial", 13), bg="#ecf0f1")
        editor_info_label.grid(row=1, column=0, pady=5, padx=10, sticky=tk.W)

        # Code editor area
        self.code_editor = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=15)
        self.code_editor.grid(row=3, column=0, rowspan=5, pady=10, padx=10, sticky=tk.W)

        # Button to execute code
        self.execute_button = tk.Button(self, text="Run Code", command=self.execute_code)
        self.execute_button.grid(row=7, column=0, pady=5, padx=10, sticky=tk.W)

        # Text display area for output
        self.output_display = tk.Text(self, wrap=tk.WORD, state=tk.DISABLED, width=50, height=10)
        self.output_display.grid(row=8, column=0, pady=10, padx=10, sticky=tk.W)

        # Configure tags for output display
        self.output_display.tag_config("error", foreground="red")
        self.output_display.tag_config("success", foreground="green")

        # Canvas for drawing shapes
        self.turtle_canvas = tk.Canvas(self, width=570, height=570, bg="white")
        self.turtle_canvas.grid(row=1, column=3, rowspan=7, pady=10, padx=10, sticky=tk.W)
         # Create a Turtle object for drawing on the canvas
        self.turtle = Turtle(self.turtle_canvas, self.output_display)

        # Right Panel
        right_panel = tk.Frame(self, bg="white", width=350)
        right_panel.grid(row=0, column=4, rowspan=10, padx=5, pady=5, sticky="nsew")

        # Text box for displaying information
        info_box = tk.Text(right_panel, height= 23, width =40, wrap=tk.WORD, font=("Arial", 14))
        info_box.grid(row=0, column=0, padx=10, pady=10)

        title_font = Font(family="Arial", size=16, weight="bold")

        # Insert title into the information box
        info_box.insert(tk.END, "Reflection\n", "bold")
        info_box.insert(tk.END, "\n")

        reflection_text = (
            "Reflection, in geometry, is like flipping an image over a line so that the original and its "
            "image are exact opposites, yet they are the same distance from the line. It's like having a "
            "sticker on one side of a page and seeing its mirror image on the other side after flipping "
            "it over the spine of a book.\n\n"
            "The line that you flip the shape over is called the line of reflection. It acts as the mirror. "
            "When you perform a reflection, each point of the original shape appears directly opposite on the "
            "other side of the line.\n\n"
            "For example, if you have a point or a part of a shape that is 2 squares away from the line of "
            "reflection to the left, its reflected image will be 2 squares away to the right. It’s as if every "
            "point jumps straight across to the other side of the 'mirror' line, the same distance away, but directly opposite."
        )
        # Insert reflection text into the information box
        info_box.insert(tk.END, reflection_text)

        # Configure text tag for bold font
        info_box.tag_configure("bold", font=title_font)

        # Disable the information box for viewing only
        info_box.configure(state="disabled")

        # Button to draw a random reflection question
        self.draw_random_shape_button = tk.Button(right_panel, text="Draw Reflection Question", command=self.draw_random_shape_and_question)
        self.draw_random_shape_button.grid(row=1, column=0, pady=2, padx=10, sticky=tk.W)

        # Label for displaying reflection question
        self.question_label = tk.Label(right_panel, text="", font=("Arial", 13), bg="#ecf0f1")
        self.question_label.grid(row=2, column=0, pady=2, padx=10, sticky=tk.W)

        instructions_text = (
            "Reflection Instructions:\n"
            "1. Observe the randomly drawn shape on the canvas.\n"
            "2. Use the provided tools to reflect the shape across the indicated line of reflection.\n"
            "3. Input the necessary commands in the command editor to draw the reflected shape.\n"
            "4. Press the 'Run Code' button to execute your commands and display the reflection on the canvas.\n"
            "5. Once executed, the correct reflection will be shown on the canvas. Compare it to your drawn shape to see if it's accurate. If it's not, modify your commands in the code editor to get the correct reflection.\n"
            "6. Ensure that the reflected shape maintains the same orientation and size as the original.\n"
            "Good luck with your reflection exercise!"
        )

        # Create a text box for displaying instructions
        instructions_box = tk.Text(right_panel, height=10, width=35, wrap=tk.WORD, font=("Arial", 14))
        instructions_box.grid(row=3, column=0, padx=10, pady=10)  # Make sure row is set to the next available position
        instructions_box.insert(tk.END, instructions_text)
        instructions_box.configure(state="disabled", bg="#ecf0f1")

        # Button to clear the drawing
        self.clear_drawing_button = tk.Button(self, text="Clear Drawing", command=self.clear_drawing)
        self.clear_drawing_button.grid(row=8, column=4, pady=5, padx=10, sticky=tk.W)

        # Button to check the reflection
        self.check_reflection_button = tk.Button(self, text="Check Reflection", command=self.check_reflection)
        self.check_reflection_button.grid(row=8, column=3, pady=5, padx=10, sticky=tk.W)
        self.check_reflection_button.grid_remove()

    def execute_code(self):
        # Get the code from the code editor
        code = self.code_editor.get("1.0", tk.END)
        # Execute the code using the turtle
        self.turtle.execute_code(code)
        # Make the "Check Reflection" button visible
        self.check_reflection_button.grid()  

    def check_reflection(self):
        # Simplify actual and expected vertices
        actual_simplified = self.turtle.simplify_vertices(self.turtle.vertices)
        expected_simplified = self.turtle.simplify_vertices(self.expected_vertices)
        # Draw the expected reflection
        self.turtle.draw_expected_reflection(self.expected_vertices) 
        # Compare actual and expected shapes
        if self.turtle.compare_shapes(expected_simplified, actual_simplified):
            feedback = "Congratulations! The reflection was performed correctly."
        else:
            feedback = "Please adjust your drawing to match the blue outline."
        # Display feedback
        self.output_display.config(state=tk.NORMAL)
        self.output_display.insert(tk.END, feedback + "\n", "feedback")
        self.output_display.config(state=tk.DISABLED)
        # Make the "Draw Reflection Question" button visible
        self.draw_random_shape_button.grid()
    
    def clear_drawing(self):
        # Clear the turtle drawing and vertices
        self.turtle.turtle.clear()
        self.turtle.vertices.clear()
        # Reset turtle position and direction
        self.turtle.turtle.penup()
        self.turtle.turtle.goto(0, 0)
        self.turtle.turtle.setheading(0)
        self.turtle.turtle.pendown()
        # Redraw the grid
        self.turtle.draw_grid()

    def draw_random_shape(self):
        self.turtle.turtle.pencolor('orange')
        self.turtle.turtle.width(3) 
        # Define available shapes
        shapes = ['square', 'rectangle']  
        # Randomly choose a shape
        shape = random.choice(shapes)
        # Define grid parameters
        grid_spacing = 50 
        grid_limit = 250  
        # Set maximum offset based on shape
        if shape == 'square':
            max_offset = 50 
        elif shape == 'rectangle':
            max_offset = 100 
        # Randomly generate start coordinates within grid limits
        start_x = random.randint((-grid_limit + max_offset) // grid_spacing, (grid_limit - max_offset) // grid_spacing) * grid_spacing
        start_y = random.randint((-grid_limit + max_offset) // grid_spacing, (grid_limit - max_offset) // grid_spacing) * grid_spacing
        # Clear previous drawing and move to start coordinates
        self.turtle.turtle.clear()
        self.turtle.goto(start_x, start_y)
        # Draw the selected shape
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
        # Put the pen down to start drawing
        self.turtle.turtle.pendown()

    def draw_random_shape_and_question(self):
        # Draw a random shape
        self.draw_random_shape()
        # Define reflection questions
        questions = ["Reflect the shape in the x-axis.", "Reflect the shape in the y-axis."]
        # Select a random question
        selected_question = random.choice(questions)
        # Update the question label with the selected question
        self.question_label.config(text=selected_question)
        # Determine the reflection axis based on the question
        reflection_axis = 'x' if "x-axis" in selected_question else 'y'
        # Calculate the expected vertices after reflection
        self.expected_vertices = self.turtle.calculate_reflected_vertices(reflection_axis)
        # Hide the button to draw a random shape
        self.draw_random_shape_button.grid_remove()

if __name__ == "__main__":
    app = ReflectShapeTab(None)
    app.geometry("800x600")
    app.mainloop()
