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
    def __init__(self, map, init_pos):
        self.map = map
        self.dir = Direction.UP
        self.pos = [int(init_pos[0][0]),int(init_pos[0][1])]
        self.out = False
        self.stuck = False

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

def turn_guard_right(dir):
    if dir == Direction.UP:
        return Direction.RIGHT
    elif dir == Direction.RIGHT:
        return Direction.DOWN
    elif dir == Direction.DOWN:
        return Direction.LEFT
    elif dir == Direction.LEFT:
        return Direction.UP

def check_if_out(new_pos):
    if 0 > new_pos[0] or 0 > new_pos[1] or guard_map.map.shape[0]-1 < new_pos[0] or guard_map.map.shape[1]-1 < new_pos[1]:
        guard_map.out = True
        return True
    else:
        return False

def mark_pos(turned, current_mark):
    if current_mark=="#" or current_mark =="0":
        print(f'error! found {current_mark} at {guard_map.pos}')
    if turned:
        guard_map.map[guard_map.pos[0],guard_map.pos[1]] = "+"
    else:
        if Direction.UP == guard_map.dir or Direction.DOWN == guard_map.dir:
            if "-" == current_mark:
                guard_map.map[guard_map.pos[0],guard_map.pos[1]] = "+"
            else:    
                guard_map.map[guard_map.pos[0],guard_map.pos[1]] = "|"
        else:
            if "|" == current_mark:
                guard_map.map[guard_map.pos[0],guard_map.pos[1]] = "+"
            else:    
                guard_map.map[guard_map.pos[0],guard_map.pos[1]] = "-"



def move_guard():
    new_pos = find_next_coord(guard_map.dir, [guard_map.pos[0],guard_map.pos[1]])
    turned = False
    current_mark = guard_map.map[guard_map.pos[0],guard_map.pos[1]]
    
    #first check if the guard left the map
    if check_if_out(new_pos):
        mark_pos(turned, current_mark)
        return True
    else:
        #check if the next position hits an obstacle
        new_mark = guard_map.map[new_pos[0],new_pos[1]]
        if new_mark == "#" or new_mark == "0":
            # check if the guard has already turned here in the past
            if(current_mark == '+'):
                guard_map.stuck = True
                return True
            
            # if so, turn right
            guard_map.dir = turn_guard_right(guard_map.dir)
            turned = True
            new_pos = find_next_coord(guard_map.dir, [guard_map.pos[0],guard_map.pos[1]])
            new_mark = guard_map.map[new_pos[0],new_pos[1]]
            #check again if the guard left the map 
            if check_if_out(new_pos):
                mark_pos(turned, current_mark)
                return True
            
            #turn again if necessary - initial error in solution
            if new_mark == "#" or new_mark == "0":
                guard_map.dir = turn_guard_right(guard_map.dir)
                turned = True
                new_pos = find_next_coord(guard_map.dir, [guard_map.pos[0],guard_map.pos[1]])
        mark_pos(turned, current_mark)
        guard_map.pos = new_pos
        
        #guard_map.map[guard_map.pos[0],guard_map.pos[1]] = "^"
        return False


    

with open("input.txt") as file:
    global guard_map
    stuck_count = 0
    
    #read the map into an array
    init_map = []
    for line in file:
        init_map.append(list(line.replace("\n","")))
    init_pos = np.argwhere(np.array(init_map) == '^')
    #Initialize the Guard_Map
    guard_map = Guard_Map(np.array(init_map), init_pos)

    while not guard_map.out:
        move_guard()

    print('initial map is:')
    print(guard_map.map)
    unique_pos = np.argwhere(np.logical_or(np.logical_or(guard_map.map=="|", guard_map.map=="-"), guard_map.map=="+"))
    
    print(f'part 1 solution: {len(unique_pos)}')
    #print(unique_pos)
    for pos in unique_pos:
        # do nothing, can't place object in initial pos
        if not (pos == init_pos[0]).all():
            # re-initialize but add a new object
            guard_map = Guard_Map(np.array(init_map), init_pos)
            guard_map.map[pos[0],pos[1]] = '0'
            # loop until stuck or out of the map
            while not (guard_map.stuck or guard_map.out):
                move_guard()
            # if out of the map, increase stuck count
            if(True == guard_map.stuck):
                stuck_count+=1

    print(f'part 2 solution: {stuck_count} scenarios')