import numpy as np




class Day8:
    def __init__(self):
        self.part1 = 0
        self.antennas = {}
        self.map = {}
        self.nodes = {}
        # assuming a square
        self.map_dim = 0
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
                    #last value won't have \n so will be correct
                    #self.map_dim[1] = j + 1
                self.map_dim = i + 1

    # Returns out_of_bound status
    def mark_node(self, node):
        if (node) in self.map:
            if self.map[node] == '.':
                self.map[node] = '#'
            if (node) not in self.nodes:
                self.nodes[node] = '#'
            return False
        else:
            return True

    def add_antinodes(self):
        for antenna_type in self.antennas:
            antenna_list = self.antennas[antenna_type]
            for loc1 in antenna_list:
                for loc2 in antenna_list:
                    #skip if it's the loc1 antenna
                    if loc1 != loc2:
                        #find the distance between antennas
                        diff = np.array(loc1) - np.array(loc2)
                        
                        change_vector = diff
                        # and here I figured that:
                        ##### antinode occurs at any grid position exactly
                        ##### in line with at least two antennas of the same frequency 
                        # meant that I needed to simplify the vector first
                        #
                        # #check if vector can be simplified
                        # if 0 == abs(diff[0]+diff[1]) % 2:
                        #     if abs(diff[0]) > abs(diff[1]):
                        #         change_vector = (diff / abs(diff[1])).astype(int)
                        #     else:
                        #         # if same, doesn't matter
                        #         change_vector = (diff / abs(diff[0])).astype(int)
                        #     print(change_vector)
                        # else:
                        #     change_vector = diff
                        
                        #cycle upwards
                        for j in range(self.map_dim):
                            test_point = (np.array(loc1) + j * change_vector).tolist()
                            if self.mark_node((test_point[0],test_point[1])):
                                # break if outside the dict
                                break
                        
                        #cycle downwards
                        for j in range(self.map_dim):
                            test_point = (np.array(loc1) - j * change_vector).tolist()
                            if self.mark_node((test_point[0],test_point[1])):
                                # break if outside the dict
                                break

if __name__ == '__main__':
    day8 = Day8()
    day8.add_antinodes()
    day8.part2 = len(day8.nodes)
    print(f'part2 = {day8.part2}')