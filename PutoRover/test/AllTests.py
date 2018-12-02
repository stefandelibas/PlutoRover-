import unittest
from main.rover import Rover

class MyTestCase(unittest.TestCase):
    def test_forward(self):
        pass

    def test_backward(self):
        pass

    def test_left(self):
        self.assertEqual(True, True)

    def test_right(self):
        pass

    def test_line_horizontal(self):
        # run along a line and when it reaches a certain edge(left or right)
        # it should go on the opposite side of the grid
        pass

    def test_line_vertical(self):
        # run along a line and when it reaches a certain edge(left or right)
        # it should go on the opposite side of the grid
        pass

    def test_corner(self):
        # from a corner go in all directions and test if they are correct
        pass

    def test_encounter_obstacle(self):
        pass


if __name__ == '__main__':
    unittest.main()
