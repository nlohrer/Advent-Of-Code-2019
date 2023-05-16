from solution1 import iterate_over_layers
import functools as ft


def stack_layers(front_layer, back_layer):
    combined_layer = map(stack_pixels, zip(front_layer, back_layer))
    return combined_layer
    

def stack_pixels(pixels):
    front_pixel, back_pixel = pixels
    if front_pixel == "2":
        return back_pixel
        
    return front_pixel
    
    
def decode_image(data, width, height):
    return "".join(list(ft.reduce(stack_layers, iterate_over_layers(data, width, height))))


def print_image(image_data, width, height):
    i = 0

    for row in range(height):
        print(image_data[i:i+width])
        i += width
    
    
def tests():
    assert decode_image("0222112222120000", 2, 2) == "0110"
    
    
if __name__ == "__main__":
    tests()

    with open("input", "r") as data:
        data = data.read().split()[0]
        
    image_data = decode_image(data, 25, 6)
    print_image(image_data, 25, 6)
