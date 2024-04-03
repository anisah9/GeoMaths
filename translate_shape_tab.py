import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import turtle
import random
import math


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


        self.shape_details = {}
        self.reset_position_orientation()  
    
    def reset_position_orientation(self):
        self.current_position = (0, 0)  
        self.current_angle = 0  

    def update_position_based_on_command(self, distance):
        
        radians = math.radians(self.current_angle)
        delta_x = distance * math.cos(radians)
        delta_y = distance * math.sin(radians)
        self.current_position = (
            self.current_position[0] + delta_x,
            self.current_position[1] + delta_y
        )

    def execute_code(self, code):
        self.reset_position_orientation()  # Reset position and orientation at start
        self.movement_history = []  # Track each forward movement distance
        self.output_display.delete("1.0", tk.END)  # Clear previous messages

        error_encountered = False
        lines = code.split('\n')
        for line in lines:
            valid_command, message = self.execute_line(line.strip())
            if not valid_command:
                self.output_display.config(state=tk.NORMAL)
                self.output_display.insert(tk.END, message + "\n", "error")
                error_encountered = True
                break  # Stop executing further lines
        
        if not error_encountered:
            # Update the actual final position after all commands have been executed
            self.shape_details['actual_final_pos'] = self.current_position
            
            self.calculate_dimensions()


    def execute_line(self, line):
        tokens = line.split()
        if not tokens:
            return True, ""  # Ignore empty lines without error

        command, *args = tokens
        if command == "forward" and len(args) == 1:
            self.move_forward(float(args[0]))
        elif command == "right" and len(args) == 1:
            self.turn_right(float(args[0]))
        elif command == "goto" and len(args) == 2:
            self.goto(float(args[0]), float(args[1]))
        else:
            return False, f"Invalid command: {line}"  # Return False to indicate error

        return True, ""  # Return True for valid commands
    
    def calculate_dimensions(self):
        if len(self.movement_history) == 4: 

            length = self.movement_history[0]
            width = self.movement_history[1]
            if length == width:  # Square
                self.shape_details['user_dimensions'] = (length,)
            else:  # Rectangle
                self.shape_details['user_dimensions'] = (length, width)
        elif len(self.movement_history) == 3: 
            side = self.movement_history[0]
            self.shape_details['user_dimensions'] = (side,)

    def move_forward(self, distance):
        angle_rad = math.radians(self.current_angle)
        dx = distance * math.cos(angle_rad)
        dy = distance * math.sin(angle_rad)
        new_x = self.current_position[0] + dx
        new_y = self.current_position[1] + dy
        self.current_position = (new_x, new_y)
        self.drawing_turtle.forward(distance)
        self.movement_history.append(distance)

    def turn_right(self, angle):
        self.current_angle = (self.current_angle + angle) % 360
        self.drawing_turtle.right(angle)
    
    def goto(self, x, y):
        self.current_position = (x, y)
        self.drawing_turtle.penup()
        self.drawing_turtle.goto(x, y)
        self.drawing_turtle.pendown()

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

    
    def draw_random_shape(self):
        shape = random.choice(['square', 'triangle', 'rectangle'])
        grid_size = 50  # Grid spacing
        
        if shape in ['square', 'triangle']:
            max_side = min(250, 250) // 2
            side = random.randint(1, max_side // grid_size) * grid_size
            if shape == 'square':
                dimensions = (side,)
            else:  # triangle
                dimensions = (side,)
        else:  # rectangle
            max_length = min(250, 250) // 2
            max_width = min(250, 250) // 4
            length = random.randint(1, max_length // grid_size) * grid_size
            width = random.randint(1, max_width // grid_size) * grid_size
            dimensions = (length, width)

        x = random.randint(-250 + max(dimensions), 250 - max(dimensions)) // grid_size * grid_size
        y = random.randint(-250 + max(dimensions), 250 - max(dimensions)) // grid_size * grid_size

        self.drawing_turtle.penup()
        self.drawing_turtle.goto(x, y)
        self.drawing_turtle.pendown()

        print(f"Starting to draw {shape} at position ({x}, {y})")

        if shape == 'square' or shape == 'triangle':
            for _ in range(4) if shape == 'square' else range(3):
                self.drawing_turtle.forward(side)
                self.drawing_turtle.right(90 if shape == 'square' else 120)
        else:  # rectangle
            for _ in range(2):
                self.drawing_turtle.forward(length)
                self.drawing_turtle.right(90)
                self.drawing_turtle.forward(width)
                self.drawing_turtle.right(90)

        self.shape_details = {
            'shape': shape,
            'start_pos': (x, y),
            'dimensions': dimensions
        }

        print(f"Drew a {shape} with dimensions {dimensions} starting at position ({x}, {y})")


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

        self.draw_random_shape_button = tk.Button(self, text="Draw Random Shape", command=self.draw_random_shape_and_question)
        self.draw_random_shape_button.grid(row=8, column=1, pady=5, padx=10, sticky=tk.W)

        self.question_label = tk.Label(self, text="", font=("Arial", 13), bg="#ecf0f1")
        self.question_label.grid(row=8, column=1, pady=10, padx=10, sticky=tk.W)


    def execute_code(self):
        code = self.code_editor.get("1.0", tk.END)
        self.turtle.execute_code(code)
        self.check_final_position()
    
    def check_final_position(self):
        actual_final_pos = self.turtle.shape_details.get('actual_final_pos')
        expected_final_pos = self.turtle.shape_details.get('expected_final_pos')
        tolerance = 10  

        if actual_final_pos and expected_final_pos:
            distance = math.sqrt((actual_final_pos[0] - expected_final_pos[0]) ** 2 + (actual_final_pos[1] - expected_final_pos[1]) ** 2)
            if distance <= tolerance:
                self.output_display.config(state=tk.NORMAL)
                self.output_display.insert(tk.END, "Position check passed: Shape is in the correct position.\n", "success")
            else:
                self.output_display.config(state=tk.NORMAL)
                self.output_display.insert(tk.END, "Position check failed: Shape is not in the correct position.\n", "error")
        else:
            self.output_display.config(state=tk.NORMAL)
            self.output_display.insert(tk.END, "Position check failed: Position data is missing.\n", "error")
        
    
        self.check_shape_dimensions()
        self.output_display.config(state=tk.DISABLED)

    def check_shape_dimensions(self):
        user_dimensions = self.turtle.shape_details.get('user_dimensions', ())
        expected_dimensions = self.turtle.shape_details.get('dimensions', ())
        if user_dimensions == expected_dimensions:
            self.output_display.config(state=tk.NORMAL)
            self.output_display.insert(tk.END, "Dimension check passed: Shape dimensions are correct.\n", "success")
            self.ask_for_new_question()  # Add this line
        else:
            self.output_display.config(state=tk.NORMAL)
            self.output_display.insert(tk.END, "Dimension check failed: Shape dimensions are not correct.\n", "error")
        self.output_display.config(state=tk.DISABLED)
    
    def ask_for_new_question(self):
        answer = messagebox.askyesno("Question Correct", "Would you like another question?")
        if answer:
            self.clear_drawing()
            self.draw_random_shape_and_question()



    def clear_drawing(self):
        self.turtle.drawing_turtle.clear()
    
    def draw_random_shape_and_question(self):
        self.turtle.draw_random_shape()
        self.display_question()

    def generate_translation_question(self):
        directions = ["right", "left", "up", "down"]
        distance = random.randint(1, 5)  # Random distance between 1 and 5 units
        direction = random.choice(directions)
        translation_distance = distance * 50  # Convert grid units to pixels

        # Calculate translation vector based on direction
        dx = translation_distance if direction == "right" else -translation_distance if direction == "left" else 0
        dy = translation_distance if direction == "up" else -translation_distance if direction == "down" else 0

        initial_pos = self.turtle.shape_details['start_pos']
        expected_final_pos = (initial_pos[0] + dx, initial_pos[1] + dy)

        # Update shape details with expected final position
        self.turtle.shape_details['expected_final_pos'] = expected_final_pos

        question = f"Translate the shape {distance} units {direction}."
        return question

    def display_question(self):
        question = self.generate_translation_question()
        self.question_label.config(text=question)
    
    def is_correct_position(self, final_pos, expected_pos, tolerance=10):
        dist = math.sqrt((final_pos[0] - expected_pos[0])**2 + (final_pos[1] - expected_pos[1])**2)
        return dist <= tolerance
    


if __name__ == "__main__":
    app = TranslateShapeTab(None)
    app.geometry("800x600")
    app.mainloop()