import unittest
from tkinter import Tk
from unittest.mock import Mock
from shape import GeometryTool

class TestGeometryTool(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.geometry_tool = GeometryTool(self.root)

    def test_draw_square(self):
        self.geometry_tool.draw_square()
        instructions = self.geometry_tool.instructions.get()
        expected_instructions = "forward 50\nright 90\nforward 50\nright 90\nforward 50\nright 90\nforward 50"
        self.assertEqual(instructions, expected_instructions)

    def test_draw_circle(self):
        self.geometry_tool.draw_circle()
        instructions = self.geometry_tool.instructions.get()
        expected_instructions = "repeat 360 [forward 1\nright 1]"
        self.assertEqual(instructions, expected_instructions)

    def test_draw_rectangle(self):
        self.geometry_tool.draw_rectangle()
        instructions = self.geometry_tool.instructions.get()
        expected_instructions = "forward 100\nright 90\nforward 50\nright 90\nforward 100\nright 90\nforward 50"
        self.assertEqual(instructions, expected_instructions)

    def test_draw_triangle(self):
        self.geometry_tool.draw_triangle()
        instructions = self.geometry_tool.instructions.get()
        expected_instructions = "forward 100\nright 120\nforward 100\nright 120\nforward 100"
        self.assertEqual(instructions, expected_instructions)

    def test_draw_custom(self):
        self.geometry_tool.draw_custom()
        instructions = self.geometry_tool.instructions.get()
        expected_instructions = "# Try drawing your own shapes!\n# Use commands like move_forward, turn_right, etc.\n# Example: move_forward 50\nturn_right 90\nmove_forward 50"
        self.assertEqual(instructions, expected_instructions)

if __name__ == '__main__':
    unittest.main()
