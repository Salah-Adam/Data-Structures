def square_list_items(list):
    new_list = []
    for i in list:
        new_list.append(i ** 2)
    return new_list

print(square_list_items([1, 2, 4, 5]))
print(square_list_items([11, 100, -2, -3, 0]))