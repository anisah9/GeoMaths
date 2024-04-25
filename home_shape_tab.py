import tkinter as tk
from tkinter import messagebox
import random
import turtle

class HomeShapeTab(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg="#ecf0f1")  # Background color
        self.create_widgets()

    def create_widgets(self):
        # Welcome Label
        label = tk.Label(self, text="Welcome to the Home Tab", font=("Arial", 16), bg="#ecf0f1")
        label.pack(pady=20, padx=10)

        # Introduction Text
        intro_text = "Explore geometric shapes and learn to draw with turtle graphics! Choose a tab to start drawing shapes, learn about geometry, or even create your own custom shapes."
        intro_label = tk.Label(self, text=intro_text, wraplength=400, justify="left", bg="#ecf0f1")
        intro_label.pack(pady=10, padx=10)

        # Navigation Button to Shape Guide
        self.shape_guide_button = tk.Button(self, text="Go to Shape Guide", command=self.goto_shape_guide)
        self.shape_guide_button.pack(pady=5, padx=10)

        # Navigation Button to Custom Drawing
        self.custom_draw_button = tk.Button(self, text="Create Custom Shapes", command=self.goto_custom_draw)
        self.custom_draw_button.pack(pady=5, padx=10)

        # Shape of the Day
        self.shape_of_the_day_button = tk.Button(self, text="Show Shape of the Day", command=self.show_and_draw_shape)
        self.shape_of_the_day_button.pack(pady=5, padx=10)

        # Mini Canvas for live preview
        self.preview_canvas = tk.Canvas(self, width=200, height=200, bg="white")
        self.preview_canvas.pack(pady=10, padx=10)
        self.t = turtle.RawTurtle(turtle.TurtleScreen(self.preview_canvas))
        self.t.speed("fastest")

    def show_and_draw_shape(self):
        shapes = {"Square": self.draw_square, "Circle": self.draw_circle, "Triangle": self.draw_triangle, "Rectangle": self.draw_rectangle}
        shape_of_the_day = random.choice(list(shapes.keys()))
        messagebox.showinfo("Shape of the Day", f"Today's shape is: {shape_of_the_day}\nSee it drawn on the mini canvas!")
        shapes[shape_of_the_day]()  # Call the drawing method

    def draw_square(self):
        self.t.clear()
        for _ in range(4):
            self.t.forward(50)
            self.t.right(90)

    def draw_circle(self):
        self.t.clear()
        self.t.circle(40)

    def draw_triangle(self):
        self.t.clear()
        for _ in range(3):
            self.t.forward(60)
            self.t.right(120)

    def draw_rectangle(self):
        self.t.clear()
        for _ in range(2):
            self.t.forward(200)  
            self.t.right(90)
            self.t.forward(100)  
            self.t.right(90)


    def display_shape_of_the_day(self):
        shapes = ["Square", "Circle", "Triangle", "Rectangle"]
        shape_of_the_day = random.choice(shapes)
        messagebox.showinfo("Shape of the Day", f"Today's shape is: {shape_of_the_day}\nLearn how to draw it in the Shape Guide!")

    def goto_shape_guide(self):
        messagebox.showinfo("Navigation", "This would take you to the Shape Guide tab.")

    def goto_custom_draw(self):
        messagebox.showinfo("Navigation", "This would navigate to the Custom Drawing tab.")
