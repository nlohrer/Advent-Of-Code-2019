class IntcodeComputer:

    MAX_PARAMS = 3

    def __init__(self, program = None):
        self.program = program
        self.console_output = []
        self._pc = 0
        self._inp = None
        self.paused = False
        self.halted = False
        self.memory = None
        self._relative_base = 0
        self._paramater_mode = None

    def initialize_memory(self):
        if self.program is None:
            raise Exception('No program found - need to either initialize computer with a program, or add a program after initialization')
        op_list = self.program.split(',')
        op_list = {index: int(op) for index, op in enumerate(op_list)}
        self.memory = op_list

    def add(self, values):
        v1, v2, v3 = values
        if self._paramater_mode == '2':
            v3 += self._relative_base
        self.memory[v3] = v1 + v2

    def mult(self, values):
        v1, v2, v3 = values
        if self._paramater_mode == '2':
            v3 += self._relative_base
        self.memory[v3] = v1 * v2

    def save(self, values):
        value = values[0]
        if self._paramater_mode == '2':
            value += self._relative_base
        if not self._inp:
            self.paused = True
            return
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
        if self._paramater_mode == '2':
            v3 += self._relative_base
        self.memory[v3] = v1 < v2

    def equals(self, values):
        v1, v2, v3 = values
        if self._paramater_mode == '2':
            v3 += self._relative_base
        self.memory[v3] = v1 == v2

    def stop(self, values):
        assert False

    def output(self, values):
        value = values[0]
        self.console_output.append(value)

    def relative_base_offset(self, values):
        value = values[0]
        self._relative_base += value

    OPCODES = {1: (3, 2, add), 2: (3, 2, mult), 3: (1, 0, save), 4: (1, -1, output), 99: (0, 0, stop), 5: (2, -1, jump_if_true), 6: (2, -1, jump_if_false),
                7: (3, 2, less_than), 8: (3, 2, equals), 9: (1, -1, relative_base_offset)}

    def position_mode(self, param):
        return self.memory.setdefault(param, 0)

    def direct_mode(self, param):
        return param

    def relative_mode(self, param):
        return self.memory.setdefault(self._relative_base + param, 0)

    PARAM_MODES = {0: position_mode, 1: direct_mode, 2: relative_mode}

    def get_values(self, params, param_modes):
        values = []
        for param, param_mode in zip(params, param_modes):
            values.append(self.PARAM_MODES[param_mode](self, param))
        return tuple(values)

    def fix_param_modes(self, param_modes, param_num, write_address_index):
        len_needed = param_num - len(param_modes)
        new_param_modes = list(reversed(param_modes))
        new_param_modes += len_needed * [0]
        if write_address_index >= 0:
            self._paramater_mode = new_param_modes[write_address_index]
            new_param_modes[write_address_index] = 1
        return [int(param) for param in new_param_modes]


    def computation_cycle(self):
        while True:
            instruction = str(self.memory[self._pc])
            param_modes, opcode = instruction[:-2], int(instruction[-2:])
            if opcode == 99:
                self.halted = True
                break
            param_num, write_address_index, operation = self.OPCODES[opcode]
            param_modes = self.fix_param_modes(param_modes, param_num, write_address_index)
            params = [self.memory.setdefault(self._pc + index + 1, 0) for index in range(param_num)]
            values = self.get_values(params, param_modes)

            new_pc = operation(self, values)
            if self.paused:
                break

            if new_pc is None:
                self._pc += 1 + param_num
            else:
                self._pc = new_pc
        return self.halted

    def continue_computation(self, inp = None):
        if not self.paused:
            return self.compute(inp)
        self._inp = inp
        self.paused = False
        return self.computation_cycle()

    def compute(self, inp = None):
        self._pc = 0
        self._inp = inp
        self.paused = False
        self.halted = False
        self.initialize_memory()
        return self.computation_cycle()

if __name__ == '__main__':
    data = '1002,4,3,4,33'
    computer = IntcodeComputer(data)
    computer.compute([4])
    print(computer.memory)
