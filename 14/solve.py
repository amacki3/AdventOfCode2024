import numpy as np
import re

X_LIM = 101
Y_LIM = 103

class Robot:

    def __init__(self,string_description):
        matches = re.findall("=(\-*\d+),(\-*\d+)",string_description)
        self.pos = np.array([int(x) for x in matches[0]])
        self.vel = np.array([int(x) for x in matches[1]])

    def move(self,time):
        self.pos = self.pos + (self.vel * time)
        self.pos[0] = self.pos[0] % X_LIM
        self.pos[1] = self.pos[1] % Y_LIM


def read_in_data(input_file_name="input.txt"):
    robots = []
    for line in open(input_file_name,'r'):
        robots.append(Robot(line))      
    return robots


def solve_part_one(input_file_name="input.txt"):
    value = 0
    robots = read_in_data(input_file_name)
    quadrants = [0,0,0,0]
    for r in robots: 
        r.move(100)
        if r.pos[0] < (X_LIM-1)/2:
            if r.pos[1] < (Y_LIM-1)/2:
                quadrants[0] += 1
            elif r.pos[1] > (Y_LIM-1)/2:
                quadrants[1] += 1
        elif r.pos[0] > (X_LIM-1)/2:
            if r.pos[1] < (Y_LIM-1)/2:
                quadrants[2] += 1
            elif r.pos[1] > (Y_LIM-1)/2:
                quadrants[3] += 1
    value = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

    return value

   


    
def solve_part_two(input_file_name="input.txt"):
    value = 0

    return value        

    


if __name__ == '__main__':
    print(solve_part_one())
    print(solve_part_two())