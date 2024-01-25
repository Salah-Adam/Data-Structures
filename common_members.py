def check_common_members(l1, l2):
    for list in l1:
        if list in l2:
            return True
    return False


print(check_common_members([1,2,3,4,5],[6,7,4,8,8]))
print(check_common_members(["apple", "banana", 'cherry'], ["date", 'fig', "grape"]))
print(check_common_members([1, 2, 3, 4 ,5 ], [3, 6, 9, 12]))