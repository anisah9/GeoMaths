import tkinter as tk
import turtle
import math
import time

class ShapeGuide(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.pack(fill='both', expand=True)

        control_panel = tk.Frame(self, bg='light gray')
        control_panel.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        shadow = tk.Frame(self, bg='grey', width=512, height=512)
        shadow.pack_propagate(False)  
        shadow.pack(side=tk.LEFT, padx=(20, 0), pady=0)
        

        canvas_frame = tk.Frame(shadow, bg='white', highlightbackground='black', highlightthickness=1)
        canvas_frame.pack(padx=1, pady=1)  
        
        self.canvas = tk.Canvas(canvas_frame, width=500, height=500, bg='white')
        self.canvas.pack()

        self.screen = turtle.TurtleScreen(self.canvas)
        self.t = turtle.RawTurtle(self.screen)
        self.t.speed("fastest")

        self.info_label = tk.Label(control_panel, text="Welcome to Shape Guides", font=("Arial", 16, "bold"),
                                   width=40, anchor='w', wraplength=300, bg='light gray')
        self.info_label.pack(pady=10, fill=tk.X)

        # self.detail_text = tk.Text(control_panel, height=10, width=40, wrap=tk.WORD)
        self.detail_text = tk.Text(control_panel, height=10, width=40, wrap=tk.WORD, font=("Arial", 14)) 
        self.detail_text.pack(pady=10, fill=tk.X)
        

        self.last_click_time = time.time() 

        self.is_drawing = False  # Flag to indicate if a drawing is in progress

        self.setup_quiz_controls()

        self.slides = [
        "2D Shapes: Length and Width\n"
        "\n"
        "Imagine a flat piece of paper. That's a 2D shape. It only has length and width, like when you draw a square or a circle on a piece of paper. These shapes are all around us, and understanding them helps us describe and work with different things in the world.",

        "Polygons: Straight Line Shapes\n"
        "\n"
        "A polygon is a 2D shape with straight lines. Polygons are compared and classified according to the properties of their sides and angles. Think of a polygon as a shape made with straight lines. You know, like a triangle, square, or pentagon. Each of these shapes has its own special characteristics, like how many sides and angles it has. We can study them by comparing these sides and angles.",

        "Regular Polygons: Perfectly Balanced Shapes\n"
        "\n"
        "When all the sides of a shape are the same length and all the angles are the same size, we call it a regular polygon. So, a regular triangle would have three equal sides and three equal angles. It's like the superhero of shapes because it's super balanced and symmetrical!",

        "Parallel Lines: Always Staying Apart\n"
        "\n"
        "Imagine drawing two lines side by side that never touch each other, no matter how far you extend them. Those are parallel lines! They're like best friends who walk together but never hold hands. We see parallel lines in things like railway tracks or the edges of a book.",

        "Vertices: Where Lines Meet\n"
        "\n"
        "Picture where two streets meet on a map or where the corners of a triangle come together. That's a vertex! It's like a meeting point for lines or edges. So, when lines, edges, or sides come together, they form a vertex. It's where all the action happens in shapes!"
        ]

 

        self.current_slide = 0

        # New - Initialize a details panel, empty for now, same size and style as quiz panel
        details_panel = tk.Frame(self, bg='white', highlightbackground='black', highlightthickness=1)
        details_panel.pack_propagate(False)  # ensures the panel does not shrink
        details_panel.pack(side=tk.TOP, fill=tk.X, expand=False, padx=10, pady=10)
        details_panel.config(width=400, height=350)

        # Label to display the slides
        self.slide_label = tk.Label(details_panel, text=self.slides[self.current_slide], wraplength=380, justify='left', font=("Arial", 16))
        self.slide_label.pack(pady=20)

        # Navigation buttons
        btn_prev = tk.Button(details_panel, text="Previous", command=self.prev_slide)
        btn_prev.pack(side=tk.LEFT, padx=10)

        btn_next = tk.Button(details_panel, text="Next", command=self.next_slide)
        btn_next.pack(side=tk.RIGHT, padx=10)


        # Buttons for shapes with icons or text
        self.buttons = {}
        shapes = [
            ("Square", self.draw_square), ("Rectangle", self.draw_rectangle),
            ("Parallelogram", self.draw_parallelogram), ("Rhombus", self.draw_rhombus),
            ("Trapezium", self.draw_trapezium), ("Pentagon", self.draw_regular_pentagon),
            ("Hexagon", self.draw_regular_hexagon), ("Heptagon", self.draw_regular_heptagon),
            ("Octagon", self.draw_regular_octagon)
        ]

        # Increase padding between buttons here
        button_pad_y = (10, 10)
        for shape, command in shapes:
            btn = tk.Button(control_panel, text=shape, command=lambda cmd=command, s=shape: self.display_shape_info(cmd, s),
                            width=12, font=("Arial", 12))
            btn.pack(pady=button_pad_y, padx=10)

        self.size_slider = tk.Scale(control_panel, from_=50, to=200, orient=tk.HORIZONTAL, label="Size of Shape",
                                    command=self.update_info, bg='light gray', troughcolor='gray', sliderlength=20)
        self.size_slider.pack(fill=tk.X, padx=10, pady=20)

        self.shape_info = {
            "Square": "A square possesses four sides of equal length and four right angles, making it both a rectangle and a rhombus, and it also falls under the category of parallelograms.",
            "Rectangle": "A rectangle features two pairs of parallel sides of equal length and four right angles, thus classifying it as a parallelogram as well.",
            "Parallelogram": "A parallelogram has opposite sides parallel and equal in length. Opposite angles are equal.",
            "Rhombus": "A rhombus is a type of parallelogram with all sides equal in length. Opposite angles are equal.",
            "Trapezium": "A trapezium has a pair of parallel sides. It's a four-sided figure with no side constraints beyond this.",
            "Pentagon": "A regular pentagon has five equal sides and five equal angles of 108°. In regular and irregular pentagons, the interior angles will total 540°",
            "Hexagon": "A regular hexagon has six equal sides and six equal angles of 120°. In regular and irregular hexagons, the interior angles will total 720°.",
            "Heptagon": "A regular heptagon has seven equal sides and seven equal angles. In regular and irregular heptagons, the interior angles will total 900°.",
            "Octagon": "A regular octagon has eight equal sides and angles. Commonly recognized from stop signs."
        }



    
    def next_slide(self):
        self.current_slide = (self.current_slide + 1) % len(self.slides)
        self.slide_label.config(text=self.slides[self.current_slide])

    def prev_slide(self):
        self.current_slide = (self.current_slide - 1) % len(self.slides)
        self.slide_label.config(text=self.slides[self.current_slide])


    def display_shape_info(self, command, shape):
        if self.is_drawing:
          
            return
        self.is_drawing = True  # Set the flag to indicate a drawing is in progress
        command()
        self.detail_text.delete('1.0', tk.END)
        self.detail_text.insert(tk.END, self.shape_info.get(shape, "No information available."))
        self.is_drawing = False  # Reset the flag once the drawing is complete


    def clear_and_reset(self):
        """Clears the drawing and resets the turtle position and orientation."""
        self.t.clear()
        self.t.penup()
        self.t.home()
        self.t.pendown()
        self.t.setheading(0)

    def update_info(self, val):
        """Update the information label with details about the shape based on the slider value."""
        size = int(val)
        if hasattr(self, 'current_shape'):
            
            self.info_label.config(text=f"Size: {size}")
        else:
            self.info_label.config(text="Adjust the slider to change the size of the shape.")

    def draw_regular_polygon(self, sides):
        if self.is_drawing:
            return 

        self.is_drawing = True
        side_length = self.size_slider.get()
        self.info_label.config(text=f"A regular polygon with {sides} sides.")
        self.clear_and_reset()
        self.set_starting_position(sides, side_length)
        angle = 360 / sides

        for _ in range(sides):
            self.t.dot(10, "blue")
            self.t.forward(side_length)
            self.t.left(angle)

        self.after(100, lambda: setattr(self, 'is_drawing', False))



    def set_starting_position(self, sides, side_length):
        """Position turtle to start drawing the shape centered."""
        central_angle = 360 / sides
        apothem = side_length / (2 * math.tan(math.pi / sides))
        self.t.penup()
        self.t.goto(-side_length / 2, -apothem)
        self.t.pendown()


    def draw_square(self):
        self.current_shape = 'Square'
        self.draw_regular_polygon(4, "Square")


    def draw_rectangle(self):
        """Draws a rectangle with blue vertices."""
        length = self.size_slider.get()
        breadth = length * 0.6
        self.info_label.config(text="Rectangle")
        self.clear_and_reset()
        self.t.penup()
        self.t.goto(-length / 2, breadth / 2)
        self.t.pendown()
        
        for _ in range(2):
            self.t.dot(10, "blue")
            self.t.forward(length)
            self.t.right(90)
            self.t.dot(10, "blue")
            self.t.forward(breadth)
            self.t.right(90)

    def draw_parallelogram(self):
        """Draws a parallelogram with blue vertices."""
        base = self.size_slider.get()
        side = base * 0.75
        angle = 60
        self.info_label.config(text="Parallelogram")
        self.clear_and_reset()
        self.t.penup()
        self.t.goto(-base / 2, 0)
        self.t.pendown()
        
        for _ in range(2):
            self.t.dot(10, "blue")
            self.t.forward(base)
            self.t.left(180 - angle)
            self.t.dot(10, "blue")
            self.t.forward(side)
            self.t.left(angle)

    def draw_rhombus(self):
        """Draws a rhombus with blue vertices."""
        side = self.size_slider.get()
        angle = 60
        self.info_label.config(text="Rhombus")
        self.clear_and_reset()
        self.t.penup()
        self.t.goto(-side / 2, 0)
        self.t.pendown()
        
        for _ in range(2):
            self.t.dot(10, "blue")
            self.t.forward(side)
            self.t.left(180 - angle)
            self.t.dot(10, "blue")
            self.t.forward(side)
            self.t.left(angle)
        self.t.dot(10, "blue")

    def draw_trapezium(self):
        """Draws a trapezium with one pair of parallel sides."""
        base1 = self.size_slider.get()  
        base2 = base1 * 0.75 
        height = base1 * 0.5 

        side_slope_angle = math.degrees(math.atan2(height, (base1 - base2) / 2))

        self.info_label.config(text="Trapezium")
        self.clear_and_reset()


        self.t.penup()
        self.t.goto(-base1 / 2, -height / 2)
        self.t.setheading(0) 
        self.t.pendown()

        self.t.dot(10, "blue")
        self.t.forward(base1)
        self.t.dot(10, "blue")
        
        self.t.left(180 - side_slope_angle)
        self.t.forward(math.hypot(height, (base1 - base2) / 2))
        self.t.dot(10, "blue")
        
        self.t.left(side_slope_angle)
        self.t.forward(base2)
        self.t.dot(10, "blue")
        
        self.t.left(side_slope_angle)
        self.t.forward(math.hypot(height, (base1 - base2) / 2))

    def draw_regular_polygon(self, sides, shape_name="Polygon"):
        side_length = self.size_slider.get()
        self.info_label.config(text=shape_name)  # Use the shape name directly
        self.clear_and_reset()
        self.set_starting_position(sides, side_length)
        angle = 360 / sides
        for _ in range(sides):
            self.t.dot(10, "blue")
            self.t.forward(side_length)
            self.t.left(angle)

    def draw_regular_pentagon(self):
        self.current_shape = 'Pentagon'
        self.draw_regular_polygon(5, "Pentagon")

    def draw_regular_hexagon(self):
        self.current_shape = 'Hexagon'
        self.draw_regular_polygon(6, "Hexagon")

    def draw_regular_heptagon(self):
        self.current_shape = 'Heptagon'
        self.draw_regular_polygon(7, "Heptagon")

    def draw_regular_octagon(self):
        self.current_shape = 'Octagon'
        self.draw_regular_polygon(8, "Octagon")

    def setup_quiz_controls(self):
        # Setup for quiz panel
        quiz_panel = tk.Frame(self, bg='white', highlightbackground='black', highlightthickness=1)
        quiz_panel.pack_propagate(False)
        quiz_panel.pack(side=tk.TOP, fill=tk.X, expand=False, padx=10, pady=10, anchor='ne')
        quiz_panel.config(width=400, height=350)

        tk.Label(quiz_panel, text="Test Your Knowledge!", font=("Arial", 16, "bold")).pack(pady=(10, 20))

        self.question_label = tk.Label(quiz_panel, text="Click 'Start Quiz' to begin.", wraplength=200)
        self.question_label.pack(pady=10)

        self.options_var = tk.StringVar(value="")
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(quiz_panel, text=f"Option {i+1}", variable=self.options_var, value=f"Option {i+1}",command=self.enable_check_answer)
            rb.pack(anchor='w')
            self.radio_buttons.append(rb)
            rb.pack_forget() 

        self.start_quiz_btn = tk.Button(quiz_panel, text="Start Quiz", command=self.start_quiz, bg='cyan')
        self.start_quiz_btn.pack(pady=20)

        self.answer_btn = tk.Button(quiz_panel, text="Check Answer", command=self.check_answer, bg='cyan', state='disabled')
        self.answer_btn.pack(pady=10)
        self.answer_btn.pack_forget()  

        self.next_question_btn = tk.Button(quiz_panel, text="Next Question", command=self.generate_question, bg='cyan', state='disabled')
        self.next_question_btn.pack(pady=10)
        self.next_question_btn.pack_forget()  # Hide the 'Next Question' button initially

        self.question_pool = [
            {
                "question": "How many sides does a hexagon have?",
                "options": ["5", "6", "7", "8"],
                "answer": "6"
            },
            {
                "question": "What do you call a four-sided shape?",
                "options": ["Quadrilateral", "Pentagon", "Hexagon", "Circle"],
                "answer": "Quadrilateral"
            },
            {
                "question": "How many lines of symmetry does a square have?",
                "options": ["2", "4", "1", "0"],
                "answer": "4"
            },
            {
                "question": "What type of angle is smaller than a right angle?",
                "options": ["Obtuse", "Acute", "Straight", "Reflex"],
                "answer": "Acute"
            },
            {
                "question": "How many lines of symmetry does a regular pentagon have?",
                "options": ["5", "6", "4", "7"],
                "answer": "5"
            },
            {
                "question": "Which shape has all its sides of equal length and all angles equal?",
                "options": ["Rectangle", "Rhombus", "Oval", "Trapezoid"],
                "answer": "Rhombus"
            },
            {
                "question": "What type of angle measures exactly 180 degrees?",
                "options": ["Right", "Straight", "Acute", "Obtuse"],
                "answer": "Straight"
            },
            {
                "question": "What is the name of a four-sided figure with only one pair of parallel sides?",
                "options": ["Rectangle", "Trapezoid", "Square", "Rhombus"],
                "answer": "Trapezoid"
            },
            {
                "question": "How many sides does a decagon have?",
                "options": ["10", "12", "8", "9"],
                "answer": "10"
            },
            {
                "question": "What do you call a shape with curved sides?",
                "options": ["Polygon", "Circle", "Ellipse", "Curvagon"],
                "answer": "Ellipse"
            },
            {
                "question": "Which shape has no straight lines?",
                "options": ["Triangle", "Rectangle", "Circle", "Hexagon"],
                "answer": "Circle"
            },
            {
                "question": "What is a flat figure formed by connecting points with straight lines called?",
                "options": ["Polygon", "Curve", "Circle", "Arc"],
                "answer": "Polygon"
            },
            {
                "question": "How many lines of symmetry does an equilateral cross have?",
                "options": ["4", "0", "1", "2"],
                "answer": "4"
            },
            {
                "question": "Which shape can be made by placing two squares side by side?",
                "options": ["Octagon", "Rectangle", "Trapezoid", "Triangle"],
                "answer": "Rectangle"
            },
            {
                "question": "What shape is a traditional stop sign?",
                "options": ["Octagon", "Hexagon", "Circle", "Triangle"],
                "answer": "Octagon"
            },
            {
                "question": "How many vertices does an octagon have?",
                "options": ["8", "7", "6", "9"],
                "answer": "8"
            },
            {
                "question": "How many sides does a nonagon have?",
                "options": ["9", "8", "7", "10"],
                "answer": "9"
            },
            {
                "question": "What type of polygon is a five-sided shape?",
                "options": ["Pentagon", "Hexagon", "Heptagon", "Quadrilateral"],
                "answer": "Pentagon"
            },
            {
                "question": "Which shape has exactly one line of symmetry and five sides?",
                "options": ["Irregular pentagon", "Rectangle", "Circle", "Triangle"],
                "answer": "Irregular pentagon"
            },
            {
                "question": "How many sides does a regular dodecagon have?",
                "options": ["10", "12", "11", "13"],
                "answer": "12"
            },
            {
                "question": "What is the common name for a quadrilateral with two parallel sides?",
                "options": ["Parallelogram", "Rhombus", "Trapezoid", "Rectangle"],
                "answer": "Trapezoid"
            },
            {
                "question": "How many lines of symmetry does a regular hexagon have?",
                "options": ["6", "5", "4", "7"],
                "answer": "6"
            },
            {
                "question": "What type of quadrilateral has both pairs of opposite sides parallel?",
                "options": ["Square", "Rectangle", "Rhombus", "Trapezoid"],
                "answer": "Square"
            },
            {
                "question": "How many lines of symmetry does a parallelogram have?",
                "options": ["0", "1", "2", "4"],
                "answer": "0"
            },
            {
                "question": "Which shape has all sides the same length but does not necessarily have all angles equal?",
                "options": ["Square", "Rectangle", "Rhombus", "Parallelogram"],
                "answer": "Rhombus"
            },
            {
                "question": "Which shape has sides that are all the same length and every angle measuring 120 degrees?",
                "options": ["Equilateral triangle", "Regular pentagon", "Regular hexagon", "Square"],
                "answer": "Regular hexagon"
            },
            {
                "question": "What is a four-sided shape with opposite sides parallel called?",
                "options": ["Rectangle", "Square", "Parallelogram", "Circle"],
                "answer": "Parallelogram"
            },
            {
                "question": "How many corners does a pentagon have?",
                "options": ["5", "6", "7", "8"],
                "answer": "5"
            },
            {
                "question": "What do you call a closed shape with many sides?",
                "options": ["Polygon", "Polyhedron", "Ellipse", "Circle"],
                "answer": "Polygon"
            },
            {
                "question": "Which shape can be described as a stretched circle?",
                "options": ["Oval", "Triangle", "Square", "Rectangle"],
                "answer": "Oval"
            }
]

        self.question_index = -1

    
    def enable_check_answer(self):
        self.answer_btn.config(state='normal')
    
    def start_quiz(self):
        self.generate_question()
        self.start_quiz_btn.pack_forget()
    
    def generate_question(self):
        self.question_index = (self.question_index + 1) % len(self.question_pool)
        current_question = self.question_pool[self.question_index]
        
        self.question_label.config(text=current_question["question"])
        
        for i, rb in enumerate(self.radio_buttons):
            rb.config(text=current_question["options"][i], value=current_question["options"][i])
            rb.pack(anchor='w')
            rb.deselect()  

        self.options_var.set(None)
        
        self.answer_btn.config(state='normal')
        self.answer_btn.pack(pady=10)
        self.next_question_btn.pack_forget()

    def check_answer(self):
        selected_option = self.options_var.get()
        correct_answer = self.question_pool[self.question_index]["answer"]
        question_text = self.question_pool[self.question_index]["question"]

        if selected_option == correct_answer:
            self.question_label.config(text="Correct!")
            self.next_question_btn.config(state='normal') 
            self.next_question_btn.pack(pady=10)  
            self.answer_btn.pack_forget() 
        else:
            self.question_label.config(text=f"Incorrect! Try again.\n\n{question_text}")
            self.answer_btn.config(state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = ShapeGuide(master=root)
    root.mainloop()
