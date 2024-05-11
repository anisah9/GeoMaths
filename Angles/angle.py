# angle.py
import tkinter as tk
from tkinter import ttk
from Angles.home_angle_tab import HomeAngleTab # Import the class for the 'Home' tab
from Angles.angles_guide import AnglesGuide    # Import the class for the 'Angles Guide' tab
from Angles.angles_triangles import AnglesInTriangles   # Import the class for the 'Angles in Triangles' tab

class AngleTool(tk.Frame):
    def __init__(self, master):
        # Initialise the AngleTool class as a Frame 
        super().__init__(master, bg="#ecf0f1")
        # Create a notebook (tab control) widget to manage multiple tabs
        self.tab_control = ttk.Notebook(self)

        # Create instances of each tab page class
        self.home_angle_tab = HomeAngleTab(self.tab_control, self.tab_control) 
        self.angles_guide = AnglesGuide(self.tab_control)
        self.angles_triangles = AnglesInTriangles(self.tab_control)

        # Add the created tab pages to the notebook with labels
        self.tab_control.add(self.home_angle_tab, text='Home')
        self.tab_control.add(self.angles_guide, text='Angles Guide')
        self.tab_control.add(self.angles_triangles, text='Angles in Triangles')

        # Pack the notebook to make it visible and fill the available space
        self.tab_control.pack(expand=1, fill="both")

if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = AngleTool(root)   # Create an instance of the AngleTool class
    root.mainloop() # Start the main event loop to handle user interactions





