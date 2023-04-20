PARAM_MODES = {0: (lambda param, memory: memory[param]), 1: (lambda param, memory: param)}
MAX_PARAMS = 3
console_output = []

def add(values, memory):
    v1, v2, v3 = values
    memory[v3] = v1 + v2

def mult(values, memory):
    v1, v2, v3 = values
    memory[v3] = v1 * v2

def save(values, memory):
    value = values[0]
    inp = 1
    memory[value] = inp # input, may vary later

def stop(values, memory):
    assert False

def output(values, memory):
    value = values[0]
    console_output.append(value)

OPCODES = {1: (3, 2, add), 2: (3, 2, mult), 3: (1, 0, save), 4: (1, -1, output), 99: (0, 0, stop)}

def intcode_to_list(intcode):
    op_list = intcode.split(',')    
    op_list = [int(op) for op in op_list]
    return op_list

def get_values(params, param_modes, memory):
    values = []
    for i, param in enumerate(params):
        param_mode = param_modes[i]
        values.append(PARAM_MODES[param_mode](param, memory))
    return tuple(values)

def fix_param_modes(param_modes, param_num, write_address_index):
    len_needed = param_num - len(param_modes)
    new_param_modes = list(reversed(param_modes))
    new_param_modes += len_needed * [0]
    if write_address_index >= 0:
        new_param_modes[write_address_index] = 1
    return [int(param) for param in new_param_modes]

def compute(memory):
    pc = 0
    while True:
        instruction = str(memory[pc])
        param_modes, opcode = instruction[:-2], int(instruction[-2:])
        if opcode == 99:
            return console_output
        param_num, write_address_index, operation = OPCODES[opcode]
        param_modes = fix_param_modes(param_modes, param_num, write_address_index)
        params = memory[pc+1 : pc+param_num + 1]
        values = get_values(params, param_modes, memory)
        operation(values, memory)
        pc += 1 + param_num

if __name__ == '__main__':
    data = '1002,4,3,4,33'
    intcode = intcode_to_list(data)
    compute(intcode)
