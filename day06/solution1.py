def parse_input(data):
    orbits = [orbit.split(')') for orbit in data.split()]
    
    return orbits
    

def compute_orbit_tree(orbits):
    tree = dict()
    
    for orbit in orbits:
        orbitee, orbiter = orbit
        
        tree.setdefault(orbitee, []).append(orbiter)

    return tree
    
    
def compute_checksum(tree, level, start):
    if start not in tree.keys():
        return level
        
    map_function = lambda child: compute_checksum(tree, level+1, child)

    checksum = 0
    
    for child in tree[start]:
        checksum += map_function(child)
    # checksum = sum(map(map_function, tree[start]))
    
    return checksum + level
    
    
def check_input(data):
    orbits = parse_input(data)
    tree = compute_orbit_tree(orbits)
    checksum = compute_checksum(tree, 0, 'COM')
    
    return checksum
    
    
def tests():
    test_input = """COM)B
        B)C
        C)D
        D)E
        E)F
        B)G
        G)H
        D)I
        E)J
        J)K
        K)L"""
        
    assert check_input(test_input) == 42
  
    
if __name__ == "__main__":
    tests()

    with open("input", 'r') as data:
        data =  data.read()
        
    checksum = check_input(data)
    print(checksum)
    
    
    