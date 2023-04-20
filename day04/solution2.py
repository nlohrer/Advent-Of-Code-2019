from solution1 import get_args


def validate(password):
    numbers = list(map(int, str(password)))
    contains_pair = False
    
    i = 0
    
    while i < 5:
        if numbers[i] > numbers[i + 1]:
                return False
     
        size_of_group = size_of_group_of_adjacents(numbers, i)
        
        if size_of_group > 1:
            i += size_of_group - 1
        else:
            i += 1
        
        contains_pair |= size_of_group == 2 
        
    return contains_pair


def size_of_group_of_adjacents(numbers, i):
    size = 1
    
    while numbers[i] == numbers[i + 1]:
        size += 1
        i += 1
        
        if i == 5:
            break
        
    return size


def tests():
    assert validate(112233)
    assert not validate(123444)
    assert validate(111122)
    assert not validate(113244)
    assert not validate(111111)
    assert not validate(599899)


if __name__ == "__main__":
    tests()
    
    lower_range, upper_range = get_args()
    count = sum(map(validate, range(lower_range, upper_range + 1)))

    print(count)