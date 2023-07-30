import sys
sys.path.append('..')
import intcode_computer as ic
from common import load_input
from solution1 import paint_panels

def get_border_values(panels):
    x_coordinates = list(map(lambda coords: coords[0], panels.keys()))
    y_coordinates = list(map(lambda coords: coords[1], panels.keys()))
    x_min, x_max = min(x_coordinates), max(x_coordinates)
    y_min, y_max = min(y_coordinates), max(y_coordinates)
    return x_min, x_max, y_min, y_max

def paint_registration_ID(panels):
    x_min, x_max, y_min, y_max = get_border_values(panels)
    color_coding = ('.', '#')
    for y in range(y_max, y_min - 1, -1):
        for x in range(x_min, x_max + 1):
            symbol = color_coding[panels.setdefault((x, y), 0)]
            print(symbol, end = '')
        print()

if __name__ == '__main__':
    program = load_input()
    robot = ic.IntcodeComputer(program)

    panels = paint_panels(robot, 1)
    paint_registration_ID(panels)
