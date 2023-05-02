import sys
sys.path.append("..")

import intcode_computer as ic

if __name__ == '__main__':
    with open('input', 'r') as data:
        program = data.read()
        program = program.split(',')
        program = ','.join([program[0]] + ['12', '2'] + program[3:])
    computer = ic.IntcodeComputer(program = program)
    computer.compute()
    print(computer.memory[0])
