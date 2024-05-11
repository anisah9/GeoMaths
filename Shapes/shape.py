# shape.py
import tkinter as tk
from tkinter import ttk
from Shapes.home_shape_tab import HomeShapeTab  # Import the HomeShapeTab class for the home tab of shape tool
from Shapes.shape_guide import ShapeGuide   # Import the ShapeGuide class for the shape guide tab
from Shapes.draw_shape_tab import DrawShapeTab   # Import the DrawShapeTab class for the draw shapes tab

class ShapeTool(tk.Frame):
    def __init__(self, master):
        # Initialise the ShapeTool class as a Frame with a specified background color
        super().__init__(master, bg="#ecf0f1")
        # Create a notebook (tab control) widget to manage multiple tabs
        self.tab_control = ttk.Notebook(self)

        # Create instances of each tab page class
        self.home_shape_tab = HomeShapeTab(self.tab_control, self.tab_control)  # Home tab for basic information and welcome
        self.shape_guide = ShapeGuide(self.tab_control)  # Tab that provides a guide to different shapes
        self.draw_shape_tab = DrawShapeTab(self.tab_control)  # Tab that allows users to draw shapes interactively
    
        # Add the created tab pages to the notebook with appropriate labels
        self.tab_control.add(self.home_shape_tab, text='Home')
        self.tab_control.add(self.shape_guide, text='Shape Guide')
        self.tab_control.add(self.draw_shape_tab, text='Draw Shapes')
    
        # Pack the notebook to make it visible and fill the available space
        self.tab_control.pack(expand=1, fill="both")

if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = ShapeTool(root)  # Instantiate the ShapeTool class
    root.mainloop()   # Start the main event loop for handling user interactions


