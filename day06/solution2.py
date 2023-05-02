import solution1 as s1
import time


def compute_reverse_tree(orbits):
    reverse_tree = dict()
    
    for orbit in orbits:
        orbitee, orbiter = orbit
        
        reverse_tree[orbiter] = orbitee

    return reverse_tree


def get_reverse_tree_from_input(input):
    orbits = s1.parse_input(input)
    reverse_tree = compute_reverse_tree(orbits)
    
    return reverse_tree
    
    
def path_to_com(reverse_tree, node):
    if node == "COM":
        return set()
        
    return {node} | path_to_com(reverse_tree, reverse_tree[node])
    
    
def compute_shortest_route_reversed(reverse_tree):
    path_to_santa = path_to_com(reverse_tree, reverse_tree["SAN"])
    path_to_you = path_to_com(reverse_tree, reverse_tree["YOU"])
    
    orbit_hops_necessary = path_to_santa.symmetric_difference(path_to_you)
    
    return len(orbit_hops_necessary)


def get_tree_from_input(input):
    orbits = s1.parse_input(input)
    tree = s1.compute_orbit_tree(orbits)
    
    return tree


def path_from_node_to(tree, current, target):
    if current == target:        
        return set()
    
    if current not in tree:
        return None
    
    for child in tree[current]:
        possible_path = path_from_node_to(tree, child, target)
        
        if not possible_path is None:
            return {current} | possible_path
            
    return None


def compute_shortest_route(tree):
    path_to_santa = path_from_node_to(tree, "COM", "SAN")
    path_to_you = path_from_node_to(tree, "COM", "YOU")
    
    orbit_hops_necessary = path_to_santa.symmetric_difference(path_to_you)
    
    return len(orbit_hops_necessary)


def tests():
    test_input = """
    COM)B
    B)C
    C)D
    D)E
    E)F
    B)G
    G)H
    D)I
    E)J
    J)K
    K)L
    K)YOU
    I)SAN"""
    tree = get_tree_from_input(test_input)
    
    reverse_tree = get_reverse_tree_from_input(test_input)
    
    assert compute_shortest_route(tree) == 4
    assert compute_shortest_route_reversed(reverse_tree) == 4
    
    
if __name__ == "__main__":
    tests()

    with open("input", 'r') as data:
        data =  data.read()
            
    t = time.time()
    tree = get_tree_from_input(data)           
    number_of_hops = compute_shortest_route(tree)
    print(number_of_hops)
    print(time.time() - t)
    
    t = time.time()
    reverse_tree = get_reverse_tree_from_input(data)
    number_of_hops = compute_shortest_route_reversed(reverse_tree)
    print(number_of_hops)
    print(time.time() - t)
    