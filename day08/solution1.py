def iterate_over_layers(data, width, height):
    i = 0
    layer_size = width * height
    
    while i < len(data):
        yield data[i:i+layer_size]
        i += layer_size
   
   
def find_result(data, width, height):
    lowest_zero_count = width * height
    current_result = 0
    
    for layer in iterate_over_layers(data, width, height):
        zero_count = layer.count("0")
        
        if zero_count < lowest_zero_count:
            current_result = layer.count("1") * layer.count("2")
            lowest_zero_count = zero_count
            
    return current_result  
   
   
def tests():
    assert find_result("123456789012", 3, 2) == 1
   

if __name__ == "__main__":
    tests()
    
    with open("input", "r") as data:
        data = data.read().split()[0]
        
    print(find_result(data, 25, 6))
    