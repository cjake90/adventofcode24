import numpy as np




class Day8:
    def __init__(self):
        self.part1 = 0
        self.antennas = {}
        self.map = {}
        self.nodes = {}
        with open('input.txt','r') as f:
            for i, line in enumerate(f.readlines()):
                for j, char in enumerate(line):
                    if char == '\n':
                        continue
                    self.map[(i,j)] = char
                    if char.isalnum():
                        if char not in self.antennas:
                            self.antennas[char] = []
                        self.antennas[char].append([i,j])
    def add_antinodes(self):
        for antenna in self.antennas:
            for loc1 in self.antennas[antenna]:
                for loc2 in self.antennas[antenna]:
                    #skip if it's loc1
                    if loc1 != loc2:
                        node = np.array(loc1) + (np.array(loc1) - np.array(loc2))
                        a = (int(node[0]),int(node[1]))
                        if (a) in self.map:
                            if self.map[a] == '.':
                                self.map[a] = '#'
                            if (a) not in self.nodes:
                                self.nodes[a] = '#'





if __name__ == '__main__':
    day8 = Day8()
    day8.add_antinodes()
    day8.part1 = len(day8.nodes)
    print(f'part1 = {day8.part1}')