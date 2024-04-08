BG_COLOR = 'light grey'
TEXT_COLOR = 'black'
FONT = ('Arial', 10)
FRAME_PADX = 20
FRAME_PADY = 20
LABEL_PADY = 5

import tkinter as tk
from tkinter import ttk
import turtle
import math

class AnglesInTrianglesFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg=BG_COLOR)

        self._update_pending = False

        # Explanation text
        explanation_frame = tk.Frame(self, bg=BG_COLOR, pady=5)
        explanation_frame.pack(side=tk.TOP, pady=20)
        explanation_text = tk.Label(explanation_frame, text="Use the slider to adjust the angle of the triangle.\nNotice how the other angles adjust to maintain a sum of 180°.",
                                    wraplength=500, justify="center", bg=BG_COLOR, font=FONT)
        explanation_text.pack()

        # Turtle canvas
        canvas = tk.Canvas(self, width=400, height=300, bg='white')
        canvas.pack(pady=10)

        self.screen = turtle.TurtleScreen(canvas)
        self.screen.bgcolor("white")

        self.drawer = turtle.RawTurtle(self.screen)
        self.drawer.speed(0)  # Draw at maximum speed

        self.first_angle_label = tk.Label(self, text="", bg=BG_COLOR, font=FONT)
        self.first_angle_label.pack(pady=LABEL_PADY)
        self.second_angle_label = tk.Label(self, text="", bg=BG_COLOR, font=FONT)
        self.second_angle_label.pack(pady=LABEL_PADY)
        self.third_angle_label = tk.Label(self, text="", bg=BG_COLOR, font=FONT)
        self.third_angle_label.pack(pady=LABEL_PADY)

        self.angle_slider = ttk.Scale(self, from_=45, to_=135, orient="horizontal", command=self.update_angle, style='TScale')
        self.angle_slider.pack(pady=20)
        self.angle_slider.set(60)

        self.draw_triangle()
        self.update_angle_labels()
        


    def draw_triangle(self):
        self.screen.tracer(0)
        self.drawer.clear()

        first_angle_degrees = self.angle_slider.get()

        if first_angle_degrees >= 178: 
            first_angle_degrees = 178  
            self.angle_slider.set(first_angle_degrees)

        first_angle_radians = math.radians(first_angle_degrees)

        base_length = 200  
        opposite_side_length = base_length * math.tan(first_angle_radians / 2) / (1 + math.tan(first_angle_radians / 2))

        self.drawer.penup()
        self.drawer.goto(-base_length / 2, 0)
        self.drawer.setheading(0)
        self.drawer.pendown()
        self.drawer.forward(base_length)

        self.drawer.left(180 - first_angle_degrees)
        self.drawer.forward(opposite_side_length)

        self.drawer.goto(-base_length / 2, 0)

        self.drawer.hideturtle()
        self.screen.update()


    def update_angle(self, event=None):
        if self._update_pending:
            return
        self._update_pending = True

        self.after(50, self.perform_update)  
    
    def perform_update(self):
        self._update_pending = False
        self.draw_triangle()
        self.update_angle_labels()
    

    def update_angle_labels(self):

        current_command = self.angle_slider.cget('command')
        self.angle_slider.config(command='')

        first_angle = self.angle_slider.get()

        min_angle = 2  

        third_angle = 60

        max_first_angle = 180 - min_angle - third_angle

        if first_angle > max_first_angle:
            first_angle = max_first_angle
            self.angle_slider.set(first_angle) 

        second_angle = 180 - first_angle - third_angle
        second_angle = max(second_angle, min_angle)

        self.first_angle_label.config(text=f"Angle 1: {first_angle:.2f}°")
        self.second_angle_label.config(text=f"Angle 2: {second_angle:.2f}°")
        self.third_angle_label.config(text=f"Angle 3: {third_angle:.2f}°")

        self.angle_slider.config(command=current_command)

class AnglesAtPointFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.screen, self.drawer = self.setup_canvas()

        # Labels to display the angles
        self.angle_labels = []

        # Instructional text for angles at a point
        self.instruction_label = tk.Label(self, text="Adjust the slider to change how many lines meet at the center point.\n"
                                              "All the angles together will always add up to 360°.")
        self.instruction_label.pack(pady=(10, 0))

        # Slider to adjust the number of lines/angles
        self.angle_count_slider = ttk.Scale(self, from_=3, to_=8, orient="horizontal",
                                            command=self.update_angles, value=5)
        self.angle_count_slider.pack(pady=20)

        # Initial setup for angle labels
        self.setup_angle_labels(5)

        self.draw_angles_at_point(initial=True)

    def setup_canvas(self):
        canvas = tk.Canvas(self, width=200, height=200)  # Same size as before
        canvas.pack()
        screen = turtle.TurtleScreen(canvas)
        screen.bgcolor("white")
        drawer = turtle.RawTurtle(screen)
        drawer.speed(0)
        return screen, drawer

    def draw_angles_at_point(self, initial=False):
        num_lines = int(self.angle_count_slider.get()) if not initial else 5
        angle_size = 360 / num_lines

        self.screen.tracer(0)
        self.drawer.clear()
        self.drawer.penup()
        self.drawer.goto(0, 0)  # Center point

        for _ in range(num_lines):
            self.drawer.down()
            self.drawer.forward(100)
            self.drawer.backward(100)
            self.drawer.left(angle_size)

        self.drawer.hideturtle()
        self.screen.update()

        # Update the labels for angles
        self.update_angle_labels(num_lines, angle_size)

    def setup_angle_labels(self, num_angles):
        for label in self.angle_labels:
            label.destroy()
        self.angle_labels.clear()

        for i in range(num_angles):
            label = tk.Label(self, text=f"Angle {i+1}: {360/num_angles:.2f}°")
            label.pack()
            self.angle_labels.append(label)

    def update_angles(self, event=None):
        num_lines = int(self.angle_count_slider.get())
        angle_size = 360 / num_lines
        self.draw_angles_at_point()
        self.update_angle_labels(num_lines, angle_size)

    def update_angle_labels(self, num_angles, angle_size):
        for i, label in enumerate(self.angle_labels):
            label.config(text=f"Angle {i+1}: {angle_size:.2f}°")
        # Adjust labels in case the number of angles has changed
        difference = num_angles - len(self.angle_labels)
        for i in range(difference):
            self.add_angle_label(i + len(self.angle_labels), angle_size)

    def add_angle_label(self, index, angle_size):
        label = tk.Label(self, text=f"Angle {index+1}: {angle_size:.2f}°")
        label.pack()
        self.angle_labels.append(label)

class AnglesOnLineFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Canvas for drawing the angles
        self.canvas = tk.Canvas(self, width=400, height=200)
        self.canvas.pack()
        
        # Setup the labels before setting the slider value to avoid AttributeError
        self.angle_label_1 = tk.Label(self, text="Angle 1: 90.00°")
        self.angle_label_1.pack()

        self.angle_label_2 = tk.Label(self, text="Angle 2: 90.00°")
        self.angle_label_2.pack()

        # Instructional text
        self.instruction_label = tk.Label(self, text="Move the slider to change the angle.\nThe sum of angles on a straight line is 180°.")
        self.instruction_label.pack(pady=(10, 0))

        # Slider for adjusting the angles
        self.angle_slider = ttk.Scale(self, from_=0, to_=180, orient="horizontal", command=self.update_straight_line_angles)
        self.angle_slider.pack(pady=20)
        self.angle_slider.set(90)  # Start with a right angle


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

        # Draw the line representing the first angle
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
        
        self.canvas_width = 300
        self.canvas_height = 300
        self.line_length = 100
        
        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        # Initialize labels before setting the slider value
        self.angle_label_a = tk.Label(self, text="")
        self.angle_label_a.pack()
        self.angle_label_b = tk.Label(self, text="")
        self.angle_label_b.pack()
        self.angle_label_c = tk.Label(self, text="")
        self.angle_label_c.pack()
        self.angle_label_d = tk.Label(self, text="")
        self.angle_label_d.pack()

        self.instruction_label = tk.Label(self, text="Move the slider to change one pair of vertically opposite angles.")
        self.instruction_label.pack(pady=(10, 0))

        # Create the slider without setting its command yet
        self.angle_slider = ttk.Scale(self, from_=0, to_=180, orient="horizontal")
        self.angle_slider.pack(pady=20)
        
        # Now that labels are initialized, link the command and set the initial value
        self.angle_slider.config(command=self.update_angles)
        self.angle_slider.set(45)  # This now safely triggers update_angles

    
    def update_angles(self, event=None):
        angle = float(self.angle_slider.get())
        opposite_angle = 180 - angle  # Calculate the opposite angle
        # Update labels
        self.angle_label_a.config(text=f"Angle A: {angle:.2f}°")
        self.angle_label_b.config(text=f"Angle B: {opposite_angle:.2f}°")
        self.angle_label_c.config(text=f"Angle C: {angle:.2f}°")
        self.angle_label_d.config(text=f"Angle D: {opposite_angle:.2f}°")
        # Pass opposite_angle to draw_intersecting_lines
        self.draw_intersecting_lines(angle, opposite_angle)


    def draw_intersecting_lines(self, angle, opposite_angle):
        self.canvas.delete("all")  # Clear the canvas
        center_x = self.canvas_width // 2
        center_y = self.canvas_height // 2

        # Draw the lines for angles A and C
        self.canvas.create_line(center_x, center_y,
                                center_x + self.line_length * math.cos(math.radians(angle)),
                                center_y - self.line_length * math.sin(math.radians(angle)))
        self.canvas.create_line(center_x, center_y,
                                center_x - self.line_length * math.cos(math.radians(angle)),
                                center_y + self.line_length * math.sin(math.radians(angle)))

        # Draw the lines for angles B and D using opposite_angle
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

        # Create a canvas and a scrollbar
        canvas = tk.Canvas(self)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Pack the scrollbar to the right and fill in the y-direction
        scrollbar.pack(side="right", fill="y")
        # Pack the canvas to the left and fill in both directions
        canvas.pack(side="left", fill="both", expand=True)

        # Create a frame inside the canvas
        self.scrollable_frame = tk.Frame(canvas)

        # Add the scrollable frame to the canvas
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Update scrollregion in a binding to the scrollable_frame's size
        self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Initialize frames
        self.angles_in_triangles_frame = AnglesInTrianglesFrame(self.scrollable_frame)
        self.angles_at_point_frame = AnglesAtPointFrame(self.scrollable_frame)
        self.angles_on_line_frame = AnglesOnLineFrame(self.scrollable_frame)
        self.vertically_opposite_angles_frame = VerticallyOppositeAnglesFrame(self.scrollable_frame)

        # Pack the frames vertically inside the scrollable frame
        self.angles_in_triangles_frame.pack(fill="x", expand=True)
        self.angles_at_point_frame.pack(fill="x", expand=True)
        self.angles_on_line_frame.pack(fill="x", expand=True)
        self.vertically_opposite_angles_frame.pack(fill="x", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = AnglesGuide(master=root)
    root.geometry("800x600")
    root.mainloop()




