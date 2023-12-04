import tkinter as tk

class CoordinateTool(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#ecf0f1")
        self.winfo_toplevel().title("Coordinate Tool")
    
if __name__ == "__main__":
    app = CoordinateTool(None)
    app.geometry("800x600")
    app.mainloop()