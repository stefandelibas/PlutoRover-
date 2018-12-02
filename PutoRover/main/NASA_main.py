
from main.rover import Rover
from main.obstacles import Obstacles

def main():
    obstacles = Obstacles("C:\\Users\\Stefan-PC\\Documents\\GitHub\\PlutoRover-\\PutoRover\\obstacles.txt")
    rover = Rover(0, 0, 'N', 100, 100, obstacles.get_coordonates())
    obstacles = Obstacles("C:\\Users\\Stefan-PC\\Documents\\GitHub\\PlutoRover-\\PutoRover\\obstacles.txt")
    commands = readCommands("C:\\Users\\Stefan-PC\\Documents\\GitHub\\PlutoRover-\\PutoRover\\commands.txt")
    for c in commands:
        if c == "F":
            rover.forward()
        elif c == "R":
            rover.right()
        elif c == "B":
            rover.backward()
        elif c == "L":
            rover.left()
    print(str(rover))


def readCommands(path):
    commands = []
    f = open(path)
    line = f.readline()
    while line:
        elems = line.strip().strip(" ")
        for e in elems:
            commands.append(e)
        line = f.readline()
    f.close()
    return commands


if __name__ == '__main__':
    main()