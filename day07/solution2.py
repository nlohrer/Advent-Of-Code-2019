import sys
sys.path.append('..')
import intcode_computer as ic
import solution1 as s1
from itertools import permutations

def test_phase_setting(program, phase_setting_sequence):
    computers = dict()
    for i, phase_setting in zip(range(5), phase_setting_sequence):
        computer = ic.IntcodeComputer(program)
        computer.compute([phase_setting])
        computers[f'icc{i}'] = computer

    output_last = 0
    while not computers['icc4'].halted:
        for i in range(5):
          current_computer = computers[f'icc{i}']
          current_computer.continue_computation([output_last])
          output_last = current_computer.console_output.pop()
    return output_last

def find_optimal_thrust(program):
    return max(map(lambda permutation: test_phase_setting(program, permutation), permutations(range(5, 10))))
    

def tests():
    test_program1, test_sequence1 = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5', [9, 8, 7, 6, 5]
    test_program2, test_sequence2 = '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10', [9, 7, 8, 5, 6]
    assert test_phase_setting(test_program1, test_sequence1) == 139629729
    assert test_phase_setting(test_program2, test_sequence2) == 18216

if __name__ == '__main__':
    tests()
    with open('input', 'r') as data:
        program = data.read()
    max_output = find_optimal_thrust(program)
    print(max_output)