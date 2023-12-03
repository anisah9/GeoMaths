import tkinter as tk
from tkinter import ttk, scrolledtext
from shape import GeometryTool
from angle import AngleTool

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#3498db")  # Set background color
        self.controller = controller

        self.welcome_label = tk.Label(self, text="Welcome to GeoMaths!\nA tool to help with geometry concepts while also learning some programming skills.", font=("Arial", 12), bg="#3498db", fg="white")
        self.welcome_label.pack(pady=20)

        self.learn_shapes_button = tk.Button(self, text="Learn about 2D Shapes", command=self.show_shapes, bg="#2ecc71", fg="grey", font=("Arial", 10))
        self.learn_shapes_button.pack(pady=10)

        self.learn_angles_button = tk.Button(self, text="Learn about Angles", command=self.show_angles, bg="#2ecc71", fg="grey", font=("Arial", 10))
        self.learn_angles_button.pack(pady=10)

    def show_shapes(self):
        self.controller.show_frame(GeometryTool)

    def show_angles(self):
        self.controller.show_frame(AngleTool)


class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, "Turtle Graphics Tool")

        self.configure(bg="#ecf0f1") 

        self.notebook = ttk.Notebook(self)

        self.welcome_page = WelcomePage(self.notebook, self)
        self.shapes_page = GeometryTool(self.notebook)
        self.angles_page = AngleTool(self.notebook)

        self.notebook.add(self.welcome_page, text="Welcome")
        self.notebook.add(self.shapes_page, text="2D Shapes")
        self.notebook.add(self.angles_page, text="Angles and Triangles")

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


