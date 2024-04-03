import tkinter as tk

class ReflectShapeTab(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#ecf0f1")
    
if __name__ == "__main__":
    app = ReflectShapeTab(None)
    app.geometry("800x600")
    app.mainloop()