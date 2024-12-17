import numpy as np

class Computer:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c 
        self.out = []
        self._instruction_pointer = 0

    def __repr__(self):
        return f"Register A: {self.a}\nRegister B: {self.b}\nRegister C: {self.c}\n\nOutput {','.join(str(i) for i in self.out)}\n"

    def _determine_combo_operand(self,operand):
        if operand < 4: 
            return operand
        else:
            if operand == 4:
                return self.a
            elif operand == 5:
                return self.b
            elif operand == 6:
                return self.c
            else:
                raise ValueError("Invalid operand!", operand)

    def _adv(self,operand):
        value = int(self.a / (2**self._determine_combo_operand(operand)))
        self.a = value
        self._instruction_pointer += 2
    
    def _bxl(self,operand):
        self.b = self.b ^ operand
        self._instruction_pointer += 2

    def _bst(self,operand):
        self.b = self._determine_combo_operand(operand) % 8
        self._instruction_pointer += 2

    def _jnz(self,operand):
        if self.a == 0:
            self._instruction_pointer += 2
        else:
            self._instruction_pointer = operand

    def _bxc(self,operand):
        self.b = self.b ^ self.c
        self._instruction_pointer += 2

    def _out(self,operand):
        self.out.append(self._determine_combo_operand(operand) % 8) 
        self._instruction_pointer += 2

    def _bdv(self,operand):
        value = int(self.a / (2**self._determine_combo_operand(operand)))
        self.b = value
        self._instruction_pointer += 2

    def _cdv(self,operand):
        value = int(self.a / (2**self._determine_combo_operand(operand)))
        self.c = value
        self._instruction_pointer += 2 

    instr_list = [_adv,_bxl,_bst,_jnz,_bxc,_out,_bdv,_cdv]

    def _carry_out_instruction(self,instr,operand):
        Computer.instr_list[instr](self,operand)

    def run(self,prog):
        halted = False
        while not halted:
            self._carry_out_instruction(prog[self._instruction_pointer],prog[self._instruction_pointer+1])
            if self._instruction_pointer >= len(prog):
                halted = True

        return self.out

    def reset(self):
        self.out = []
        self._instruction_pointer = 0        

def read_data(input):
    a = []
    b = []
    c = []
    prog = []
    for lines in  open(input,'r'):
        if lines.find('A') > -1:
            a = int(lines.split()[-1])
        elif lines.find('B') > -1:
            b = int(lines.split()[-1])
        elif lines.find('C') > -1:
            c =int(lines.split()[-1])
        elif lines.find('Program') > -1:
            prog = [int (x) for x in lines.strip('Program: ').split(',')]

    reg = Computer(a,b,c)
    return reg,prog


def solve_part_one(input_file_name="input.txt"):
    value = []

    reg,instr = read_data(input_file_name)
    
    reg.run(instr)
    return reg


    
def solve_part_two(input_file_name="input.txt"):
    total = 0
    return total

if __name__ == '__main__':
    print(solve_part_one())
    print(solve_part_two())