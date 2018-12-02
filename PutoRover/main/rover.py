

class Rover:
    def __init__(self, x=0, y=0, direction='N', grid_width=100, grid_height=100):
        self.n = grid_height
        self.m = grid_width
        self.x = x
        self.y = y
        self.d = direction

    def set_position(self, x, y, d):
        # whenever we want to reinitialize the position of the rover(typically in testing)
        self.x = x
        self.y = y
        self.d = d

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getD(self):
        return self.d

    def backward(self):
        pass

    def forward(self):
        pass

    def right(self):
        pass

    def left(self):
        pass

