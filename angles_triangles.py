import tkinter as tk
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
        if command == "forward" and len(tokens) == 2:
            try:
                distance = float(tokens[1])
                self.move_forward(distance)
            except ValueError:
                return f"Invalid command: {line}"
        elif command == "right" and len(tokens) == 2:
            try:
                angle = float(tokens[1])
                self.turn_right(angle)
            except ValueError:
                return f"Invalid command: {line}"
        elif command == "goto" and len(tokens) == 3:
            try:
                x = float(tokens[1])
                y = float(tokens[2])
                self.goto(x, y)
            except ValueError:
                return f"Invalid command: {line}"
        elif command == "angle" and len(tokens) == 2:
            try:
                angle = float(tokens[1])
                self.set_angle(angle)
            except ValueError:
                return f"Invalid command: {line}"
        else:
            return f"Invalid command: {line}"

    def move_forward(self, distance):
        self.turtle.forward(distance)

    def turn_right(self, angle):
        self.turtle.right(angle)
    
    def set_angle(self, angle):
        self.turtle.setheading(angle)
    
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

    def draw_random_triangle(self):
        # Store current turtle state
        original_state = (self.turtle.pos(), self.turtle.heading())

        # Generate and store the points of the triangle
        points = []
        while len(points) < 3:
            x = random.randint(-200, 200)
            y = random.randint(-200, 200)
            current_point = (x, y)
            if all(self.distance(current_point, p) > 50 for p in points):
                points.append(current_point)
        self.random_triangle_points = points
            
        # Set the pen color to a darker grey
        self.turtle.pencolor('#a9a9a9')  # Darker gray color
        self.turtle.pensize(1)  # Optionally set a thinner pen size if desired
        
        # Draw the triangle and label the vertices
        self.turtle.penup()
        for idx, point in enumerate(points):
            self.turtle.goto(point)
            self.label_vertex(point, f'V{idx+1}')
            if idx == 0:
                self.turtle.pendown()

        # Closing the triangle by going back to the first vertex
        self.turtle.goto(points[0])
        self.turtle.penup()

        # Event generation for triangle completion
        self.output_display.event_generate("<<TriangleDrawn>>")

        # Restore original turtle state
        self.turtle.goto(*original_state[0])
        self.turtle.setheading(original_state[1])
        self.turtle.pendown()  

    def label_vertex(self, point, label):
        offset = 15
        self.turtle.penup()
        self.turtle.goto(point[0]+offset, point[1]-offset)
        self.turtle.write(label, align="left", font=("Arial", 8, "normal"))
        self.turtle.goto(point)
        self.turtle.pendown()

        # Display vertex coordinates next to the label
        coord_text = f"{point}"
        self.turtle.goto(point[0] + 20, point[1])  # Adjust position for the coordinates text
        self.turtle.write(coord_text, align="left", font=("Arial", 8, "normal"))
        self.turtle.goto(point)  # Go back to the vertex

        # Update the output display with the vertex information
        vertex_info = f"{label}: {point}\n"
        self.output_display.config(state=tk.NORMAL)
        self.output_display.insert(tk.END, vertex_info)
        self.output_display.config(state=tk.DISABLED)

    # Method to calculate distance between two points
    def distance(self, point1, point2):
        return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5
    
    def triangles_match(self):
        if set(self.vertices) == set(self.random_triangle_points):
            return True
        return False
    
    def clear_and_draw_new_triangle(self):
        self.turtle.clear()  # Clears everything the turtle has drawn on the canvas
        self.vertices.clear()  # Clears the list of vertices
        self.turtle.penup()  # Lifts the pen so moving the turtle won't draw lines
        self.turtle.goto(0, 0)  # Moves the turtle to the center of the canvas
        self.turtle.setheading(0)  # Resets the turtle's direction to right (east)
        self.turtle.pendown()  # Puts the pen down so the turtle resumes drawing
        self.draw_grid()  # Redraws the grid to ensure it's still visible after clearing
        self.draw_random_triangle()

class AnglesInTriangles(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#ecf0f1")

        self.master.rowconfigure(1, weight=1)  
        self.master.columnconfigure(0, weight=1)  
        self.master.columnconfigure(2, weight=1)  
        self.master.columnconfigure(3, weight=1)

        # Create a frame for the left-hand side elements
        left_frame = tk.Frame(self, bg="white")
        left_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)


        # Information text
        info_text = (
            "Welcome to the Angles in Triangles Tab!\n\n"
            "In this tab, you can explore and learn about various aspects of triangles. "
            "Triangles are fascinating geometric shapes with a wide range of properties and applications. "
            "You can also practice some questions on triangles to test your knowledge and skills. "
            "Explore and learn about different aspects of triangles!"
        )

        # Add a text box to the left panel
        self.left_text_box = tk.Text(left_frame, height=12, width=40, font=("Arial", 13), wrap=tk.WORD)
        self.left_text_box.grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)
        self.left_text_box.insert(tk.END, info_text)
        self.left_text_box.tag_configure("title", font=("Arial", 14, "bold"))
        self.left_text_box.tag_configure("text", font=("Arial", 13))
        self.left_text_box.tag_add("title", "1.0", "1.end")
        self.left_text_box.tag_add("text", "2.0", tk.END)
        self.left_text_box.config(state=tk.DISABLED)

        # Add output display to the left panel
        self.output_display = tk.Text(left_frame, wrap=tk.WORD, state=tk.DISABLED, width=40, height=10)
        self.output_display.grid(row=1, column=0, pady=10, padx=10, sticky=tk.W)

        right_frame = tk.Frame(self, bg="white")  
        right_frame.grid(row=1, column=3, sticky="nsew", padx=20, pady=20) 

        self.clear_drawing_button = tk.Button(right_frame, text="Clear Drawing", command=self.clear_drawing)
        self.clear_drawing_button.grid(row=1, column=0, pady=5, padx=10, sticky=tk.W)

        self.coord_display_label = tk.Label(right_frame, text="Coordinates: (0,0)", font=("Arial", 10), bg="#ecf0f1")
        self.coord_display_label.grid(row=2, column=0, pady=5, padx=10, sticky=tk.W)

        self.turtle_canvas = tk.Canvas(self, width=570, height=570, bg="white")
        self.turtle_canvas.grid(row=1, column=1, rowspan=7, pady=10, padx=10, sticky=tk.W)

        self.turtle = Turtle(self.turtle_canvas, self.output_display)

        self.output_display.tag_config("error", foreground="red")
        self.output_display.tag_config("success", foreground="green")

        self.turtle_canvas.bind("<Motion>", self.update_coordinates)
        self.turtle = Turtle(self.turtle_canvas, self.output_display)
        self.turtle.output_display.bind("<<TriangleDrawn>>", self.generate_missing_angle)

        self.draw_triangle_button = tk.Button(right_frame, text="Draw Random Triangle & Generate Problem", command=self.turtle.draw_random_triangle)
        self.draw_triangle_button.grid(row=3, column=0, pady=5, padx=10, sticky=tk.W)

        # Label to display the angle problem
        self.problem_label = tk.Label(right_frame, text="Click the button to draw a triangle and generate a problem.", wraplength=300, bg="#ecf0f1")
        self.problem_label.grid(row=4, column=0, pady=5, padx=10, sticky=tk.W)

        # Entry and label for user to input the missing angle
        self.answer_entry = tk.Entry(right_frame, width=10)
        self.answer_entry.grid(row=5, column=0, pady=5, padx=10, sticky=tk.W)

        self.submit_answer_button = tk.Button(right_frame, text="Submit Answer", command=self.check_answer)
        self.submit_answer_button.grid(row=6, column=0, pady=5, padx=10, sticky=tk.W)

        self.feedback_label = tk.Label(right_frame, text="", bg="#ecf0f1")
        self.feedback_label.grid(row=7, column=0, pady=5, padx=10, sticky=tk.W)

        self.attempts = 0

    
    def update_coordinates(self, event):
        # Convert canvas coordinates to turtle coordinates
        turtle_x = event.x - 250  # Adjust according to the canvas center
        turtle_y = 250 - event.y  # Invert the y-axis
        self.coord_display_label.config(text=f"Coordinates: ({turtle_x},{turtle_y})")


    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())  # Convert input to integer
            if user_answer == self.missing_angle:
                self.feedback_label.config(text="Correct! Great job!")
            else:
                self.feedback_label.config(text=f"Incorrect. The correct answer is {self.missing_angle}. Try again!")
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number.")
        
    
    def execute_code(self):
        code = self.code_editor.get("1.0", tk.END)
        self.output_display.config(state=tk.NORMAL)
        self.output_display.delete("1.0", tk.END)

        result = self.turtle.execute_code(code)

        if "Invalid command" in result:
            self.output_display.insert(tk.END, result, "error")
        else:
            self.output_display.insert(tk.END, "Code executed successfully.", "success")

            # Check if the triangles match and give feedback
            if self.turtle.triangles_match():
                self.output_display.insert(tk.END, "\nTriangle is correct!", "success")
            else:
                self.output_display.insert(tk.END, "\nTriangle is incorrect. Please try again.", "error")

        self.output_display.config(state=tk.DISABLED)


    
    def clear_drawing(self):
        self.turtle.turtle.clear()  # Clears everything the turtle has drawn on the canvas
        self.turtle.vertices.clear()  # Clears the list of vertices
        self.turtle.turtle.penup()  # Lifts the pen so moving the turtle won't draw lines
        self.turtle.turtle.goto(0, 0)  # Moves the turtle to the center of the canvas
        self.turtle.turtle.setheading(0)  # Resets the turtle's direction to right (east)
        self.turtle.turtle.pendown()  # Puts the pen down so the turtle resumes drawing
        self.turtle.draw_grid()  # Redraws the grid to ensure it's still visible after clearing

    
    def draw_random_triangle(self):
        self.output_display.config(state=tk.NORMAL)
        self.output_display.delete("1.0", tk.END)
        self.turtle.draw_random_triangle()
        self.output_display.config(state=tk.DISABLED)

    def generate_missing_angle(self, event=None):
        self.attempts = 0  # Reset attempts whenever a new problem is generated
        angle1 = random.randint(20, 80)
        angle2 = random.randint(20, 80)
        self.missing_angle = 180 - (angle1 + angle2)
        self.problem_label.config(text=f"The angles of a triangle are {angle1}, {angle2}, and ? degrees. What is the missing angle?")

    def check_answer(self):
        user_answer = self.answer_entry.get()
        if not user_answer.isdigit():
            self.feedback_label.config(text="Please enter a valid number.", fg="red")
            return

        user_answer = int(user_answer)
        if user_answer == self.missing_angle:
            self.feedback_label.config(text="Correct! Great job!", fg="green")
            self.attempts = 0  # Reset attempts after a correct answer
        else:
            self.attempts += 1
            if self.attempts < 2:
                self.feedback_label.config(text="Incorrect. Try again!", fg="red")
            else:
                self.feedback_label.config(text=f"Incorrect. The correct answer is {self.missing_angle}.", fg="red")
                self.attempts = 0  # Reset attempts after showing the correct answer

    
    def reset_and_draw_new_triangle(self):
        # Clear the turtle drawing on the canvas
        self.turtle.turtle.clear()
        self.turtle.vertices.clear()  # Clears the list of vertices
        self.turtle.turtle.penup()  # Lifts the pen so moving the turtle won't draw lines
        self.turtle.turtle.goto(0, 0)  # Moves the turtle to the center of the canvas
        self.turtle.turtle.setheading(0)  # Resets the turtle's direction to right (east)
        self.turtle.turtle.pendown()  # Puts the pen down so the turtle resumes drawing
        self.turtle.draw_grid()  # Redraws the grid to ensure it's still visible after clearing

        # Clear the output display
        self.output_display.config(state=tk.NORMAL)
        self.output_display.delete("1.0", tk.END)
        self.output_display.config(state=tk.DISABLED)

        # Clear the problem and feedback labels, and the answer entry
        self.problem_label.config(text="")
        self.feedback_label.config(text="")
        self.answer_entry.delete(0, tk.END)

        # Generate a new triangle and a corresponding new angle problem
        self.turtle.draw_random_triangle()
    
if __name__ == "__main__":
    app = AnglesInTriangles(None)
    app.geometry("800x600")
    app.mainloop()