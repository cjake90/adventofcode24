import re



class Day7:
    def __init__(self):
        self.part1 = 0
        self.solutions = []
        self.inputs = []
        self.possible_operators = ['*', '+']
        with open('input.txt', 'r') as f:
            for i, line in enumerate(f.readlines()):
                self.inputs.append([])
                temp = re.split(r':',line)
                self.solutions.append(int(temp[0]))
                items = re.split(r'\s+',(temp[1].lstrip().replace('\n','')))
                for item in items:
                    self.inputs[i].append(item)

    def try_operators(self, solution, inputs):
        result = 0
        for op in self.possible_operators:
            result = eval(str(inputs[0])+op+inputs[1])
            if(len(inputs) == 2):
                if int(result)==solution:
                    return True
            else:
                if self.try_operators(solution, [str(result)] + inputs[2:]):
                    return True
        return False
        

    def parse_list(self):
        for i in range(len(self.solutions)):
            if self.try_operators(self.solutions[i],self.inputs[i]):
                self.part1 += self.solutions[i]
            else:
                continue

if __name__ == '__main__':
    day7 = Day7()
    day7.parse_list()

    print(f'part1 = {day7.part1}')
