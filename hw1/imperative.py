def sort_list_imperative(array):
    temp = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] > array[i]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array

array = [1, 2, 3, 5, 8, 10, 17, 105, 14, 6, -17, 0]
print(array)
print(sort_list_imperative(array))
