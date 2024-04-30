import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from shape import ShapeTool
from angle import AngleTool
from coordinate import CoordinateTool

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ecf0f1")
        self.controller = controller

        # Top frame for the title and welcome message
        top_frame = tk.Frame(self, bg="#ecf0f1")
        top_frame.pack(side="top", fill="x", expand=True)
        welcome_label = tk.Label(top_frame, text="Welcome to GeoMaths!", font=("Arial", 24, "bold"), bg="#ecf0f1", fg="#2c3e50")
        welcome_label.pack(pady=10)
        subtitle_label = tk.Label(top_frame, text="A tool to help with geometry concepts while also learning some programming skills.", font=("Arial", 14), bg="#ecf0f1", fg="#34495e")
        subtitle_label.pack(pady=10)

        # Middle frame for the buttons
        middle_frame = tk.Frame(self, bg="#ecf0f1")
        middle_frame.pack(side="top", fill="x", expand=True)
        learn_shapes_button = tk.Button(middle_frame, text="Learn about 2D Shapes", command=lambda: controller.show_frame(ShapeTool), bg="#3498db", fg="black", font=("Arial", 12, "bold"), padx=10, pady=10)
        learn_shapes_button.pack(pady=20, padx=20)
        learn_angles_button = tk.Button(middle_frame, text="Learn about Angles", command=lambda: controller.show_frame(AngleTool), bg="#9b59b6", fg="black", font=("Arial", 12, "bold"), padx=10, pady=10)
        learn_angles_button.pack(pady=20, padx=20)
        learn_coordinates_button = tk.Button(middle_frame, text="Learn about Coordinates", command=lambda: controller.show_frame(CoordinateTool), bg="#e67e22", fg="black", font=("Arial", 12, "bold"), padx=10, pady=10)
        learn_coordinates_button.pack(pady=20, padx=20)

        # Bottom frame for images and additional information
        bottom_frame = tk.Frame(self, bg="#ecf0f1")
        bottom_frame.pack(side="top", fill="x", expand=True)

        # Load and display image
        image_path = "Images/background.jpg" 
        image = Image.open(image_path)
        photo_image = ImageTk.PhotoImage(image)
        image_label = tk.Label(bottom_frame, image=photo_image, bg="#ecf0f1")
        image_label.image = photo_image 
        image_label.pack(pady=20)

class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, "GeoMaths")
        self.configure(bg="#ecf0f1") 

        self.notebook = ttk.Notebook(self)
        self.welcome_page = WelcomePage(self.notebook, self)
        self.shapes_page = ShapeTool(self.notebook)
        self.angles_page = AngleTool(self.notebook)
        self.coordinates_page = CoordinateTool(self.notebook)

        self.notebook.add(self.welcome_page, text="Welcome")
        self.notebook.add(self.shapes_page, text="2D Shapes")
        self.notebook.add(self.angles_page, text="Angles and Triangles")
        self.notebook.add(self.coordinates_page, text="Coordinate Systems")
        self.notebook.pack(expand=1, fill="both")

    def show_frame(self, frame_class):
        for index, child in enumerate(self.notebook.winfo_children()):
            if isinstance(child, frame_class):
                self.notebook.select(index)
                break

if __name__ == "__main__":
    app = MainApp()
    app.geometry("600x400")
    app.mainloop()
