import tkinter as tk

class FindingUnknownAngles(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        label = tk.Label(self, text="Welcome to the Unknown Angles Tab")
        label.pack()