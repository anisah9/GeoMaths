import tkinter as tk
from tkinter import ttk, scrolledtext
from shape import GeometryTool

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.welcome_label = tk.Label(self, text="Welcome to GeoMaths!\nA tool to help with geometry concepts while also improving programming skills.")
        self.welcome_label.pack(pady=10)

        self.learn_button = tk.Button(self, text="Learn about 2D Shapes", command=self.show_shapes)
        self.learn_button.pack(pady=5)

    def show_shapes(self):
        self.controller.show_frame(GeometryTool)


class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, "Turtle Graphics Tool")

        self.notebook = ttk.Notebook(self)

        self.welcome_page = WelcomePage(self.notebook, self)
        self.shapes_page = GeometryTool(self.notebook)

        self.notebook.add(self.welcome_page, text="Welcome")
        self.notebook.add(self.shapes_page, text="2D Shapes")

        self.notebook.pack(expand=1, fill="both")

    def show_frame(self, frame_class):
        """Show a frame for the given class"""
        for index, child in enumerate(self.notebook.winfo_children()):
            if isinstance(child, frame_class):
                self.notebook.select(index)
                break

if __name__ == "__main__":
    app = MainApp()
    app.geometry("600x400")
    app.mainloop()


