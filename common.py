def load_input(file_name="input"):
    with open(file_name, "r") as data:
        data = data.read()
        
    if data[-1] == "\n":
        data = data[:-1]
        
    return data