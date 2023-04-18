def intcode_to_list(intcode):
    op_list = intcode.split(',')    
    op_list = [int(op) for op in op_list]
    return op_list


def compute(memory):
    pc = 0

    while True:
        opcode = memory[pc]
        
        if opcode == 99:
            return memory
        
        adr1, adr2, adr3 = memory[pc+1:pc+4]
        
        val1, val2 = memory[adr1], memory[adr2]
        memory[adr3] = operate(opcode, val1, val2)
        
        pc += 4
        
        
def operate(opcode, val1, val2):
    if opcode == 1:
        return val1 + val2
        
    elif opcode == 2:
        return val1 * val2
        
    else:
        raise ValueError('Unknown opcode.')


def list_comparison(list1, list2):
    length = len(list1)

    if length != len(list2):
        return False
        
    for i in range(length):
        if list1[i] != list2[i]:
            return False
            
    return True


def tests():
    assert compute([1,0,0,0,99]) == [2,0,0,0,99]
    assert compute([2,3,0,3,99]) == [2,3,0,6,99]
    assert compute([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
    assert compute([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]
  

if __name__ == '__main__':
    tests()

    with open('input', 'r') as data:
        intcode = data.read().replace('\n', '')
  
    memory = intcode_to_list(intcode)
    memory[1:3] = [12, 2]
    
    resulting_memory = compute(memory)
    print(resulting_memory[0])
    