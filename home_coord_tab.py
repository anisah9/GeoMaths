import tkinter as tk
from PIL import Image, ImageTk

class HomeCoordTab(tk.Frame):
    def __init__(self, master, notebook, **kwargs):
        super().__init__(master, **kwargs)
        self.notebook = notebook 
        self.config(bg="#ecf0f1")  
        self.create_widgets()
        self.load_and_display_image()
    
    def create_widgets(self):
        label = tk.Label(self, text="Welcome to the Home Tab", font=("Arial", 16), bg="#ecf0f1")
        label.pack(pady=20, padx=10)

        intro_text = "Explore the world of coordinates, translation, and reflection of shapes. Get started by selecting one of the options below."
        intro_label = tk.Label(self, text=intro_text, wraplength=400, justify="left", bg="#ecf0f1")
        intro_label.pack(pady=10, padx=10)

        # Example Button to Full Grid
        grid_button = tk.Button(self, text="Go to Full Coordinate Grid", command=self.goto_full_grid)
        grid_button.pack(pady=5, padx=10)
        
        # Example Button to Translate Shapes
        translate_button = tk.Button(self, text="Go to Translate Shapes", command=self.goto_translate_shapes)
        translate_button.pack(pady=5, padx=10)

        # Example Button to Translate Shapes
        reflect_button = tk.Button(self, text="Go to Reflect Shapes", command=self.goto_reflect_shapes)
        reflect_button.pack(pady=5, padx=10)

    def load_and_display_image(self):
        
        image_path = "Images/grid.jpg"
        image = Image.open(image_path)
        photo_image = ImageTk.PhotoImage(image)
        image_label = tk.Label(self, image=photo_image, bg="#ecf0f1")
        image_label.image = photo_image  
        image_label.pack(pady=20)

    def goto_full_grid(self):
        self.notebook.select(1)

    def goto_translate_shapes(self):
        self.notebook.select(2)

    def goto_reflect_shapes(self):
        self.notebook.select(3)