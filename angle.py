# import tkinter as tk
# from turtle import RawTurtle, Canvas
# from tkinter import messagebox

# class AngleTool(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master, bg="#ecf0f1")
#         self.winfo_toplevel().title("Angle Tool")

#         # Create a canvas for drawing
#         self.canvas = Canvas(self, width=500, height=500, bg="white")
#         self.canvas.pack(pady=10)

#         # Create a Turtle for drawing on the canvas
#         self.turtle = RawTurtle(self.canvas)
#         self.turtle.speed(1)

#         # Add a label for instructions
#         instructions_label = tk.Label(self, text="Instructions:\nClick on buttons to draw and manipulate triangles.", font=("Arial", 13), bg="#ecf0f1")
#         instructions_label.pack(pady=10)

#         # Add buttons for triangle activities
#         self.draw_triangle_button = tk.Button(self, text="Draw Triangle", command=self.draw_triangle)
#         self.draw_triangle_button.pack(pady=10)

#         self.meet_at_a_point_button = tk.Button(self, text="Meet at a Point", command=self.meet_at_a_point)
#         self.meet_at_a_point_button.pack(pady=5)

#         self.on_a_straight_line_button = tk.Button(self, text="On a Straight Line", command=self.on_a_straight_line)
#         self.on_a_straight_line_button.pack(pady=5)

#         self.vertically_opposite_button = tk.Button(self, text="Vertically Opposite", command=self.vertically_opposite)
#         self.vertically_opposite_button.pack(pady=5)

#     def draw_triangle(self):
#         # Draw a simple triangle
#         self.turtle.clear()
#         self.turtle.penup()
#         self.turtle.goto(-50, -50)
#         self.turtle.pendown()
#         for _ in range(3):
#             self.turtle.forward(100)
#             self.turtle.left(120)

#         messagebox.showinfo("Draw Triangle", "You've drawn a triangle! A triangle is a polygon with three edges and three vertices.")

#     def meet_at_a_point(self):
#         # Clear the canvas
#         self.turtle.clear()

#         # Draw lines extending from the point
#         for _ in range(3):
#             self.turtle.penup()
#             self.turtle.goto(0, 0)
#             self.turtle.pendown()
#             self.turtle.forward(120)  # Adjust the length of the lines
#             self.turtle.backward(120)
#             self.turtle.left(120)

#         # Draw a point at the meeting point
#         self.turtle.penup()
#         self.turtle.goto(0, 0)
#         self.turtle.pendown()
#         self.turtle.dot(5, "red")

#         # Add a label to display "360 degrees"
#         self.turtle.penup()
#         self.turtle.goto(30, -20)  # Adjust the position of the label
#         self.turtle.pendown()
#         self.turtle.write("360 degrees", align="center", font=("Arial", 12, "normal"))

#         messagebox.showinfo("Meet at a Point", "The angles meet at a point. The sum of angles around a point is 360 degrees.")

#     def on_a_straight_line(self):
#         # Draw a triangle with red points at the vertices where angles add up to 180 degrees
#         self.turtle.clear()
#         self.turtle.penup()
#         self.turtle.goto(-80, -50)  # Adjusted starting point
#         self.turtle.pendown()

#         # Draw a triangle
#         for _ in range(3):
#             self.turtle.forward(100)
#             self.turtle.left(120)

#         # Draw red points at the vertices
#         self.turtle.penup()
#         self.turtle.goto(-80, -50)  # Adjusted starting point
#         self.turtle.pendown()
#         self.turtle.dot(5, "red")

#         # Draw a red dot at the other point of the triangle touching the line
#         self.turtle.penup()
#         self.turtle.goto(20, -50)  # Adjusted position for the bottom vertex
#         self.turtle.pendown()
#         self.turtle.dot(5, "red")

#         # Draw a straight line through the red dots
#         self.turtle.penup()
#         self.turtle.goto(-160, -50)  # Adjusted starting point for the line
#         self.turtle.pendown()
#         self.turtle.goto(120, -50)  # Adjusted ending point for the line

#         # Draw labels

#         self.turtle.penup()
#         self.turtle.goto(20, -75)  # Adjusted label position for the bottom red dot
#         self.turtle.pendown()
#         self.turtle.write("180 degrees", font=("Arial", 12, "normal"))

#         self.turtle.penup()
#         self.turtle.goto(-80, -75)  # Adjusted label position for the bottom red dot
#         self.turtle.pendown()
#         self.turtle.write("180 degrees", font=("Arial", 12, "normal"))

#         messagebox.showinfo("On a Straight Line", "The angles are on a straight line. The sum of angles on a straight line is 180 degrees.")

#     def vertically_opposite(self):
#         # Clear the canvas
#         self.turtle.clear()

#         # Define angles for the two sets of opposite angles
#         angles_set1 = [30, 150]  # Adjust the angles as needed
#         angles_set2 = [30, 150]  # Adjust the angles as needed

#         # Draw a red dot in the middle
#         self.turtle.penup()
#         self.turtle.goto(0, -50)
#         self.turtle.pendown()
#         self.turtle.dot(5, "red")

#         # Draw lines extending from the red dot for the first set of opposite angles
#         for angle in angles_set1:
#             self.turtle.penup()
#             self.turtle.goto(0, -50)
#             self.turtle.pendown()
#             self.turtle.forward(120)  # Adjust the length of the lines
#             self.turtle.backward(120)
#             self.turtle.left(angle)

#         # Draw lines extending from the red dot for the second set of opposite angles
#         for angle in angles_set2:
#             self.turtle.penup()
#             self.turtle.goto(0, -50)
#             self.turtle.pendown()
#             self.turtle.forward(120)  # Adjust the length of the lines
#             self.turtle.backward(120)
#             self.turtle.left(angle)

#         messagebox.showinfo("Vertically Opposite", "The angles are vertically opposite. Vertically opposite angles are equal and add up to 360 degrees.")

# if __name__ == "__main__":
#     app = AngleTool(None)
#     app.geometry("800x600")
#     app.mainloop()



# angle.py
import tkinter as tk
from tkinter import ttk
from home_angle_tab import HomeTab
from angles_guide import AnglesGuide




class AngleTool(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#ecf0f1")
        self.tab_control = ttk.Notebook(self)

        # Initialize and add tabs
        self.home_angle_tab = HomeTab(self.tab_control)
        self.angles_guide = AnglesGuide(self.tab_control)


        self.tab_control.add(self.home_angle_tab, text='Home')
        self.tab_control.add(self.angles_guide, text='Angles Guide')

        

        self.tab_control.pack(expand=1, fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    app = AngleTool(root)
    root.mainloop()







