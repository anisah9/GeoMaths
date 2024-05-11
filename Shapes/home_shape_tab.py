# home_shape_tab.py
import tkinter as tk
from PIL import Image, ImageTk  # Import for handling images

class HomeShapeTab(tk.Frame):
    def __init__(self, master, notebook, **kwargs):
        # Initialise the HomeShapeTab class as a Frame 
        super().__init__(master, **kwargs)
        self.notebook = notebook    # Store reference to the notebook widget to manage tabs
        self.config(bg="#ecf0f1") 
        self.create_widgets()   # Call to create initial widgets on the tab
        self.load_and_display_image()   # Call to load and display an introductory image

    def create_widgets(self):
        # Create and pack the welcome label with padding
        label = tk.Label(self, text="Welcome to the Home Tab", font=("Arial", 16), bg="#ecf0f1")
        label.pack(pady=20, padx=10)

        # Introductory text explaining what the tab is about
        intro_text = "Explore geometric shapes and learn to draw with turtle graphics! Choose a tab to start drawing shapes, learn about geometry, and create shapes through coding."
        intro_label = tk.Label(self, text=intro_text, wraplength=400, justify="left", bg="#ecf0f1")
        intro_label.pack(pady=10, padx=10)

        # Buttons that navigate to other tabs
        shape_guide_button = tk.Button(self, text="Go to Shape Guide", command=self.goto_shape_guide)
        shape_guide_button.pack(pady=5, padx=10)

        draw_shape_button = tk.Button(self, text="Go to Draw Shapes", command=self.goto_draw_shape)
        draw_shape_button.pack(pady=5, padx=10)

    def load_and_display_image(self):
        # Load an image and display it on the tab
        image_path = "Images/shape.jpg"
        image = Image.open(image_path)
        photo_image = ImageTk.PhotoImage(image)
        image_label = tk.Label(self, image=photo_image, bg="#ecf0f1")
        image_label.image = photo_image  
        image_label.pack(pady=20)

    def goto_shape_guide(self):
        # Navigate to the Shape Guide tab
        self.notebook.select(1)

    def goto_draw_shape(self):
        # Navigate to the Draw Shapes tab
        self.notebook.select(2)

