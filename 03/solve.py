import numpy as np
import re

def determine_value_in_string(data):
    value = 0
    matches = re.findall('mul\((\d*)\,(\d*)\)',data)
    for x in matches:
        value += int(x[0])*int(x[1])
    return value


def solve_part_one(input_file_name="input.txt"):
    

    with open(input_file_name,'r') as f:
        data = f.read()

    return determine_value_in_string(data)

    
def solve_part_two(input_file_name="input.txt"):
    value = 0
    with open(input_file_name,'r') as f:
        data = f.read()

    notEnd = True
    enabled = True
    while notEnd:
        ops = ['do()',"don't()"]
        next_onoff_operator = data.find(ops[1] if enabled else ops[0])
        if next_onoff_operator == -1:
            notEnd = False
        if enabled:
            value += determine_value_in_string(data[0:next_onoff_operator])
        data = data[next_onoff_operator+len(ops[1] if enabled else ops[0]):]
        enabled = not enabled

    return value        

    


if __name__ == '__main__':
    print(solve_part_one())
    print(solve_part_two())