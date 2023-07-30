import sys
sys.path.append('..')
import intcode_computer as ic
from common import load_input

def paint_panels(robot):
    direction = 0    #north
    position = (0, 0)
    panels = dict()
    while not robot.halted:
        color = panels.setdefault(position, 0)
        robot.continue_computation([color])
        new_color, turning_direction = robot.console_output[-2:]
        panels[position] = new_color
        direction = turn(direction, turning_direction)
        position = step(position, direction)
    return panels

def step(position, direction):
    step_vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dx, dy = step_vectors[direction]
    x, y = position
    return (x + dx, y + dy)

def turn(direction, turning_direction):
    # direction: ^ == 0, > == 1, v == 2, < == 3
    # turning_direction: 0 == l, 1 == r

    signum = -((-1) ** turning_direction)
    direction = (direction + signum) % 4
    return direction

def tests():
    assert turn(0, 0) == 3
    assert turn(3, 1) == 0
    assert turn(2, 0) == 1
    assert turn(1, 1) == 2

if __name__ == "__main__":
    tests()
    program = load_input()

    robot = ic.IntcodeComputer(program)
    panels = paint_panels(robot)
    print(len(panels.keys()))
