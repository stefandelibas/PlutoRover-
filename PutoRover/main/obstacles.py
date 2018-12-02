

class Obstacles:
    def __init__(self, path):
        self.coords = []
        self.readObstacles(path)

    def get_coordonates(self):
        return self.coords

    def readObstacles(self, path):
        f = open(path)
        line = f.readline()
        while line:
            elems = line.strip().split(" ")
            self.coords.append([int(elems[0]), int(elems[1])])
            line = f.readline()
        f.close()

    def printMap(self, n):
        matr = []
        for i in range(n):
            matr.append([0 for x in range(n)])
        for coord in self.coords:
            matr[coord[0]][coord[1]] = 1

        for line in matr:
            for e in line:
                print(e, end=' ')
            print()
