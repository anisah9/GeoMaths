# home_coord_tab.py
import tkinter as tk
from PIL import Image, ImageTk  # Import necessary for handling images

class HomeCoordTab(tk.Frame):
    def __init__(self, master, notebook, **kwargs):
        # Initialize the HomeCoordTab class as a Frame 
        super().__init__(master, **kwargs)
        self.notebook = notebook    # Store reference to the notebook widget to manage tabs
        self.config(bg="#ecf0f1")  
        self.create_widgets()   # Call to create initial widgets on the tab
        self.load_and_display_image()   # Call to load and display an introductory image
    
    def create_widgets(self):
        # Create and pack the welcome label with padding
        label = tk.Label(self, text="Welcome to the Home Tab", font=("Arial", 16), bg="#ecf0f1")
        label.pack(pady=20, padx=10)

        # Introductory text about coordinate geometry
        intro_text = "Explore the world of coordinates, translation, and reflection of shapes. Get started by selecting one of the options below."
        intro_label = tk.Label(self, text=intro_text, wraplength=400, justify="left", bg="#ecf0f1")
        intro_label.pack(pady=10, padx=10)

        # Buttons that navigate to other tabs
        grid_button = tk.Button(self, text="Go to Full Coordinate Grid", command=self.goto_full_grid)
        grid_button.pack(pady=5, padx=10)
        translate_button = tk.Button(self, text="Go to Translate Shapes", command=self.goto_translate_shapes)
        translate_button.pack(pady=5, padx=10)
        reflect_button = tk.Button(self, text="Go to Reflect Shapes", command=self.goto_reflect_shapes)
        reflect_button.pack(pady=5, padx=10)

    def load_and_display_image(self):
        # Load an image
        image_path = "Images/grid.jpg"
        image = Image.open(image_path)
        photo_image = ImageTk.PhotoImage(image)
        image_label = tk.Label(self, image=photo_image, bg="#ecf0f1")
        image_label.image = photo_image  
        image_label.pack(pady=20)

    def goto_full_grid(self):
        # Navigate to the Full Coordinate Grid tab
        self.notebook.select(1)

    def goto_translate_shapes(self):
        # Navigate to the Translate Shapes tab
        self.notebook.select(2)

    def goto_reflect_shapes(self):
        # Navigate to the Reflect Shapes tab
        self.notebook.select(3)