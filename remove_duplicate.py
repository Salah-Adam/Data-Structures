def remover_duplicate(list):
    list.reverse()
    for i in list:
        if list.count(i) > 1:
            list.remove(i)
    list.reverse()
    return list

print(remover_duplicate([1, 2, 3,2, 4, 1]))
print(remover_duplicate(["apple", "banana", "apple", "cherry"]))
print(remover_duplicate([5, 2, 7, 5, 1, 2, 9, 7]))