def bubble_sort(list):
    n = len(list) - 1
    while n > 1:
        index = 0
        while index < n:
            if list[index] > list[index + 1]:
                tmp = list[index]
                list[index] = list[index + 1]
                list[index + 1] = tmp
            index += 1
        n -= 1
    list.reverse()
    return list


list1 = [6,7,3,4,5,1,2,9,6,8]

print(bubble_sort(list1))