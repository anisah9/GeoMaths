import unittest
from unittest.mock import Mock
from tkinter import Tk
from coordinate import CoordinateTool, Turtle

class TestTurtle(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.canvas = Mock()
        self.output_display = Mock()
        self.turtle = Turtle(self.canvas, self.output_display)

    def test_execute_code_forward(self):
        code = "forward 50"
        self.turtle.execute_code(code)
        current_position = self.turtle.get_current_position()
        self.assertEqual(current_position, (50, 0))


class TestCoordinateTool(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.coordinate_tool = CoordinateTool(self.root)

    def test_execute_code(self):
        code = "forward 50"
        self.coordinate_tool.code_editor.insert("1.0", code)
        self.coordinate_tool.execute_code()


if __name__ == '__main__':
    unittest.main()



