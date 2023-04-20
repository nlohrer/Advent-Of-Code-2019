import argparse

def validate(password):
    numbers = list(map(int, str(password)))
    contains_pair = False
    
    for i in range(5):
        if numbers[i] > numbers[i + 1]:
            return False
            
        if not contains_pair:
            contains_pair = numbers[i] == numbers[i + 1]    
    
    return contains_pair
    
    
def tests():
    assert validate(111111)
    assert not validate(223450)
    assert not validate(123789)
    
    
if __name__ == "__main__":
    tests()
    
    count = sum(map(validate, range(183564, 657474 + 1)))
    
    print(count)
        