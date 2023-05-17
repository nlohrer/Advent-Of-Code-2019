import sys
sys.path.append('..')
import intcode_computer as ic

def tests():
    test_program1 = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
    test_program2 = '1102,34915192,34915192,7,4,7,99,0'
    test_program3 = '104,1125899906842624,99'
    test_computer = ic.IntcodeComputer()
    test_computer.program = test_program1
    test_computer.compute()
    assert test_computer.console_output == [int(a) for a in test_program1.split(',')]
    test_computer.program = test_program2
    test_computer.compute()
    assert test_computer.console_output[-1] == 1219070632396864
    test_computer.program = test_program3
    test_computer.compute()
    assert test_computer.console_output[-1] == 1125899906842624
    
if __name__ == '__main__':
    tests()
    with open('input', 'r') as data:
        program = data.read()
    computer = ic.IntcodeComputer(program = program)
    computer.compute([1])
    print(computer.console_output[-1])