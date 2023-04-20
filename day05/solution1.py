import sys
sys.path.append("..")

import intcode_computer as ic

if __name__ == '__main__':
    with open('input', 'r') as data:
        intcode = ic.intcode_to_list(data.read())
    logs = ic.compute(intcode)
    print(logs[-1])
