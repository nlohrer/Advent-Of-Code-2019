from itertools import permutations
import sys
sys.path.append('..')

import intcode_computer as ic

def test_phase_setting(computer, phase_setting_sequence):
    inp = 0
    for phase_setting in phase_setting_sequence:
        computer.console_output = []
        computer.compute([inp, phase_setting])
        inp = computer.console_output[-1]
    return inp

def find_optimal_thrust(computer):
    return max(map(lambda permutation: test_phase_setting(computer, permutation), permutations(range(5))))

def tests():
    test_program1, test_sequence1 = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0', [4, 3, 2, 1, 0]
    test_program2, test_sequence2 = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0', [0, 1, 2, 3, 4]
    test_program3, test_sequence3 = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33, 1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0', [1, 0, 4, 3, 2]
    test_computer = ic.IntcodeComputer()
    test_computer.program = test_program1
    assert test_phase_setting(test_computer, test_sequence1) == 43210
    test_computer.program = test_program2
    assert test_phase_setting(test_computer, test_sequence2) == 54321
    test_computer.program = test_program3
    assert test_phase_setting(test_computer, test_sequence3) == 65210

if __name__ == '__main__':
    tests()
    with open('input', 'r') as data:
        program = data.read()
    computer = ic.IntcodeComputer(program)
    max_output = find_optimal_thrust(computer)
    print(max_output)
