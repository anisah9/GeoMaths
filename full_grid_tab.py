import tkinter as tk
import PySimpleGUI as sg
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class FullGridTab(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Create a new Matplotlib figure and subplot
        
        self.figure = Figure(figsize=(6, 6), dpi=100)
        self.plot = self.figure.add_subplot(111)

        # Set aspects of the plot
        self.plot.set_aspect('equal', adjustable='box')
        self.plot.grid(True)
        axis_limit = 10  # Change this to set different limits
        self.plot.set_xlim(-axis_limit, axis_limit)
        self.plot.set_ylim(-axis_limit, axis_limit)

        # Configure plot spines
        self.plot.spines['left'].set_position('zero')
        self.plot.spines['bottom'].set_position('zero')
        self.plot.spines['right'].set_color('none')
        self.plot.spines['top'].set_color('none')

        # Configure ticks
        self.plot.xaxis.set_ticks_position('bottom')
        self.plot.yaxis.set_ticks_position('left')
        self.plot.tick_params(axis='both', which='both', direction='out')

        # Embed the figure in the Tkinter frame
        self.canvas = FigureCanvasTkAgg(self.figure, self)  # Note 'self' is used here
        self.canvas.draw()
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Add Matplotlib's navigation toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.pack(side=tk.TOP, fill=tk.X, expand=False)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Label to introduce the concept
        self.label = tk.Label(self, text="The coordinate grid divides the plane into four quadrants. "
                                          "The X-axis goes horizontally and the Y-axis goes vertically.")
        self.label.pack(side=tk.TOP, pady=10)

        # Plotting functionality
        self.x_entry = tk.Entry(self)
        self.x_entry.pack(side=tk.LEFT)
        self.y_entry = tk.Entry(self)
        self.y_entry.pack(side=tk.LEFT)
        self.plot_button = tk.Button(self, text="Plot Point", command=self.plot_input_point)
        self.plot_button.pack(side=tk.LEFT)

        # Practice exercises guide
        self.practice_button = tk.Button(self, text="Practice Exercises", command=self.show_practice_guide)
        self.practice_button.pack(side=tk.TOP, pady=10)

        # Handle resizing
        self.bind("<Configure>", self.on_resize)

    def plot_input_point(self):
        # Get x and y from the entry fields, convert them to floats, and plot the point
        try:
            x = float(self.x_entry.get())
            y = float(self.y_entry.get())
            self.plot_point(x, y)  
            self.predict_quadrant(x, y)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid decimal numbers for X and Y coordinates.")

    def plot_point(self, x, y):
        # Plot a single point (x, y) on the grid
        self.plot.plot(x, y, 'ro')  # 'ro' stands for red circle
        self.canvas.draw()

    def predict_quadrant(self, x, y):
        # Predict and print which quadrant the point falls into
        if x > 0 and y > 0:
            quadrant = "first"
        elif x < 0 and y > 0:
            quadrant = "second"
        elif x < 0 and y < 0:
            quadrant = "third"
        elif x > 0 and y < 0:
            quadrant = "fourth"
        else:
            quadrant = "on an axis or at the origin"
        messagebox.showinfo("Quadrant Prediction", f"The point ({x}, {y}) falls into the {quadrant} quadrant.")

    def show_practice_guide(self):
        guide_text = "In the practice exercises, you will input different points and predict which quadrant they will fall into before plotting.\n\n"\
                     "Enter the X and Y coordinates in the respective entry fields and click 'Plot Point' to see the result.\n\n"\
                     "Remember:\n"\
                     "  - The X-axis goes horizontally.\n"\
                     "  - The Y-axis goes vertically.\n"\
                     "  - Positive X is to the right, negative X is to the left.\n"\
                     "  - Positive Y is upwards, negative Y is downwards."
        messagebox.showinfo("Practice Exercises Guide", guide_text)

    def on_resize(self, event):
        # Calculate the new size maintaining the aspect ratio
        new_size = min(event.width, event.height)
        if new_size > 0:
            new_size_inches = new_size / self.figure.dpi
            self.figure.set_size_inches(new_size_inches, new_size_inches, forward=True)
            self.canvas.draw_idle()
    
    def show_guide(self):  # Corrected function definition
        guide_layout = [
            [sg.Text("In the practice exercises, you will input different points and predict which quadrant they will fall into before plotting.")],
            [sg.Text("Enter the X and Y coordinates in the respective entry fields and click 'Plot Point' to see the result.")],
            [sg.Text("Remember:")],
            [sg.Text("  - The X-axis goes horizontally.")],
            [sg.Text("  - The Y-axis goes vertically.")],
            [sg.Text("  - Positive X is to the right, negative X is to the left.")],
            [sg.Text("  - Positive Y is upwards, negative Y is downwards.")],
            [sg.Button("Close")]
        ]
        guide_window = sg.Window("Practice Exercises Guide", guide_layout)
        while True:
            event, _ = guide_window.read()
            if event == sg.WINDOW_CLOSED or event == "Close":
                break
        guide_window.close()

# Example of usage
if __name__ == "__main__":
    root = tk.Tk()
    tab = FullGridTab(root)
    tab.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()


    


