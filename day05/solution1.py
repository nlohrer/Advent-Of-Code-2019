import sys
sys.path.append("..")

import intcode_computer as ic

if __name__ == '__main__':
    with open('input', 'r') as data:
        program = data.read()
    computer = ic.IntcodeComputer(program = program)
    computer.compute([1])
    print(computer.console_output[-1])
