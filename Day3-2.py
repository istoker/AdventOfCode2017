from enum import Enum

class Direction(Enum):
    RIGHT = 1
    UP = 2
    LEFT = 3
    DOWN = 4

def next_direction(direc):
    pass
    
def main():
    data = {}
    x = {'cur': 1, 'min': 0, 'max': 0}
    y = {'cur': 1, 'min': 0, 'max': 0}
    direc = Direction.RIGHT
    current_number = 1
    data[(x['cur'], y['cur'])] = current_number
    goal_number = 325489
    while current_number < goal_number:
        pass
        

if __name__ == '__main__':
    main()