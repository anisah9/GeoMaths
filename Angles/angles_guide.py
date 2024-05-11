# angle_guide.py
import tkinter as tk
from tkinter import ttk
import turtle
import math

BG_COLOR = '#f8f8ff'
TEXT_COLOR = 'black'
LARGE_FONT = ('Arial', 16)  
FONT = ('Arial', 12)  
FRAME_PADX = 20
FRAME_PADY = 20
LABEL_PADY = 5

class AnglesInTrianglesFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        # Initialise the frame
        super().__init__(master, **kwargs)
        self.config(bg=BG_COLOR)    # Set background color

        # Flag to track pending updates
        self._update_pending = False

        # Title text
        title_frame = tk.Frame(self, bg=BG_COLOR, pady=5)
        title_frame.pack(side=tk.TOP, pady=20)
        title_text = tk.Label(title_frame, text="Angles in Triangles Add Up to 180 Degrees",
                              font=LARGE_FONT, bg=BG_COLOR, fg=TEXT_COLOR)
        title_text.pack()

        # Explanation text
        explanation_frame = tk.Frame(self, bg=BG_COLOR, pady=5)
        explanation_frame.pack(side=tk.TOP, pady=10)
        explanation_text = tk.Label(explanation_frame, text="Use the slider to adjust the angle of the triangle.\nNotice how the other angles adjust to maintain a sum of 180°.",
                                    wraplength=600, justify="center", bg=BG_COLOR, font=FONT, fg=TEXT_COLOR)
        explanation_text.pack()

        # Turtle canvas
        canvas = tk.Canvas(self, width=500, height=400, bg='white')  
        canvas.pack(pady=10)

        self.screen = turtle.TurtleScreen(canvas)   # Initialise TurtleScreen with the canvas
        self.screen.bgcolor("white")    # Set background color of the TurtleScreen

        self.drawer = turtle.RawTurtle(self.screen) # Initialise RawTurtle with the screen
        self.drawer.speed(0)  # Draw at maximum speed

        # Labels for displaying angles
        self.first_angle_label = tk.Label(self, text="", bg=BG_COLOR, font=FONT, fg=TEXT_COLOR)
        self.first_angle_label.pack(pady=LABEL_PADY)
        self.second_angle_label = tk.Label(self, text="", bg=BG_COLOR, font=FONT, fg=TEXT_COLOR)
        self.second_angle_label.pack(pady=LABEL_PADY)
        self.third_angle_label = tk.Label(self, text="", bg=BG_COLOR, font=FONT, fg=TEXT_COLOR)
        self.third_angle_label.pack(pady=LABEL_PADY)

        # Angle slider
        self.angle_slider = ttk.Scale(self, from_=45, to_=135, orient="horizontal", command=self.update_angle, style='TScale')
        self.angle_slider.pack(pady=20)
        self.angle_slider.set(60)   # Set default angle

        self.draw_triangle()    # Draw the initial triangle
        self.update_angle_labels()  # Update angle labels

    def draw_triangle(self):
        # Turn off animation to draw the triangle instantly
        self.screen.tracer(0)
        # Clear any existing drawings
        self.drawer.clear()

        # Get the value of the first angle from the slider
        first_angle_degrees = self.angle_slider.get()
        # Ensures the first angle does not exceed a certain limit
        if first_angle_degrees >= 178:
            first_angle_degrees = 178
            self.angle_slider.set(first_angle_degrees)

        # Convert the first angle from degrees to radians
        first_angle_radians = math.radians(first_angle_degrees)
        base_length = 300   # Length of the base of the triangle
        # Calculate the length of the opposite side using trigonometry
        opposite_side_length = base_length * math.tan(first_angle_radians / 2) / (1 + math.tan(first_angle_radians / 2))

        # Move the turtle to the starting position
        self.drawer.penup()
        self.drawer.goto(-base_length / 2, 0)
        self.drawer.setheading(0)
        self.drawer.pendown()
        # Draw the base of the triangle
        self.drawer.forward(base_length)
        # Rotate and draw the second side of the triangle
        self.drawer.left(180 - first_angle_degrees)
        self.drawer.forward(opposite_side_length)
        # Return to the starting position
        self.drawer.goto(-base_length / 2, 0)
        # Hide the turtle and update the screen
        self.drawer.hideturtle()
        self.screen.update()

    def update_angle(self, event=None):
        # Prevent multiple updates from being triggered simultaneously
        if self._update_pending:
            return
        self._update_pending = True
        # Schedule the update after a short delay
        self.after(50, self.perform_update)

    def perform_update(self):
        # Mark the update as complete
        self._update_pending = False
         # Redraw the triangle
        self.draw_triangle()
        # Update the angle labels
        self.update_angle_labels()

    def update_angle_labels(self):
        # Temporarily disable the command associated with the slider
        current_command = self.angle_slider.cget('command')
        self.angle_slider.config(command='')

        # Get the current value of the first angle from the slider
        first_angle = self.angle_slider.get()
        min_angle = 2
        third_angle = 60
        # Calculate the maximum allowed value for the first angle
        max_first_angle = 180 - min_angle - third_angle
        if first_angle > max_first_angle:
            first_angle = max_first_angle
            self.angle_slider.set(first_angle)

        # Calculate the second angle and ensure it does not fall below a certain limit
        second_angle = 180 - first_angle - third_angle
        second_angle = max(second_angle, min_angle)

        # Update the angle labels with formatted angles
        self.first_angle_label.config(text=f"Angle 1: {first_angle:.2f}°")
        self.second_angle_label.config(text=f"Angle 2: {second_angle:.2f}°")
        self.third_angle_label.config(text=f"Angle 3: {third_angle:.2f}°")
        # Restore the original command associated with the slider
        self.angle_slider.config(command=current_command)


class AnglesAtPointFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        # Initialise the frame
        super().__init__(master, **kwargs)
        self.config(bg=BG_COLOR)

        # Set up the canvas for drawing
        self.screen, self.drawer = self.setup_canvas()

        # List to store angle label widgets
        self.angle_labels = []  

        # Title for the frame
        self.title_label = tk.Label(self, text="Angles at a Point",
                                    font=LARGE_FONT, bg=BG_COLOR, fg=TEXT_COLOR)
        self.title_label.pack(pady=(10, 0), padx=20)   # Adjust padding for title label

        # Instruction label
        self.instruction_label = tk.Label(self, text="Adjust the slider to change how many lines meet at the center point.\n"
                                                     "All the angles together will always add up to 360°.",
                                          bg=BG_COLOR, font=FONT, fg=TEXT_COLOR)
        self.instruction_label.pack(pady=(10, 20)) # Adjust padding for instruction label

        # Slider to control the number of lines meeting at the center point
        self.angle_count_slider = ttk.Scale(self, from_=3, to_=8, orient="horizontal",
                                            command=self.update_angles, value=5)
        self.angle_count_slider.pack(pady=20)

        # Set up angle labels with initial value
        self.setup_angle_labels(5)
        # Draw the angles at the point initially
        self.draw_angles_at_point(initial=True)

    def setup_canvas(self):
        # Create a canvas for drawing angles
        canvas = tk.Canvas(self, width=300, height=300, bg='white')  
        canvas.pack()   # Pack the canvas into the frame
        screen = turtle.TurtleScreen(canvas)    # Create a turtle screen associated with the canvas
        screen.bgcolor("white") # Set background color for the turtle screen
        drawer = turtle.RawTurtle(screen)   # Create a raw turtle for drawing
        drawer.speed(0) # Set the drawing speed to maximum
        return screen, drawer   # Return the turtle screen and drawer

    def draw_angles_at_point(self, initial=False):
        # Get the number of lines to draw angles
        num_lines = int(self.angle_count_slider.get()) if not initial else 5
        angle_size = 360 / num_lines    # Calculate the angle size for each line

        self.screen.tracer(0)   # Turn off animation
        self.drawer.clear() # Clear any existing drawings
        self.drawer.penup() # Lift the pen
        self.drawer.goto(0, 0)  # Center point

        # Draw angles at the center point
        for _ in range(num_lines):
            self.drawer.down()
            self.drawer.forward(100)
            self.drawer.backward(100)
            self.drawer.left(angle_size)

        self.drawer.hideturtle()
        self.screen.update()

        # Update angle labels
        self.update_angle_labels(num_lines, angle_size)

    def setup_angle_labels(self, num_angles):
        # Clear existing angle labels
        for label in self.angle_labels:
            label.destroy()
        self.angle_labels.clear()

        # Create and pack new angle labels
        for i in range(num_angles):
            label = tk.Label(self, text=f"Angle {i+1}: {360/num_angles:.2f}°", bg=BG_COLOR, font=FONT, fg=TEXT_COLOR)
            label.pack()    # Pack the label into the frame
            self.angle_labels.append(label) # Add the label to the list

    def update_angles(self, event=None):
        # Get the number of lines from the slider
        num_lines = int(self.angle_count_slider.get())
        angle_size = 360 / num_lines    # Calculate the angle size for each line
        self.draw_angles_at_point() # Redraw angles at the point
        self.update_angle_labels(num_lines, angle_size)  # Update angle labels

    def update_angle_labels(self, num_angles, angle_size):
        # Clear existing angle labels
        for label in self.angle_labels:
            label.destroy()
        self.angle_labels.clear()

        # Create and pack new angle labels
        for i in range(num_angles):
            label = tk.Label(self, text=f"Angle {i+1}: {angle_size:.2f}°", bg=BG_COLOR, font=FONT, fg=TEXT_COLOR)
            label.pack()    # Pack the label into the frame
            self.angle_labels.append(label) # Add the label to the list


class AnglesOnLineFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg=BG_COLOR) 

        # Title label
        title_label = tk.Label(self, text="Angles on a Line", font=('Arial', 16), bg='light gray', fg='black')
        title_label.pack(pady=(10, 5))

        # Canvas for drawing
        self.canvas = tk.Canvas(self, width=400, height=200, bg='white')
        self.canvas.pack(pady=(10, 10))

        # Angle labels 
        self.angle_label_1 = tk.Label(self, text="Angle 1: 90.00°", font=('Arial', 12), bg='light gray')
        self.angle_label_1.pack()   # Pack the first angle label

        self.angle_label_2 = tk.Label(self, text="Angle 2: 90.00°", font=('Arial', 12), bg='light gray')
        self.angle_label_2.pack()   # Pack the second angle label

        # Instruction label
        self.instruction_label = tk.Label(self, text="Move the slider to change the angle.\nThe sum of angles on a straight line is 180°.",
                                          font=('Arial', 12), bg='light gray', pady=10)
        self.instruction_label.pack(pady=(5, 10))  # Pack the instruction label with padding 

        # Slider for adjusting the angles
        self.angle_slider = ttk.Scale(self, from_=0, to_=180, orient="horizontal",
                                      command=self.update_straight_line_angles)
        self.angle_slider.pack(pady=10) # Pack the slider with padding
        self.angle_slider.set(90)  # Set initial value for the slider

        # Initial drawing
        self.draw_straight_line_angles()

    def draw_straight_line_angles(self):
        # Clear the canvas
        self.canvas.delete("all")

        # Get the current angle from the slider
        angle = self.angle_slider.get()

        # Calculate the position of the second point based on the angle
        x2 = 200 + 180 * math.cos(math.radians(angle))
        y2 = 100 - 180 * math.sin(math.radians(angle))

        # Draw the straight line (baseline)
        self.canvas.create_line(20, 100, 380, 100, arrow=tk.LAST)

        self.canvas.create_line(200, 100, x2, y2, arrow=tk.LAST)

    def update_straight_line_angles(self, event=None):
        # Get the current angle from the slider
        angle = self.angle_slider.get()

        # Calculate the complementary angle
        complementary_angle = 180 - angle

        # Update the angle labels
        self.angle_label_1.config(text=f"Angle 1: {angle:.2f}°")
        self.angle_label_2.config(text=f"Angle 2: {complementary_angle:.2f}°")

        # Redraw the angles
        self.draw_straight_line_angles()


class VerticallyOppositeAnglesFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg=BG_COLOR) 

        # Title label
        title_label = tk.Label(self, text="Vertically Opposite Angles", font=('Arial', 16), bg='light gray')
        title_label.pack(pady=(10, 5))

        # Canvas dimensions and line length
        self.canvas_width = 400
        self.canvas_height = 400
        self.line_length = 150  
        
        # Canvas for drawing
        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack(pady=(10, 10))

        # Angle labels
        self.angle_label_a = tk.Label(self, text="", font=('Arial', 12), bg='light gray')
        self.angle_label_a.pack()   # Pack angle label a
        self.angle_label_b = tk.Label(self, text="", font=('Arial', 12), bg='light gray')
        self.angle_label_b.pack()   # Pack angle label b
        self.angle_label_c = tk.Label(self, text="", font=('Arial', 12), bg='light gray')
        self.angle_label_c.pack()   # Pack angle label c
        self.angle_label_d = tk.Label(self, text="", font=('Arial', 12), bg='light gray')
        self.angle_label_d.pack()   # Pack angle label d

        # Instruction label
        self.instruction_label = tk.Label(self, text="Move the slider to change one pair of vertically opposite angles.",
                                          font=('Arial', 12), bg='light gray')
        self.instruction_label.pack(pady=(10, 20))  # Pack the instruction label with padding

        # Slider for adjusting the angles
        self.angle_slider = ttk.Scale(self, from_=0, to_=180, orient="horizontal", command=self.update_angles)
        self.angle_slider.pack(pady=20)  # Pack the slider with padding
        self.angle_slider.set(45)   # Set initial value for the slider

    def update_angles(self, event=None):
        # Get the current angle from the slider
        angle = float(self.angle_slider.get())
        # Calculate the opposite angle
        opposite_angle = 180 - angle  

        # Update angle labels with the current and opposite angles
        self.angle_label_a.config(text=f"Angle A: {angle:.2f}°")
        self.angle_label_b.config(text=f"Angle B: {opposite_angle:.2f}°")
        self.angle_label_c.config(text=f"Angle C: {angle:.2f}°")
        self.angle_label_d.config(text=f"Angle D: {opposite_angle:.2f}°")

        # Draw intersecting lines based on the current and opposite angles
        self.draw_intersecting_lines(angle, opposite_angle)

    def draw_intersecting_lines(self, angle, opposite_angle):
        # Clear the canvas
        self.canvas.delete("all")  
        # Calculate the center coordinates of the canvas
        center_x = self.canvas_width // 2
        center_y = self.canvas_height // 2

        # Draw two lines intersecting at the center, each at the specified angle and its opposite
        self.canvas.create_line(center_x, center_y,
                                center_x + self.line_length * math.cos(math.radians(angle)),
                                center_y - self.line_length * math.sin(math.radians(angle)))
        self.canvas.create_line(center_x, center_y,
                                center_x - self.line_length * math.cos(math.radians(angle)),
                                center_y + self.line_length * math.sin(math.radians(angle)))

        self.canvas.create_line(center_x, center_y,
                                center_x + self.line_length * math.cos(math.radians(opposite_angle)),
                                center_y - self.line_length * math.sin(math.radians(opposite_angle)))
        self.canvas.create_line(center_x, center_y,
                                center_x - self.line_length * math.cos(math.radians(opposite_angle)),
                                center_y + self.line_length * math.sin(math.radians(opposite_angle)))

class AnglesGuide(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill="both", expand=True)
        
        # Initialise frames list and current frame index
        self.frames = []
        self.current_frame_index = 0

        # Instantiate frames for different angle topics
        self.angles_in_triangles_frame = AnglesInTrianglesFrame(self)
        self.angles_at_point_frame = AnglesAtPointFrame(self)
        self.angles_on_line_frame = AnglesOnLineFrame(self)
        self.vertically_opposite_angles_frame = VerticallyOppositeAnglesFrame(self)

        # Add frames to the frames list
        self.frames.extend([
            self.angles_in_triangles_frame,
            self.angles_at_point_frame,
            self.angles_on_line_frame,
            self.vertically_opposite_angles_frame
        ])

        # Show the initial frame
        self.show_frame(0)  

        # Buttons for navigation
        btn_prev = tk.Button(self, text="Previous", command=self.prev_frame)
        btn_prev.pack(side=tk.LEFT, padx=10, pady=10)

        btn_next = tk.Button(self, text="Next", command=self.next_frame)
        btn_next.pack(side=tk.RIGHT, padx=10, pady=10)

    def show_frame(self, index):
        """Show a frame for the given index."""
        frame = self.frames[index]
        frame.pack(fill="both", expand=True)
        if self.current_frame_index != index:
            self.frames[self.current_frame_index].pack_forget()
        self.current_frame_index = index

    def next_frame(self):
        """Show the next frame in the list."""
        next_index = (self.current_frame_index + 1) % len(self.frames)
        self.show_frame(next_index)

    def prev_frame(self):
        """Show the previous frame in the list."""
        prev_index = (self.current_frame_index - 1) % len(self.frames)
        self.show_frame(prev_index)

if __name__ == "__main__":
    root = tk.Tk()
    app = AnglesGuide(master=root)
    root.geometry("800x600")
    root.mainloop()



