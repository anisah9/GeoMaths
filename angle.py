import tkinter as tk
from tkinter import ttk
from home_angle_tab import HomeAngleTab
from angles_guide import AnglesGuide
from angles_triangles import AnglesInTriangles

class AngleTool(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#ecf0f1")
        self.tab_control = ttk.Notebook(self)

        self.home_angle_tab = HomeAngleTab(self.tab_control, self.tab_control) 
        self.angles_guide = AnglesGuide(self.tab_control)
        self.angles_triangles = AnglesInTriangles(self.tab_control)

        self.tab_control.add(self.home_angle_tab, text='Home')
        self.tab_control.add(self.angles_guide, text='Angles Guide')
        self.tab_control.add(self.angles_triangles, text='Angles in Triangles')

        self.tab_control.pack(expand=1, fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    app = AngleTool(root)
    root.mainloop()






