string = "hello launchschool"

reverse_generator = (string[i] for i in range(len(string) - 1, -1, -1))

for char in reverse_generator:
    print(char)
