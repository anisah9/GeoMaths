import unittest
from shape import ShapeTool
from angle import AngleTool
from coordinate import CoordinateTool

class TestModuleInitialization(unittest.TestCase):
    def test_module_init(self):
        try:
            shape_tool = ShapeTool()
            angle_tool = AngleTool()
            coordinate_tool = CoordinateTool()
        except Exception as e:
            self.fail(f"Module initialization failed: {e}")

if __name__ == '__main__':
    unittest.main()































# /////////////////////

# import unittest
# from tkinter import Tk
# from unittest.mock import Mock
# from main import MainApp, WelcomePage, GeometryTool, AngleTool, CoordinateTool

# class TestMainApp(unittest.TestCase):
#     def setUp(self):
#         self.app = MainApp()

#     def test_show_frame_shapes(self):
#         self.app.show_frame(GeometryTool)
#         selected_frame = self.app.notebook.winfo_children()[self.app.notebook.index("current")]
#         self.assertIsInstance(selected_frame, GeometryTool)

#     def test_show_frame_angles(self):
#         self.app.show_frame(AngleTool)
#         selected_frame = self.app.notebook.winfo_children()[self.app.notebook.index("current")]
#         self.assertIsInstance(selected_frame, AngleTool)

#     def test_show_frame_coordinates(self):
#         self.app.show_frame(CoordinateTool)
#         selected_frame = self.app.notebook.winfo_children()[self.app.notebook.index("current")]
#         self.assertIsInstance(selected_frame, CoordinateTool)

# class TestWelcomePage(unittest.TestCase):
#     def setUp(self):
#         self.root = Tk()
#         self.controller = Mock()
#         self.welcome_page = WelcomePage(self.root, self.controller)

#     def test_show_shapes(self):
#         self.welcome_page.show_shapes()
#         self.controller.show_frame.assert_called_with(GeometryTool)

#     def test_show_angles(self):
#         self.welcome_page.show_angles()
#         self.controller.show_frame.assert_called_with(AngleTool)

#     def test_show_coordinates(self):
#         self.welcome_page.show_coordinates()
#         self.controller.show_frame.assert_called_with(CoordinateTool)

# if __name__ == '__main__':
#     unittest.main()


 

