from enum import Enum
import numpy as np
import re

# direction enumerations are:
# dir 0 = up
# dir 1 = right
# dir 2 = down
# dir 3 = left
class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Guard_Map:
    def __init__(self, map):
        self.map = map
        self.dir = Direction.UP
        init_pos = np.where(self.map == '^')
        self.pos = [int(init_pos[0][0]),int(init_pos[1][0])]
        self.out = False

def find_next_coord(dir, pos):
    if dir == Direction.UP:
        new_pos = [pos[0]-1, pos[1]]
    elif dir == Direction.RIGHT:
        new_pos = [pos[0], pos[1]+1]
    elif dir == Direction.DOWN:
        new_pos = [pos[0]+1, pos[1]]
    elif dir == Direction.LEFT:
        new_pos = [pos[0], pos[1]-1]
    return new_pos

def turn_guard_right():
    if guard_map.dir == Direction.UP:
        guard_map.dir = Direction.RIGHT
    elif guard_map.dir == Direction.RIGHT:
        guard_map.dir = Direction.DOWN
    elif guard_map.dir == Direction.DOWN:
        guard_map.dir = Direction.LEFT
    elif guard_map.dir == Direction.LEFT:
        guard_map.dir = Direction.UP

def check_if_out(new_pos):
    if 0 > new_pos[0] or 0 > new_pos[1] or guard_map.map.shape[0]-1 < new_pos[0] or guard_map.map.shape[1]-1 < new_pos[1]:
        guard_map.out = True
        return True
    else:
        return False


def move_guard():
    new_pos = find_next_coord(guard_map.dir, [guard_map.pos[0],guard_map.pos[1]])
    
    #first check if the guard left the map
    if check_if_out(new_pos):
        return True
    else:
        #check if the next position hits an obstacle
        if guard_map.map[new_pos[0],new_pos[1]] == "#":
            # if so, turn right
            turn_guard_right()
            new_pos = find_next_coord(guard_map.dir, [guard_map.pos[0],guard_map.pos[1]])
        
            #check again if the guard left the map 
            if check_if_out(new_pos):
                return True
        guard_map.pos = new_pos
        guard_map.map[guard_map.pos[0],guard_map.pos[1]] = "^"
        return False


    

with open("input.txt") as file:
    global guard_map
    move_count = 0

    #read the map into an array
    map_in = []
    for line in file:
        map_in.append(list(line.replace("\n","")))
    
    #Initialize the Guard_Map
    guard_map = Guard_Map(np.array(map_in))

    while not guard_map.out:
        guard_map.map[guard_map.pos[0],guard_map.pos[1]] = 'X'
        move_guard()
    print(guard_map.map)
    print(f'final unique move count = {np.count_nonzero(guard_map.map == "X")}')