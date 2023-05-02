# NOTE: You have to hard-code an input value of 5 into the intcode_computer.py file

import sys
sys.path.append("..")

import intcode_computer as ic

if __name__ == '__main__':
    with open('input', 'r') as data:
        program = data.read()
        
    computer = ic.IntcodeComputer(program)
    computer.compute([5])
    
    memory = computer.memory
    print(memory[-1])
