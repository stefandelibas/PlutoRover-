

class Rover:
    def __init__(self, x=0, y=0, direction='N', grid_width=100, grid_height=100):
        self.n = grid_height
        self.m = grid_width
        self.x = x
        self.y = y
        self.d = direction
        self.__dir = Direction()

    def set_position(self, x, y, d):
        # whenever we want to reinitialize the position of the rover(typically in testing)
        self.x = x
        self.y = y
        self.d = d

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getD(self):
        return self.d

    def backward(self):
        if self.d == self.__dir.get("N"):
            if self.y - 1 < 0:
                self.y = self.n
            else:
                self.y = self.y - 1
        elif self.d == self.__dir.get("E"):
            if self.x - 1 < 0:
                self.x = self.m
            else:
                self.x = self.x - 1
        elif self.d == self.__dir.get("S"):
            if self.y + 1 > self.n:
                self.y = 0
            else:
                self.y = self.y + 1
        elif self.d == self.__dir.get("W"):
            if self.x + 1 > self.m:
                self.x = 0
            else:
                self.x = self.x + 1

    def forward(self):
        if self.d == self.__dir.get("N"):
            if self.y + 1 > self.n:
                self.y = 0
            else:
                self.y = self.y + 1

        elif self.d == self.__dir.get("E"):
            if self.x + 1 > self.m:
                self.x = 0
            else:
                self.x = self.x + 1

        elif self.d == self.__dir.get("S"):
            if self.y - 1 < 0:
                self.y = self.n
            else:
                self.y = self.y - 1

        elif self.d == self.__dir.get("W"):
            if self.x - 1 < 0:
                self.x = self.m
            else:
                self.x = self.x - 1

    def right(self):
        if self.d == self.__dir.get("N"):
            self.d = "E"
        elif self.d == self.__dir.get("E"):
            self.d = "S"
        elif self.d == self.__dir.get("S"):
            self.d = "W"
        elif self.d == self.__dir.get("W"):
            self.d = "N"

    def left(self):
        if self.d == self.__dir.get("N"):
            self.d = "W"
        elif self.d == self.__dir.get("E"):
            self.d = "N"
        elif self.d == self.__dir.get("S"):
            self.d = "E"
        elif self.d == self.__dir.get("W"):
            self.d = "S"



class Direction:
    # this class will restrict the freedom of choosing other directions that the rover possible handle
    # as well it might be useful to provide a way of extending the direction our rover can go
    def __init__(self):
        self.d = {
            'N': "N",
            'S': "S",
            'E': "E",
            'W': "W",
        }

    def get(self, direction):
        return self.d[direction]

