import numpy as np

class Datablock:
    def __init__(self,runlen,id,start):
        self.length = runlen
        self.id = id
        self.start = start   
    
    def calc_block_value(self):
        #     Value can be worked out by the following polynomial halved.
        #     (s-l)(s-l-1)
        #     ls + ls - s +l^2-l -s
        #     2ls - 2s -l + l^2
        if self.id < 0:
            return 0
        self.start -=1
        self.length += 1
        val = ((self.start * self.length)*(self.start + self.length - 1)  - (self.start * (self.start - 1)))/2
        val = (self.start*self.length - self.start) + ((self.length*self.length - self.length)/2)
        self.length -= 1
        self.start +=1
        return val * self.id

    def copy(self):
        newblock = Datablock(self.length,self.id,self.start)
        return newblock

def solve_part_one(input_file_name="input.txt"):
    
    disk = []
    
    #readin
    run_len = 0
    cur_id = 0
    next_is_empty = False
    start_loc = 0

    for line in open(input_file_name,'r'):
        for char in line:
            if not next_is_empty:
                disk.append(Datablock(int(char),cur_id,start_loc))
                cur_id += 1
            else:
                disk.append(Datablock(int(char),-1,start_loc))
            next_is_empty = not next_is_empty
            start_loc += run_len

    newdisk = []
    left_index = 0
    right_index = len(disk)-1
    length_of_new_disk = 0

    while True:
        if disk[left_index].id >= 0:
            newdisk.append(disk[left_index].copy())
            newdisk[-1].start = length_of_new_disk
            length_of_new_disk += newdisk[-1].length
            left_index += 1
        else:
            while disk[right_index].id < 0:
                right_index -= 1
            if right_index <= left_index:
                break
            #Now we need to push into the left side.
            #Check how much the left side has available
            space_available = disk[left_index].length
            if space_available >= disk[right_index].length:
                disk[left_index].length -= disk[right_index].length
                newdisk.append(disk[right_index].copy())
                newdisk[-1].start = length_of_new_disk
                if space_available == disk[right_index].length:
                    left_index += 1
                right_index -= 1
                length_of_new_disk += newdisk[-1].length
            else:
                newdisk.append(disk[right_index].copy())
                newdisk[-1].length = disk[left_index].length
                newdisk[-1].start = length_of_new_disk
                disk[right_index].length -= disk[left_index].length

                left_index += 1
                length_of_new_disk += newdisk[-1].length     

    value = 0
    for data in newdisk:
        value += data.calc_block_value()
    return value



        
        

        
def solve_part_two(input_file_name="input.txt"):
    return ""

if __name__ == '__main__':
    print(solve_part_one())
    # print(solve_part_two())