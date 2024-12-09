from enum import Enum
import numpy as np
import re

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Guard_Map:
    turn_right_map = {Direction.UP:Direction.RIGHT, 
    Direction.RIGHT:Direction.DOWN, 
    Direction.DOWN: Direction.LEFT, 
    Direction.LEFT:Direction.UP}
    
    dir_vector = {Direction.UP:[-1,0],
    Direction.RIGHT:[0,1],
    Direction.DOWN:[1,0],
    Direction.LEFT:[0,-1]}

    def __init__(self, map):
        self.map = map
        self.dir = Direction.UP
        init_pos = np.where(self.map == '^')
        self.pos = [int(init_pos[0][0]),int(init_pos[1][0])]
        self.out = False

    def turn_guard_right(self):
        self.dir = self.turn_right_map[self.dir]

    def find_next_coord(self):
        self.new_pos = [self.pos[x] + self.dir_vector[self.dir][x]
                        for x in range(2)]
        return self.new_pos

    def check_if_out(self):
        if (0 > self.new_pos[0] or 
        0 > self.new_pos[1] or 
        self.map.shape[0]-1 < self.new_pos[0] or 
        self.map.shape[1]-1 < self.new_pos[1]):
            self.out = True
        return self.out

    def move_guard(self):
        self.find_next_coord()
        
        #first check if the guard left the map
        if self.check_if_out():
            return True
        else:
            #check if the next position hits an obstacle
            if self.map[self.new_pos[0],self.new_pos[1]] == "#":
                # if so, turn right
                self.turn_guard_right()
                self.find_next_coord()
            
                #check again if the guard left the map 
                if self.check_if_out():
                    return True
            self.pos = self.new_pos
            return False


class Day6:
    def __init__(self):
        self.map_in = []
        with open("input.txt") as file:
            for line in file:
                self.map_in.append(list(line.replace("\n","")))
        self.guard_map = Guard_Map(np.array(self.map_in))
    
    def guard_patrol(self):
        while not self.guard_map.out:
            self.guard_map.map[self.guard_map.pos[0],self.guard_map.pos[1]] = 'X'
            self.guard_map.move_guard()
        print(self.guard_map.map)
        self.part1 = np.count_nonzero(self.guard_map.map == "X")

if __name__ == '__main__':
    day6 = Day6()
    day6.guard_patrol()
    print(f'final unique move count = {day6.part1}')
    
