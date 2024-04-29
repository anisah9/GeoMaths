# home_tab.py
import tkinter as tk

class HomeCoordTab(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        label = tk.Label(self, text="Welcome to the Home Tab")
        label.pack()
