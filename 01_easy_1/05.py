lst = [1, "hello", None, [2], None]
result = list(filter(lambda value: value is not None, lst))

print(result)
