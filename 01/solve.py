import numpy as np

def solve_part_one(input_file_name="input.txt"):
    data = np.loadtxt(input_file_name,dtype=float).T
    data = np.sort(data,axis = 1)
    print(data)
    vals = data[1] - data[0]
    return np.sum(abs(vals))
    

if __name__ == '__main__':
    print(solve_part_one())