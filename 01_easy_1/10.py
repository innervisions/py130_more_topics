def input_generator():
    while True:
        string = input("Enter a string: ")
        if string == "stop":
            break
        yield string


for string in input_generator():
    print(string)
