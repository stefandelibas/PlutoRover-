import unittest
from main.rover import Rover

class MyTestCase(unittest.TestCase):
    def test_forward(self):
        self.test_forward_north()
        self.test_forward_east()

    def test_forward_north(self):
        rover = Rover(5, 5, 'N', 10, 10)
        rover.forward()
        self.assertEqual(rover.getX(), 5)
        self.assertEqual(rover.getY(), 6)

    def test_forward_east(self):
        rover = Rover(5, 5, 'E', 10, 10)
        rover.forward()
        self.assertEqual(rover.getX(), 6)
        self.assertEqual(rover.getY(), 5)

    def test_forward_south(self):
        rover = Rover(5, 5, 'S', 10, 10)
        rover.forward()
        self.assertEqual(rover.getX(), 5)
        self.assertEqual(rover.getY(), 4)

    def test_forward_west(self):
        rover = Rover(5, 5, 'W', 10, 10)
        rover.forward()
        self.assertEqual(rover.getX(), 4)
        self.assertEqual(rover.getY(), 5)


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
