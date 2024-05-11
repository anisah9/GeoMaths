import unittest
from unittest.mock import MagicMock
from reflect_shape_tab import Turtle

class TestTurtle(unittest.TestCase):

    def setUp(self):
        self.canvas_mock = MagicMock()
        self.output_display_mock = MagicMock()
        self.turtle = Turtle(self.canvas_mock, self.output_display_mock)

    def test_move_forward(self):
        start_pos = (0, 0)
        end_pos = (50, 0)
        self.turtle.turtle.pos = MagicMock(side_effect=[start_pos, end_pos])
        self.turtle.move_forward(50)
        self.assertEqual(self.turtle.vertices, [start_pos, end_pos])

    def test_turn_right(self):
        start_heading = 0
        end_heading = 90
        self.turtle.turtle.heading = MagicMock(side_effect=[start_heading, end_heading])
        self.turtle.turn_right(90)
        self.assertEqual(self.turtle.turtle.heading(), 90)

    def test_goto(self):
        self.turtle.goto(100, 100)
        self.assertEqual(self.turtle.vertices, [(100, 100)])
        self.assertTrue(self.turtle.turtle.penup.called)
        self.assertTrue(self.turtle.turtle.pendown.called)

    def test_reflect_shape_x(self):
        self.turtle.vertices = [(0, 0), (0, 50), (50, 50)]
        self.turtle.reflect_shape('x')
        self.assertEqual(self.turtle.vertices, [(0, 0), (0, -50), (50, -50)])

    def test_reflect_shape_y(self):
        self.turtle.vertices = [(0, 0), (0, 50), (50, 50)]
        self.turtle.reflect_shape('y')
        self.assertEqual(self.turtle.vertices, [(0, 0), (0, 50), (-50, 50)])

    def test_simplify_vertices(self):
        vertices = [(0, 0), (0, 0), (50, 50), (50, 50)]
        simplified = self.turtle.simplify_vertices(vertices)
        self.assertEqual(simplified, [(0, 0), (50, 50)])

    def test_compare_shapes(self):
        expected_vertices = [(0, 0), (50, 0), (50, 50)]
        actual_vertices = [(0, 0), (50, 0), (50, 50)]
        self.assertTrue(self.turtle.compare_shapes(expected_vertices, actual_vertices))

if __name__ == '__main__':
    unittest.main()
