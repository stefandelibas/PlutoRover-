import unittest
from main.rover import Rover,Direction
class MyTestCase(unittest.TestCase):

    def test_forward(self):
        self.d = Direction()
        self.test_forward_north()
        self.test_forward_east()
        self.test_forward_south()
        self.test_forward_west()

    def test_forward_north(self):
        self.d = Direction()
        rover = Rover(5, 5, self.d.get("N"), 10, 10)
        rover.forward()
        self.assertEqual(rover.getX(), 5)
        self.assertEqual(rover.getY(), 6)

    def test_forward_east(self):
        self.d = Direction()
        rover = Rover(5, 5, self.d.get("E"), 10, 10)
        rover.forward()
        self.assertEqual(rover.getX(), 6)
        self.assertEqual(rover.getY(), 5)

    def test_forward_south(self):
        self.d = Direction()
        rover = Rover(5, 5, self.d.get("S"), 10, 10)
        rover.forward()
        self.assertEqual(rover.getX(), 5)
        self.assertEqual(rover.getY(), 4)

    def test_forward_west(self):
        self.d = Direction()
        rover = Rover(5, 5, self.d.get("W"), 10, 10)
        rover.forward()
        self.assertEqual(rover.getX(), 4)
        self.assertEqual(rover.getY(), 5)

    def test_backward_north(self):
        self.d = Direction()
        rover = Rover(5, 5, self.d.get("N"), 10, 10)
        rover.backward()
        self.assertEqual(rover.getX(), 5)
        self.assertEqual(rover.getY(), 4)

    def test_backward_east(self):
        self.d = Direction()
        rover = Rover(5, 5, self.d.get("E"), 10, 10)
        rover.backward()
        self.assertEqual(rover.getX(), 4)
        self.assertEqual(rover.getY(), 5)

    def test_backward_south(self):
        self.d = Direction()
        rover = Rover(5, 5, self.d.get("S"), 10, 10)
        rover.backward()
        self.assertEqual(rover.getX(), 5)
        self.assertEqual(rover.getY(),6)

    def test_backward_west(self):
        self.d = Direction()
        rover = Rover(5, 5, self.d.get("W"), 10, 10)
        rover.backward()
        self.assertEqual(rover.getX(), 6)
        self.assertEqual(rover.getY(), 5)

    def test_left_north(self):
        self.d = Direction()
        rover = Rover(5, 5, self.d.get("N"), 10, 10)
        rover.left()
        self.assertEqual(rover.getD(), "W")
        self.assertEqual(rover.getY(), 5)
        self.assertEqual(rover.getX(), 5)

    def test_left_east(self):
        self.d = Direction()
        rover = Rover(5, 5, self.d.get("E"), 10, 10)
        rover.left()
        self.assertEqual(rover.getD(), "N")
        self.assertEqual(rover.getY(), 5)
        self.assertEqual(rover.getX(), 5)

    def test_left_south(self):
        self.d = Direction()
        rover = Rover(5, 5, self.d.get("S"), 10, 10)
        rover.left()
        self.assertEqual(rover.getD(), "E")
        self.assertEqual(rover.getY(), 5)
        self.assertEqual(rover.getX(), 5)

    def test_left_west(self):
        self.d = Direction()
        rover = Rover(5, 5, self.d.get("W"), 10, 10)
        rover.left()
        self.assertEqual(rover.getD(), "S")
        self.assertEqual(rover.getY(), 5)
        self.assertEqual(rover.getX(), 5)

    def test_right_north(self):
        self.d = Direction()
        rover = Rover(5, 5, self.d.get("N"), 10, 10)
        rover.right()
        self.assertEqual(rover.getD(), "E")
        self.assertEqual(rover.getY(), 5)
        self.assertEqual(rover.getX(), 5)

    def test_right_east(self):
        self.d = Direction()
        rover = Rover(5, 5, self.d.get("E"), 10, 10)
        rover.right()
        self.assertEqual(rover.getD(), "S")
        self.assertEqual(rover.getY(), 5)
        self.assertEqual(rover.getX(), 5)

    def test_right_south(self):
        self.d = Direction()
        rover = Rover(5, 5, self.d.get("S"), 10, 10)
        rover.right()
        self.assertEqual(rover.getD(), "W")
        self.assertEqual(rover.getY(), 5)
        self.assertEqual(rover.getX(), 5)

    def test_right_west(self):
        self.d = Direction()
        rover = Rover(5, 5, self.d.get("W"), 10, 10)
        rover.right()
        self.assertEqual(rover.getD(), "N")
        self.assertEqual(rover.getY(), 5)
        self.assertEqual(rover.getX(), 5)

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
