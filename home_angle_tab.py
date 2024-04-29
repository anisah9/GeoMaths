import tkinter as tk
from PIL import Image, ImageTk

class HomeAngleTab(tk.Frame):
    def __init__(self, master, notebook, **kwargs):
        super().__init__(master, **kwargs)
        self.notebook = notebook
        self.config(bg="#ecf0f1")
        self.create_widgets()
        self.load_and_display_image()

    def create_widgets(self):
        label = tk.Label(self, text="Welcome to the Angle Home Tab", font=("Arial", 16), bg="#ecf0f1")
        label.pack(pady=20, padx=10)

        intro_text = "Learn about different types of angles and their properties. Explore how angles form in triangles and use interactive guides to enhance your understanding."
        intro_label = tk.Label(self, text=intro_text, wraplength=400, justify="left", bg="#ecf0f1")
        intro_label.pack(pady=10, padx=10)

        angles_guide_button = tk.Button(self, text="Go to Angles Guide", command=self.goto_angles_guide)
        angles_guide_button.pack(pady=5, padx=10)

        angles_triangles_button = tk.Button(self, text="Go to Angles in Triangles", command=self.goto_angles_in_triangles)
        angles_triangles_button.pack(pady=5, padx=10)

    def load_and_display_image(self):
        image_path = "Images/angles.jpg" 
        image = Image.open(image_path)
        photo_image = ImageTk.PhotoImage(image)
        image_label = tk.Label(self, image=photo_image, bg="#ecf0f1")
        image_label.image = photo_image
        image_label.pack(pady=20)

    def goto_angles_guide(self):
        self.notebook.select(1)

    def goto_angles_in_triangles(self):
        self.notebook.select(2)
