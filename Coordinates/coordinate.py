# coordinate.py
import tkinter as tk
from tkinter import ttk
from Coordinates.home_coord_tab import HomeCoordTab # Import the class for the Home tab in coordinate tool
from Coordinates.full_grid_tab import FullGridTab   # Import the class for displaying the full coordinate grid tab
from Coordinates.translate_shape_tab import TranslateShapeTab   # Import the class for the tab that deals with translating shapes
from Coordinates.reflect_shape_tab import ReflectShapeTab   # Import the class for the tab that deals with reflecting shapes

class CoordinateTool(tk.Frame):
    def __init__(self, master):
        # Initialise the CoordinateTool class as a Frame 
        super().__init__(master, bg="#ecf0f1")
        # Create a notebook (tab control) widget to manage multiple tabs
        self.tab_control = ttk.Notebook(self)

        # Create instances of each tab page class
        self.home_coord_tab = HomeCoordTab(self.tab_control, self.tab_control)  # Home tab for basic coordinate tool information
        self.full_grid_tab = FullGridTab(self.tab_control)  # Tab for interacting with a full coordinate grid
        self.translate_shape_tab = TranslateShapeTab(self.tab_control)  # Tab for functionality to translate shapes on the grid
        self.reflect_shape_tab = ReflectShapeTab(self.tab_control)  # Tab for functionality to reflect shapes on the grid

        # Add the created tab pages to the notebook with appropriate labels
        self.tab_control.add(self.home_coord_tab, text='Home')
        self.tab_control.add(self.full_grid_tab, text='Full Coordinate Grid')
        self.tab_control.add(self.translate_shape_tab, text='Translate Shapes')
        self.tab_control.add(self.reflect_shape_tab, text='Reflect Shapes')

        # Pack the notebook to make it visible and fill the available space
        self.tab_control.pack(expand=1, fill="both")

if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = CoordinateTool(root)  # Instantiate the CoordinateTool class
    root.mainloop() # Start the main event loop for handling user interactions
