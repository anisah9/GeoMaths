# full_grid_tab.py
import tkinter as tk    # Importing tkinter module as tk
from tkinter import messagebox   # Importing messagebox submodule from tkinter
from matplotlib.figure import Figure    # Importing Figure class from matplotlib.figure module
from matplotlib.backends.backend_tkagg import ( # Importing necessary classes from matplotlib backend module
    FigureCanvasTkAgg, NavigationToolbar2Tk)

class CustomToolbar(NavigationToolbar2Tk):
    toolitems = [t for t in NavigationToolbar2Tk.toolitems if t[0] not in ('Zoom', 'Subplots')]
    # Custom toolbar class inheriting from NavigationToolbar2Tk
    # Override toolitems attribute to exclude 'Zoom' and 'Subplots' tools

class FullGridTab(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.axis_limit = 10    # Setting the limit for the axis

        # Information panel on the left
        self.info_panel = tk.Frame(self, width=300, height=600) # Creating a frame for the information panel
        self.info_panel.pack(side=tk.LEFT, fill=tk.Y)   # Packing the information panel on the left side
        self.info_panel.pack_propagate(False)   # Preventing the frame from shrinking to fit its contents

        # Control panel on the right
        self.control_panel = tk.Frame(self, width=300, height=600)  # Creating a frame for the control panel
        self.control_panel.pack(side=tk.RIGHT, fill=tk.Y)   # Packing the control panel on the right side
        self.control_panel.pack_propagate(False)    # Preventing the frame from shrinking to fit its contents

        # Creating a figure and subplot for plotting
        self.figure = Figure(figsize=(6, 6), dpi=100)
        self.plot = self.figure.add_subplot(111)
        self.setup_plot()   # Setting up the plot

        # Creating a canvas for the figure
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.draw()
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Adding a toolbar for navigation
        self.toolbar = CustomToolbar(self.canvas, self)
        self.toolbar.update()
        self.toolbar.pack(side=tk.TOP, fill=tk.X, expand=False)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Text box for information display
        self.info_box = tk.Text(self.info_panel, width=80, height=10, wrap=tk.WORD)
        self.info_box.pack(pady=10)

        # Styling the information box
        self.info_box.configure(bg="#f0f0f0",  # Light gray background color
                                bd=2,  # Border width
                                relief=tk.SOLID,  # Border style
                                padx=10,  # Horizontal padding
                                pady=10,  # Vertical padding
                                font=("Arial", 12))  # Default font style

        # Configuring tags for different text styles
        self.info_box.tag_configure("title", font=("Arial", 16, "bold"))
        self.info_box.insert(tk.END, "Welcome to the Coordinate Grid!\n\n", "title")

        self.info_box.tag_configure("message", font=("Arial", 12))
        self.info_box.insert(tk.END, "Here, you'll explore points and plots on the interactive grid.\nLearn all about coordinates, and discover how to plot points with precision and understand the unique quadrants that make up the grid.", "message")

        self.info_boxes = []    # Initialising a list to store additional info boxes

        additional_info = [
            "What is a Coordinate Grid?",
            "The Origin",
            "Coordinates",
            "Plotting Points",
            "Quadrants",
            "Directions on the Grid"
        ]

        for info in additional_info:
            box = tk.Text(self.control_panel, width=80, height=6, wrap=tk.WORD)
            box.pack(pady=5)
            box.configure(bg="#f0f0f0",  # Light gray background color
                          bd=2,  # Border width
                          relief=tk.SOLID,  # Border style
                          padx=10,  # Horizontal padding
                          pady=10,  # Vertical padding
                          font=("Arial", 11)) 
            self.info_boxes.append(box)

        # Define additional information content
        additional_info_content = [
            "A coordinate grid is like a big sheet of paper with two main lines: one that goes across (the x-axis) and one that goes up and down (the y-axis).",
            "The origin is where the two lines meet, always located at (0, 0).",
            "Each point on the grid has coordinates, like a home address, consisting of two parts: one for the x-axis (left or right) and one for the y-axis (up or down).",
            "To plot a point, follow its coordinates. For example, (3, 2) means moving 3 steps to the right and 2 steps up from the origin.",
            "The grid has four quadrants, each with its own pattern of positive and negative numbers.",
            "Moving along the x-axis, use words like \"left\" or \"right.\" Moving along the y-axis, use words like \"up\" or \"down.\" Going up makes the number bigger, and going down makes it smaller."
        ]

        for i, (info, content) in enumerate(zip(additional_info, additional_info_content)):
            self.info_boxes[i].tag_configure("subheading", font=("Arial", 14, "bold"), spacing3=0)  
            self.info_boxes[i].insert(tk.END, f"{i + 1}. {info}\n", "subheading")
            self.info_boxes[i].tag_configure("additional_info", font=("Arial", 12), spacing1=0)
            self.info_boxes[i].insert(tk.END, f"{content}\n", "additional_info")


        # Disable editing for all boxes
        for box in self.info_boxes:
            box.config(state=tk.DISABLED)

        # Frame for plot controls
        self.plot_controls_frame = tk.Frame(self.info_panel, bg="#f0f0f0", bd=2, relief=tk.SOLID)
        self.plot_controls_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Text box for plot instructions
        self.plot_instructions_box = tk.Text(self.plot_controls_frame, height=4, wrap=tk.WORD)
        self.plot_instructions_box.pack(padx=10, pady=(10, 0), fill=tk.X)
        self.plot_instructions_box.configure(bg="#f0f0f0",  # Background color
                                             relief=tk.FLAT,  # Border style
                                             font=("Arial", 11))  # Font style
        
        # Configure tags for different text styles
        self.plot_instructions_box.tag_configure("instruction_title", font=("Arial", 14, "bold"))
        self.plot_instructions_box.insert(tk.END, "Plot a Point on the Grid\n", "instruction_title")
        self.plot_instructions_box.tag_configure("instruction_text", font=("Arial", 11))
        self.plot_instructions_box.insert(tk.END, "Enter X and Y coordinates below and press 'Plot Point' to display them on the coordinate grid.", "instruction_text")

        self.plot_instructions_box.config(state=tk.DISABLED)    # Disable editing

        # Labels and entry boxes for X and Y coordinates
        self.x_label = tk.Label(self.plot_controls_frame, text="X-coordinate:", bg="#f0f0f0")
        self.x_label.pack(pady=(10, 2))
        self.x_entry = tk.Entry(self.plot_controls_frame)
        self.x_entry.pack(pady=(2, 10))

        self.y_label = tk.Label(self.plot_controls_frame, text="Y-coordinate:", bg="#f0f0f0")
        self.y_label.pack(pady=(2, 10))
        self.y_entry = tk.Entry(self.plot_controls_frame)
        self.y_entry.pack(pady=(2, 10))

        # Button to plot the point
        self.plot_button = tk.Button(self.plot_controls_frame, text="Plot Point", command=self.plot_input_point)
        self.plot_button.pack(pady=(2, 10))

        # Initialise coordinate history list
        self.coord_history = []

        # Text box for coordinate history
        self.history_box = tk.Text(self.info_panel, width=40, height=4, wrap=tk.WORD)
        self.history_box.pack(pady=10)
        self.history_box.configure(bg="#f0f0f0", bd=2, relief=tk.SOLID, padx=10, pady=10, font=("Arial", 12))
        self.history_box.tag_configure("history_title", font=("Arial", 14, "bold"))
        self.history_box.insert(tk.END, "Coordinate History:\n", "history_title")
        self.history_box.config(state=tk.DISABLED)

        # Text box for navigation instructions
        self.navigation_instructions_box = tk.Text(self.info_panel, width=40, height=4, wrap=tk.WORD)
        self.navigation_instructions_box.pack(pady=10)
        self.navigation_instructions_box.configure(bg="#f0f0f0", bd=2, relief=tk.SOLID, padx=10, pady=10)

        self.navigation_instructions_box.tag_configure("title_text", font=("Arial", 14, "bold"))

        self.navigation_instructions_box.tag_configure("instruction_text", font=("Arial", 12))

        self.navigation_instructions_box.insert(tk.END, "Navigation Instructions:\n", "title_text")

        self.navigation_instructions_box.insert(tk.END, "Use the toolbar to zoom and pan around the grid.", "instruction_text")

        self.navigation_instructions_box.config(state=tk.DISABLED)

    # Method to plot a point on the grid based on user input
    def plot_input_point(self):
        try:
            x = float(self.x_entry.get())   # Get X-coordinate from entry box and convert to float
            y = float(self.y_entry.get())   # Get Y-coordinate from entry box and convert to float
            self.plot.cla() # Clear the current plot

            # Update axis limit to accommodate new point and set up the plot
            new_limit = max(abs(x), abs(y), self.axis_limit)
            self.axis_limit = new_limit + 1 
            self.setup_plot()

            # Plot the point
            self.plot_point(x, y)

            # Set the limits of the plot to show the point and maintain the grid
            self.plot.set_xlim(x - self.axis_limit, x + self.axis_limit)
            self.plot.set_ylim(y - self.axis_limit, y + self.axis_limit)

            # Redraw canvas to reflect changes
            self.canvas.draw()

            # Add the coordinates to the history and update the display
            self.coord_history.append((x, y))
            self.update_coord_history()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid decimal numbers for X and Y coordinates.")
    
    # Method to update the coordinate history display
    def update_coord_history(self):
        self.history_box.config(state=tk.NORMAL)    # Enable editing
        self.history_box.delete("1.0", tk.END)   # Clear existing content
        self.history_box.insert(tk.END, "Coordinate History:\n", "history_title")   # Insert title

        # Show the last 5 points in reverse order
        for i, (x, y) in enumerate(reversed(self.coord_history[-5:])):  
            self.history_box.insert(tk.END, f"{i + 1}: ({x}, {y})\n", "history")

        self.history_box.config(state=tk.DISABLED)  # Disable editing

    # Method to set up the plot with grid and axes
    def setup_plot(self):
        self.plot.set_aspect('equal', adjustable='box') # Set aspect ratio to equal
        self.plot.grid(True)    # Enable grid
        self.plot.spines['left'].set_position('zero')    # Set position of left spine to zero
        self.plot.spines['bottom'].set_position('zero') # Set position of bottom spine to zero
        self.plot.spines['right'].set_color('none')  # Hide right spine
        self.plot.spines['top'].set_color('none')   # Hide top spine
        self.plot.xaxis.set_ticks_position('bottom')    # Set position of x-axis ticks
        self.plot.yaxis.set_ticks_position('left')      # Set position of y-axis ticks

    # Method to plot a point on the grid
    def plot_point(self, x, y):
        self.plot.plot(x, y, 'ro')  # Plot a red point at the given coordinates

    def setup_plot(self):
        self.plot.set_aspect('equal', adjustable='box')
        self.plot.grid(True)
        self.plot.set_xlim(-self.axis_limit, self.axis_limit)
        self.plot.set_ylim(-self.axis_limit, self.axis_limit)
        self.plot.spines['left'].set_position('zero')
        self.plot.spines['bottom'].set_position('zero')
        self.plot.spines['right'].set_color('none')
        self.plot.spines['top'].set_color('none')
        self.plot.xaxis.set_ticks_position('bottom')
        self.plot.yaxis.set_ticks_position('left')
    
if __name__ == "__main__":
    root = tk.Tk()  # Create root window
    tab = FullGridTab(root) # Create instance of FullGridTab
    tab.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop() # Run the Tkinter event loop





    