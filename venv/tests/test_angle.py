import unittest
import tkinter as tk
from tkinter import Canvas
from unittest.mock import patch
from angle import AngleTool

class TestAngleTool(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.angle_tool = AngleTool(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_draw_triangle(self):
        with patch("tkinter.messagebox.showinfo") as mock_showinfo:
            self.angle_tool.draw_triangle()
            mock_showinfo.assert_called_with("Draw Triangle", "You've drawn a triangle! A triangle is a polygon with three edges and three vertices.")

    def test_meet_at_a_point(self):
        with patch("tkinter.messagebox.showinfo") as mock_showinfo:
            self.angle_tool.meet_at_a_point()
            mock_showinfo.assert_called_with("Meet at a Point", "The angles meet at a point. The sum of angles around a point is 360 degrees.")

    def test_on_a_straight_line(self):
        with patch("tkinter.messagebox.showinfo") as mock_showinfo:
            self.angle_tool.on_a_straight_line()
            mock_showinfo.assert_called_with("On a Straight Line", "The angles are on a straight line. The sum of angles on a straight line is 180 degrees.")

    def test_vertically_opposite(self):
        with patch("tkinter.messagebox.showinfo") as mock_showinfo:
            self.angle_tool.vertically_opposite()
            mock_showinfo.assert_called_with("Vertically Opposite", "The angles are vertically opposite. Vertically opposite angles are equal and add up to 360 degrees.")

if __name__ == '__main__':
    unittest.main()
