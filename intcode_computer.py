class IntcodeComputer:

    PARAM_MODES = {0: (lambda param, memory: memory[param]), 1: (lambda param, memory: param)}
    MAX_PARAMS = 3

    def __init__(self, program = None):
        self.program = program
        self.console_output = []
        self._pc = 0

    def initialize_memory(self):
        if self.program is None:
            raise Exception('No program found - need to either initialize computer with a program, or add a program after initialization')
        op_list = self.program.split(',')    
        op_list = [int(op) for op in op_list]
        self.memory = op_list

    def add(self, values):
        v1, v2, v3 = values
        self.memory[v3] = v1 + v2

    def mult(self, values):
        v1, v2, v3 = values
        self.memory[v3] = v1 * v2

    def save(self, values):
        value = values[0]
        inp = self._inp.pop()
        self.memory[value] = inp

    def jump_if_true(self, values):
        v1, v2 = values
        if v1:
            return v2

    def jump_if_false(self, values):
        v1, v2 = values
        if not v1:
            return v2

    def less_than(self, values):
        v1, v2, v3 = values
        self.memory[v3] = int(v1 < v2)

    def equals(self, values):
        v1, v2, v3 = values
        self.memory[v3] = int(v1 == v2)

    def stop(self, values):
        assert False

    def output(self, values):
        value = values[0]
        self.console_output.append(value)

    OPCODES = {1: (3, 2, add), 2: (3, 2, mult), 3: (1, 0, save), 4: (1, -1, output), 99: (0, 0, stop), 5: (2, -1, jump_if_true), 6: (2, -1, jump_if_false), 7: (3, 2, less_than), 8: (3, 2, equals)}

    def get_values(self, params, param_modes):
        values = []
        for param, param_mode in zip(params, param_modes):
            values.append(self.PARAM_MODES[param_mode](param, self.memory))
        return tuple(values)

    def fix_param_modes(self, param_modes, param_num, write_address_index):
        len_needed = param_num - len(param_modes)
        new_param_modes = list(reversed(param_modes))
        new_param_modes += len_needed * [0]
        if write_address_index >= 0:
            new_param_modes[write_address_index] = 1
        return [int(param) for param in new_param_modes]

    def compute(self, inp = None):
        self._pc = 0
        self._inp = inp
        self.initialize_memory()
        while True:
            instruction = str(self.memory[self._pc])
            param_modes, opcode = instruction[:-2], int(instruction[-2:])
            if opcode == 99:
                return self.console_output
            param_num, write_address_index, operation = self.OPCODES[opcode]
            param_modes = self.fix_param_modes(param_modes, param_num, write_address_index)
            params = self.memory[self._pc+1 : self._pc+param_num + 1]
            values = self.get_values(params, param_modes)

            new_pc = operation(self, values)
            if new_pc is None:
                self._pc += 1 + param_num
            else:
                self._pc = new_pc

if __name__ == '__main__':
    data = '1002,4,3,4,33'
    computer = IntcodeComputer(data)
    computer.compute([4])
    print(computer.memory)
