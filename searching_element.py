def linear_search(list,target):
    for i in list:
        if list[i] == target:
            return i
        return -1

print(linear_search(list,8)