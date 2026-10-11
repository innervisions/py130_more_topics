def count_up():
    for idx in range(1, 6):
        yield idx
        
for num in count_up():
    print(num)
