def remove_every_second_element(items):
    updated_list = []
    for item in items:
        if items.index(item) % 2 == 0:
            updated_list.append(item)
    return updated_list


print(remove_every_second_element(['apple', 'banana', 'orange', 'Grape', 'Mango', 'Pineapple']))
print(remove_every_second_element([1, 2, 3, 4, 5, 6]))