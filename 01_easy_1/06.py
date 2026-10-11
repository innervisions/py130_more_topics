from functools import reduce

strings = ["hello", "darkness", "my", "old", "friend"]
result = reduce(lambda str1, str2: str1 + str2, strings)

print(result)
