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
            return True, ""  

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
        shape = random.choice(['square', 'rectangle'])
        grid_size = 50  # Grid spacing
        
        if shape == 'square':
            max_side = min(250, 250) // 2
            side = random.randint(1, max_side // grid_size) * grid_size
            dimensions = (side,)
        else:  # rectangle
            max_length = min(250, 250) // 2
            max_width = min(250, 250) // 4
            length = random.randint(1, max_length // grid_size) * grid_size
            width = random.randint(1, max_width // grid_size) * grid_size
            dimensions = (length, width)

        x = random.randint(-250 + max(dimensions), 250 - max(dimensions)) // grid_size * grid_size
        y = random.randint(-250 + max(dimensions), 250 - max(dimensions)) // grid_size * grid_size

        initial_position = (x, y)  

        self.drawing_turtle.penup()
        self.drawing_turtle.goto(x, y)
        self.drawing_turtle.pendown()

        # Set color and thickness
        self.drawing_turtle.pencolor('purple')
        self.drawing_turtle.pensize(3)

        if shape == 'square':
            for _ in range(4):
                self.drawing_turtle.forward(side)
                self.drawing_turtle.right(90)
        else:  # rectangle
            for _ in range(2):
                self.drawing_turtle.forward(length)
                self.drawing_turtle.right(90)
                self.drawing_turtle.forward(width)
                self.drawing_turtle.right(90)

        self.shape_details = {
            'shape': shape,
            'start_pos': initial_position,  # Store the initial position
            'dimensions': dimensions
        }

        # Reset the color and thickness of the turtle to default values
        self.drawing_turtle.pencolor("blue")
        self.drawing_turtle.pensize(2)

class TranslateShapeTab(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#ecf0f1")
        self.winfo_toplevel().title("Geometry Tool")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)  
        self.grid_columnconfigure(1, weight=3)  
        self.grid_columnconfigure(2, weight=1)  
        self.grid_columnconfigure(3, weight=2, minsize=300) 

        # Create a frame for the left-hand side elements
        left_frame = tk.Frame(self, bg="white")
        left_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

        # Create a frame for the right-hand side elements with specified color
        right_frame = tk.Frame(self, bg="white")  
        right_frame.grid(row=1, column=3, sticky="nsew", padx=20, pady=20) 

        self.info_text = tk.Text(left_frame, height=12, width=40, font=("Arial", 14), wrap=tk.WORD)
        self.info_text.grid(row=1, column=1, pady=10, padx=10, sticky=tk.W)

        self.info_text.tag_configure('title', font=('Arial', 16, 'bold'))

        title = "Welcome to the Translate Shapes tab!\n\n"
        self.info_text.insert(tk.END, title, 'title')
        intro_text = ("A space to help learn shape translation through coding! "
                      "Embark on a hands-on journey where you can practice shifting shapes "
                      "across the canvas with coding commands. Delight in discovering how coding "
                      "can alter geometric configurations and help aid your understanding of "
                      "coordinate systems."
                      "To get started press the Draw Translation Question button and then follow the " 
                      "instructions in the box below!\n\n")  
        self.info_text.insert(tk.END, intro_text)
        self.info_text.config(state=tk.DISABLED)

        # Setup label for the code editor
        editor_info_label = tk.Label(left_frame, text="Enter your drawing instructions below:", font=("Arial", 13), bg="#ecf0f1")
        editor_info_label.grid(row=2, column=1, pady=10, padx=10, sticky=tk.W)

        # Code editor
        self.code_editor = scrolledtext.ScrolledText(left_frame, wrap=tk.WORD, width=50, height=15)
        self.code_editor.grid(row=3, column=1, pady=10, padx=10, sticky=tk.W)

        # Execute button
        self.execute_button = tk.Button(left_frame, text="Run Code", command=self.execute_code)
        self.execute_button.grid(row=4, column=1, pady=5, padx=10, sticky=tk.W)

        # Output display
        self.output_display = tk.Text(left_frame, wrap=tk.WORD, state=tk.DISABLED, width=50, height=10)
        self.output_display.grid(row=5, column=1, pady=10, padx=10, sticky=tk.W)

        self.turtle_canvas = tk.Canvas(self, width=570, height=570, bg="white")
        self.turtle_canvas.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.turtle = Turtle(self.turtle_canvas, self.output_display)

        self.output_display.tag_config("error", foreground="red")
        self.output_display.tag_config("success", foreground="green")
        
        # Add a text box at the top of the right panel
        self.info_text_box = tk.Text(right_frame, height=30, width=35, font=("Arial", 12), wrap=tk.WORD)
        self.info_text_box.grid(row=0, column=0, pady=5, padx=10, sticky=tk.W + tk.E + tk.N + tk.S)

        # Define text styles with tags
        self.info_text_box.tag_configure('title', font=('Arial', 16, 'bold'))
        self.info_text_box.tag_configure('description', font=('Arial', 14))

        # Set the text with a title and explanation
        title = "Translation\n\n"
        description = ("Imagine you have a sticker on a piece of paper. Now, suppose you want to move that sticker to another spot on the paper without rotating it or flipping it over. You just slide it straight over to where you want it. That sliding movement is what we call translation in geometry.\n\n"
                       "When you translate something, you're moving it up, down, left, or right, or even diagonally, but it always keeps facing the same way and doesn't get any bigger or smaller. It’s like when you slide a toy car across the floor: it moves to a new place, but it’s still the same car, facing the same direction.\n\n"
                       "So, in geometry, when we translate a shape, we are moving every point of the shape the same distance in the same direction. It’s like every point in the shape has taken the same little journey to a new location!\n\n")

        # Insert text with tags to apply styles
        self.info_text_box.insert(tk.END, title, 'title')
        self.info_text_box.insert(tk.END, description, 'description')
        self.info_text_box.config(state=tk.DISABLED)

        # Add a button below the text box in the right panel
        self.draw_random_shape_button = tk.Button(right_frame, text="Draw Translation Question", command=self.draw_random_shape_and_question)
        self.draw_random_shape_button.grid(row=1, column=0, pady=5, padx=10, sticky=tk.W)

        # Add a label below the button in the right panel
        self.question_label = tk.Label(right_frame, text="", font=("Arial", 13), bg="#ecf0f1")
        self.question_label.grid(row=2, column=0, pady=10, padx=10, sticky=tk.W)

        # Add another text box below the label for specific instructions
        self.instructions_text_box = tk.Text(right_frame, height=14, width=35, font=("Arial", 12), wrap=tk.WORD)
        self.instructions_text_box.grid(row=3, column=0, pady=5, padx=10, sticky=tk.W + tk.E + tk.N + tk.S)
        
        detailed_instructions = (
        "Instructions:\n"
        "1. Observe the randomly drawn shape on the canvas.\n"
        "2. Use the tools provided to translate the shape according to the displayed direction.\n"
        "3. Draw the shape using the command editor.\n"
        "4. Press the 'Run Code' button to apply the translation.\n"
        "5. The display box will tell you if your translation was successful or not.\n"
        "6. Ensure the shape remains oriented as it started and maintains its original size.\n"
        "Good luck with your translation exercise!"
    )

        self.instructions_text_box.insert(tk.END, detailed_instructions)
        self.instructions_text_box.config(state=tk.DISABLED)



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

        initial_pos = self.turtle.shape_details['start_pos']
        max_x = 250 - translation_distance if direction == "right" else -250 + translation_distance if direction == "left" else 250
        max_y = 250 - translation_distance if direction == "up" else -250 + translation_distance if direction == "down" else 250

        # Check if translation will result in going beyond canvas boundaries
        if direction in ["right", "left"]:
            if initial_pos[0] + translation_distance > max_x or initial_pos[0] - translation_distance < -250:
                return self.generate_translation_question()  # Generate a new question
        elif direction in ["up", "down"]:
            if initial_pos[1] + translation_distance > max_y or initial_pos[1] - translation_distance < -250:
                return self.generate_translation_question()  # Generate a new question

        dx = translation_distance if direction == "right" else -translation_distance if direction == "left" else 0
        dy = translation_distance if direction == "up" else -translation_distance if direction == "down" else 0

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
