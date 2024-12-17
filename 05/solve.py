import numpy as np


def read_in_data(input_file_name="input.txt"):
    page_dict = {}
    page_list = []

    for line in open(input_file_name,'r'):
        if line.find('|') > -1:
            bef,aft = (int(x) for x in line.split('|'))

            if bef in page_dict:
                page_dict[bef].append(aft)
            else:
                page_dict[bef] = [aft]
        
        if line.find(',') > -1:
            page_list.append([ int(x.strip()) for x in line.split(',') ])
        
    return page_list,page_dict


def solve_part_one(input_file_name="input.txt"):
    value = 0
    pages, dic = read_in_data(input_file_name)

    for l in pages:
        valid = True
        for i,val in enumerate(l):
            if val in dic:
                for pages_before in l[0:i]:
                    if pages_before in dic[val]:
                        valid = False
                        break
        if valid:
            value += l[int(len(l)/2)]


    return value

   


    
def solve_part_two(input_file_name="input.txt"):
    value = 0

    return value        

    


if __name__ == '__main__':
    print(solve_part_one())
    print(solve_part_two())