def binary_search(list, value):
    if value in list:
        return list.index(value)
    return -1


list1 = [1,2,3,4,5,6,7,8,9]
list2 = [55,77,134,657,777,957,999]
list3 = [-9,-8,-7,-6,-5,-4,-3,-2,-1]


print(binary_search(list1, 1))
print(binary_search(list1, 11))

print(binary_search(list2, 134))
print(binary_search(list2, 135))

print(binary_search(list3, -6))
print(binary_search(list3, 1))