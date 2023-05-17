from numpy import sign
from fractions import Fraction

def build_coordinates(input_map):
    asteroid_positions = set()
    
    for y, row in enumerate(input_map.split()):
        for x, entry in enumerate(row):
            if entry == "#":
                asteroid_positions.add((x,y))
    
    return asteroid_positions
    

def number_of_detected_asteroids(asteroid_positions):
    for base_asteroid in asteroid_positions:
        target_directions = get_detection_directions(base_asteroid, asteroid_positions)
        
        yield len(target_directions) - 1


def get_detection_directions(base_asteroid, asteroid_positions):   
        base_x, base_y = base_asteroid
        detection_directions = set()
        
        for target_asteroid in asteroid_positions:
            target_x, target_y = target_asteroid
            
            x_distance = target_x - base_x
            y_distance = target_y - base_y
            
            detection_directions.add(get_direction(x_distance, y_distance))
            
        return detection_directions
            
            
def get_direction(x_distance, y_distance):
    if x_distance == 0:
        return (0, sign(y_distance))
        
    x_sign = sign(x_distance)
    direction_fraction = Fraction(y_distance, x_distance)
    
    reduced_direction = (direction_fraction.denominator * x_sign, 
        direction_fraction.numerator)
    
    return reduced_direction
    

def get_maximal_asteroids_seen(input_map):
    asteroid_positions = build_coordinates(input_map)
    
    return max(number_of_detected_asteroids(asteroid_positions))


def tests():
    with open("test_input", "r") as test_data:
        test_inputs = test_data.read().split("\n\n")
        
    test_outputs = [8, 33, 35, 41, 210]
        
    for input, output in zip(test_inputs, test_outputs):        
        assert get_maximal_asteroids_seen(input) == output
        
        
if __name__ == "__main__":
    tests()
    
    with open("input", "r") as data:
        input_map = data.read()
        
    print(get_maximal_asteroids_seen(input_map))
    