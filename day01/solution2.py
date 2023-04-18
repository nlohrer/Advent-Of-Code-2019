def compute_fuel(module):
    fuel = module // 3 - 2
    if fuel <= 0:
        return 0

    return compute_fuel(fuel) + fuel

def tests():
    assert compute_fuel(12) == 2
    assert compute_fuel(14) == 2
    assert compute_fuel(1969) == 966
    assert compute_fuel(100756) == 50346

if __name__ == '__main__':
    tests()
    with open('input', 'r') as data:
        modules = data.read().split()
        modules = (int(module) for module in modules)
    total = sum(map(compute_fuel, modules))
    print(total)
