import tkinter as tk
from tkinter import ttk
from home_shape_tab import HomeShapeTab
from shape_guide import ShapeGuide
from draw_shape_tab import DrawShapeTab

class ShapeTool(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#ecf0f1")
        self.tab_control = ttk.Notebook(self)

        self.home_shape_tab = HomeShapeTab(self.tab_control, self.tab_control)
        self.shape_guide = ShapeGuide(self.tab_control)
        self.draw_shape_tab = DrawShapeTab(self.tab_control)
    
        self.tab_control.add(self.home_shape_tab, text='Home')
        self.tab_control.add(self.shape_guide, text='Shape Guide')
        self.tab_control.add(self.draw_shape_tab, text='Draw Shapes')
    
        self.tab_control.pack(expand=1, fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeTool(root)
    root.mainloop()
