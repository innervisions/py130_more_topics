nested_lists = [[1, 2, 3], [4, 5], [6]]
flat_list = list((num
                  for sublist in nested_lists
                  for num in sublist))
print(flat_list)
