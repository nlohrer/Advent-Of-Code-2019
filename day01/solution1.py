def compute_fuel(module):
    fuel = module // 3 - 2
    return fuel

def tests():
    assert compute_fuel(12) == 2
    assert compute_fuel(14) == 2
    assert compute_fuel(1969) == 654
    assert compute_fuel(100756) == 33583

if __name__ == '__main__':
    tests()
    with open('input', 'r') as data:
        modules = data.read().split()
        modules = (int(module) for module in modules)
    total = sum(map(compute_fuel, modules))
    print(total)
