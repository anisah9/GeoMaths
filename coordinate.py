# coordinate.py
import tkinter as tk
from tkinter import ttk
from home_coord_tab import HomeCoordTab
from full_grid_tab import FullGridTab
from translate_shape_tab import TranslateShapeTab
from reflect_shape_tab import ReflectShapeTab



class CoordinateTool(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#ecf0f1")
        self.tab_control = ttk.Notebook(self)

        # Initialize and add tabs
        self.home_coord_tab = HomeCoordTab(self.tab_control) 
        self.full_grid_tab = FullGridTab(self.tab_control) 
        self.translate_shape_tab = TranslateShapeTab(self.tab_control)
        self.reflect_shape_tab = ReflectShapeTab(self.tab_control)

        self.tab_control.add(self.home_coord_tab, text='Home')
        self.tab_control.add(self.full_grid_tab, text='Full Coordinate Grid')
        self.tab_control.add(self.translate_shape_tab, text='Translate Shapes')
        self.tab_control.add(self.reflect_shape_tab, text='Reflect Shapes')
        

        self.tab_control.pack(expand=1, fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    app = CoordinateTool(root)
    root.mainloop()





