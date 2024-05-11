# import unittest
# from unittest.mock import patch
# import tkinter as tk
# from tkinter import scrolledtext
# from tkinter import messagebox
# from PIL import Image

# from draw_shape_tab import DrawShapeTab 


# class TestTurtle(unittest.TestCase):
#     def setUp(self):
#         self.root = tk.Tk()
#         self.app = DrawShapeTab(self.root)

#     def tearDown(self):
#         self.root.destroy()

#     def test_move_forward(self):
#         self.app.turtle.move_forward(50)  # Move forward by 50 units
#         # Assert the turtle's position after moving
#         self.assertEqual(self.app.turtle.turtle.position(), (50, 0))

#     def test_turn_right(self):
#         initial_heading = self.app.turtle.turtle.heading()
#         self.app.turtle.turn_right(90)  # Turn right by 90 degrees
#         # Calculate the expected heading after turning right
#         expected_heading = (initial_heading + 90) % 360
#         # Assert the turtle's heading after turning
#         self.assertEqual(self.app.turtle.turtle.heading(), expected_heading)


#     def test_goto(self):
#         self.app.turtle.goto(100, -100)  # Move to coordinates (100, -100)
#         # Assert the turtle's position after moving
#         self.assertEqual(self.app.turtle.turtle.position(), (100, -100))


# class TestDrawShapeTab(unittest.TestCase):
#     def setUp(self):
#         self.root = tk.Tk()
#         self.app = DrawShapeTab(self.root)

#     def tearDown(self):
#         self.root.destroy()

#     def test_execute_code(self):
#         # Test executing valid code
#         code = "forward 50\nright 90\nforward 50\nright 90\nforward 50\nright 90\nforward 50"
#         expected_result = "Code executed successfully."
#         self.assertEqual(self.app.turtle.execute_code(code), expected_result)

#         # Test executing invalid code
#         invalid_code = "invalid_command 50"
#         error_message = "Invalid command or wrong number of arguments: invalid_command 50"
#         self.assertIn(error_message, self.app.turtle.execute_code(invalid_code))


# if __name__ == '__main__':
#     unittest.main()


import unittest
from unittest.mock import MagicMock
from tkinter import Tk
from draw_shape_tab import Turtle, DrawShapeTab

class TestTurtle(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.canvas = MagicMock()
        self.output_display = MagicMock()
        self.turtle = Turtle(self.canvas, self.output_display)

    def tearDown(self):
        self.root.destroy()


class TestDrawShapeTab(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.app = DrawShapeTab(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_show_forward(self):
        self.app.show_forward()
        # Assert that the turtle's position changed appropriately

    def test_show_right(self):
        self.app.show_right()
        # Assert that the turtle's position changed appropriately

    def test_show_goto(self):
        self.app.show_goto()
        # Assert that the turtle's position changed appropriately

    def test_draw_square(self):
        self.app.draw_square()
        # Assert that the square was drawn correctly

    def test_draw_circle(self):
        self.app.draw_circle()
        # Assert that the circle was drawn correctly

    def test_draw_rectangle(self):
        self.app.draw_rectangle()
        # Assert that the rectangle was drawn correctly

    def test_draw_triangle(self):
        self.app.draw_triangle()
        # Assert that the triangle was drawn correctly

    def test_draw_parallelogram(self):
        self.app.draw_parallelogram()
        # Assert that the parallelogram was drawn correctly

    def test_draw_rhombus(self):
        self.app.draw_rhombus()
        # Assert that the rhombus was drawn correctly

    def test_draw_trapezium(self):
        self.app.draw_trapezium()
        # Assert that the trapezium was drawn correctly

    def test_draw_pentagon(self):
        self.app.draw_pentagon()
        # Assert that the pentagon was drawn correctly

    def test_draw_hexagon(self):
        self.app.draw_hexagon()
        # Assert that the hexagon was drawn correctly

    def test_draw_heptagon(self):
        self.app.draw_heptagon()
        # Assert that the heptagon was drawn correctly

    def test_draw_octagon(self):
        self.app.draw_octagon()
        # Assert that the octagon was drawn correctly

    def test_clear_instructions(self):
        # Set some instructions
        self.app.instructions.set("Some instructions")
        # Clear the instructions
        self.app.clear_instructions()
        # Check if instructions are cleared
        self.assertEqual(self.app.instructions.get(), "")
        # Check if the code editor is also cleared
        self.assertEqual(self.app.code_editor.get("1.0", "end-1c"), "")

    def test_clear_drawing(self):
        # Call the clear drawing method
        self.app.clear_drawing()
        # Assert that the turtle canvas has been cleared
        # You can do this by checking if the turtle's position is at the origin (0, 0)

    

if __name__ == "__main__":
    unittest.main()
