import numpy as np


def read_data(inputfile):
     data = np.loadtxt(inputfile,dtype=float).T
     return data

def solve_part_one(input_file_name="input.txt"):
    data = read_data(input_file_name)
    data = np.sort(data,axis = 1)
    print(data)
    vals = data[1] - data[0]
    return np.sum(abs(vals))
    
def solve_part_two(input_file_name="input.txt"):
    data = read_data(input_file_name)
    total = 0
    for elem in data[0]:
        total += elem * np.sum(data[1] == elem)
    return total

if __name__ == '__main__':
    print(solve_part_one())
    print(solve_part_two())