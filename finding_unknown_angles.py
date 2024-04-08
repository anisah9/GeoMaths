import tkinter as tk
from tkinter import ttk
import turtle
import math

class AngleGuidesFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._update_pending = False

        # Explanation text
        explanation_frame = tk.Frame(self)
        explanation_frame.pack(side=tk.TOP, pady=20)
        explanation_text = tk.Label(explanation_frame, text="Use the slider to adjust the angle of the triangle.\nNotice how the other angles adjust to maintain a sum of 180°.",
                                    wraplength=500, justify="center")
        explanation_text.pack()

        # Turtle canvas
        canvas = tk.Canvas(self, width=400, height=300)
        canvas.pack()

        self.screen = turtle.TurtleScreen(canvas)
        self.screen.bgcolor("white")

        self.drawer = turtle.RawTurtle(self.screen)
        self.drawer.speed(0)  # Draw at maximum speed


        self.first_angle_label = tk.Label(self, text="")
        self.first_angle_label.pack()  
        self.second_angle_label = tk.Label(self, text="")
        self.second_angle_label.pack()  
        self.third_angle_label = tk.Label(self, text="")
        self.third_angle_label.pack() 

        # Slider for adjusting angle
        self.angle_slider = ttk.Scale(self, from_=45, to_=135, orient="horizontal", command=self.update_angle)
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



class FindingUnknownAngles(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # Button to show angle guides
        self.show_button = tk.Button(self, text="Show Angle Guides", command=self.toggle_angle_guides)
        self.show_button.pack(pady=20)

        self.angle_guides_frame = None

    def toggle_angle_guides(self):
        if self.angle_guides_frame is None:
            self.angle_guides_frame = AngleGuidesFrame(self)
            self.angle_guides_frame.pack(fill="both", expand=True)
            self.show_button.config(text="Hide Angle Guides")
        else:
            self.angle_guides_frame.pack_forget()
            self.angle_guides_frame = None
            self.show_button.config(text="Show Angle Guides")

if __name__ == "__main__":
    root = tk.Tk()
    app = FindingUnknownAngles(master=root)
    app.pack(fill="both", expand=True)
    root.geometry("800x600")
    root.mainloop()




