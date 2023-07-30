import sys # one
sys.path.append('..') # two 
from common import load_input # three
from solution1 import get_maximal_asteroids_seen, build_coordinates # FOUR
from math import gcd
from numpy import sign


def tests():
    test_input = load_input(file_name="test_input").split("\n\n")[-1]
    
    test_vaporization_indices = [0, 1, 2, 9, 19, 49, 99, 198, 199, 200, 298]
    test_positions = [(11,12), (12,1),
    (12,2), (12,8), (16,0), (16,9), (10,16),
        (9,6), (8,2), (10,9), (11,1)]
    
    vaporization_order = list(get_vaporization_order(test_input))
    
    for test_tuple in zip(test_vaporization_indices, test_positions):
        vaporization_index, coordinates = test_tuple
        assert vaporization_order[vaporization_index] == coordinates


def get_vaporization_order(input_map):
    laser_base = get_maximal_asteroids_seen(input_map)[1]
    asteroids = build_coordinates(input_map)
    
    asteroids_by_slope = polar_coordinates_to_base(asteroids, laser_base)
    
    sorted_slopes = list(asteroids_by_slope.keys())
    sorted_slopes.remove("inf")
    sorted_slopes.sort(key=compare_slopes, reverse=True)
    
    positive_slopes = sorted_slopes.copy()
    negative_slopes = sorted_slopes    
    
    while True:
        empty_slopes = []
        
        slope = "inf"
        
        slope_asteroids = asteroids_by_slope[slope]
            
        try:
            distance_factors = slope_asteroids["negative_asteroids"]
            next_distance_factor = distance_factors.pop()
            
            yield slope_to_euclidean(slope_asteroids["base_vector"], 
            next_distance_factor, laser_base)
            
        except:
            pass                  
        
        for slope in positive_slopes:
            slope_asteroids = asteroids_by_slope[slope]
            
            try:
                distance_factors = slope_asteroids["positive_asteroids"]
                next_distance_factor = distance_factors.pop(0)
            except:
                empty_slopes.append(slope)
                continue         
        
            yield slope_to_euclidean(slope_asteroids["base_vector"], 
                next_distance_factor, laser_base)
                
        for slope in empty_slopes:
            positive_slopes.remove(slope)
            
        slope = "inf"
        
        slope_asteroids = asteroids_by_slope[slope]
            
        try:
            distance_factors = slope_asteroids["positive_asteroids"]
            next_distance_factor = distance_factors.pop(0)
            
            yield slope_to_euclidean(slope_asteroids["base_vector"], 
            next_distance_factor, laser_base)
            
        except:
            pass      

        empty_slopes = []
            
        for slope in negative_slopes:
            slope_asteroids = asteroids_by_slope[slope]
            
            try:
                distance_factors = slope_asteroids["negative_asteroids"]
                next_distance_factor = distance_factors.pop()
            except:
                empty_slopes.append(slope)
                continue          
            
            yield slope_to_euclidean(slope_asteroids["base_vector"], 
                next_distance_factor, laser_base)
                
        for slope in empty_slopes:
            negative_slopes.remove(slope)
    
        infinite_slope_asteroids = asteroids_by_slope["inf"]["positive_asteroids"] + asteroids_by_slope["inf"]["negative_asteroids"]
            
        if positive_slopes + negative_slopes + infinite_slope_asteroids == []:
            break
    
    yield None


def slope_to_euclidean(base_vector, distance_factor, positional_vector):
    base_x, base_y = base_vector
    positional_x, positional_y = positional_vector

    return (base_x * distance_factor + positional_x, 
        base_y * distance_factor + positional_y)


def compare_slopes(slope):
    if slope == "inf":
        return 0

    return -2 ** slope


def polar_coordinates_to_base(asteroid_positions, base_coordinates):
    base_x, base_y = base_coordinates
    asteroid_positions.remove(base_coordinates)
    
    asteroids_by_slope = dict()

    for x, y in asteroid_positions:
        x_distance = x - base_x
        y_distance = y - base_y
        
        slope, base_vector, distance_factor = get_polar_directions(x_distance, y_distance)
        
        slope_asteroids = asteroids_by_slope.setdefault(slope, dict())
        
        add_asteroid(slope_asteroids, distance_factor)
        slope_asteroids.setdefault("base_vector", base_vector)
  
    list(map(sort_slope_asteroids, asteroids_by_slope.values())) # Be in awe for spagghut
  
    return asteroids_by_slope
    
    
def sort_slope_asteroids(slope_asteroids):
    asteroid_list_keys = ["positive_asteroids", "negative_asteroids"]
    
    for key in asteroid_list_keys:
        try:
            slope_asteroids[key].sort()
        except KeyError:
            pass
    
    
def get_polar_directions(x_distance, y_distance):
    if x_distance == 0:
        slope = "inf"
        base_vector = (0, 1)
        distance_factor = y_distance
    
    else:
        divisor = gcd(y_distance, x_distance)
        direction_signum = sign(x_distance)
        
        distance_factor = divisor * direction_signum
        
        base_vector = (x_distance // distance_factor,
            y_distance // distance_factor)
        
        slope = base_vector[1] / base_vector[0]
    
    return slope, base_vector, distance_factor


def add_asteroid(slope_asteroids, distance_factor):
    asteroid_list_key = "positive_asteroids"

    if distance_factor < 0:
        asteroid_list_key = "negative_asteroids"

    slope_asteroids.setdefault(asteroid_list_key, []).append(distance_factor)
    

if __name__ == "__main__":
    tests()
    
    aaa100th_vaporized_asteroid = list(get_vaporization_order(load_input()))[199]
    
    print(aaa100th_vaporized_asteroid[0] * 100 + aaa100th_vaporized_asteroid[1])
