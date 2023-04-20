# find all traversed points for a given set
def input_to_point_set(path):
    path = path.split(',')
    points = set()
    current_pos = (0, 0)
    for section in path:
        direction, distance = section[0], int(section[1:])
        new_points, current_pos = trace_section(direction, distance, current_pos)
        points |= new_points
    return points
    
def trace_section(direction, distance, current_pos):

    x_pos, y_pos = current_pos

    if direction in ('L', 'R'):
        if direction == 'L':
            sign = -1
        else:
            sign = 1
        new_points = {(x_pos + x * sign, y_pos) for x in range(1, distance + 1)}
        new_pos = (x_pos + distance * sign, y_pos)
            
    if direction in ('D', 'U'):
        if direction == 'D':
            sign = -1
        else:
            sign = 1
        new_points = {(x_pos, y_pos + y * sign) for y in range(1, distance + 1)}
        new_pos = (x_pos, y_pos + distance * sign)

    return new_points, new_pos

def get_lowest_distance(data):
    path1, path2 = input_to_paths(data)
    points1, points2 = input_to_point_set(path1), input_to_point_set(path2)
    intersections = points1 & points2
    distances = {abs(x) + abs(y) for (x, y) in intersections}
    return min(distances)

def input_to_paths(data):
    if data[-1] == '\n':
        data = data[:-1]
    path1, path2 = data.split('\n')
    return path1, path2

def tests():
    test_input1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83'
    test_input2 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7\n'
    assert get_lowest_distance(test_input1) == 159
    assert get_lowest_distance(test_input2) == 135

if __name__ == '__main__':
    tests()
    with open('input', 'r') as data:
        data = data.read()
    result = get_lowest_distance(data)
    print(result)
