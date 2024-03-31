import tkinter as tk
from tkinter import ttk
import turtle

class CoordShapeTab(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill="both", expand=True)



if __name__ == "__main__":
    root = tk.Tk()
    tab = CoordShapeTab(root)
    tab.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()

  

