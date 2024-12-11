class Stone:
    def __init__(self,value,blinks):
        self.value = value
        self.blinks = blinks
        self.other_values = []

    def blink(self):
        if self.value == 0:
            newvalue = 1
        elif len(str(self.value)) % 2 == 0:
            characters = str(self.value)
            newvalue = int(characters[0:int(len(characters)/2)])
            self.other_values.append(Stone(int(characters[int(len(characters)/2):]), self.blinks + 1))
        else:
            newvalue = self.value * 2024
        self.value = newvalue
        self.blinks += 1



def solve_part_one(input_file_name="input.txt"):

    for line in open(input_file_name,'r'):
        stones = [Stone(int(num),0) for num in line.split(' ') if num.strip() != '']

    value = 0
    for s in stones:
        while s.blinks < 25:
            s.blink()
        for x in s.other_values:
            stones.append(x)
        value += 1
    print(value)
    # for s in stones:
    #     print(s.value)

def solve_part_two(input_file_name="input.txt"):

    for line in open(input_file_name,'r'):
        stones = [Stone(int(num),0) for num in line.split(' ') if num.strip() != '']

    value = 0
    for s in stones:
        while s.blinks < 75:
            s.blink()
        for x in s.other_values:
            stones.append(x)
        value += 1
    print(value)
    # for s in stones:
    #     print(s.value)

if __name__ == '__main__':
    print(solve_part_one())
    print(solve_part_two())
