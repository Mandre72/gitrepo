#Task1
def find_two_lowest(arr: list) -> tuple:

    arr.sort()

    lowest_1 = arr[0]
    lowest_2 = arr[1]

    return lowest_1, lowest_2


input_list = [198, 3, 4, 9, 10, 9, 2]
result = find_two_lowest(input_list)
print(result)  # Should return (2, 3)


#Task2
def invert_list(arr: list) -> list:

    inverted_arr = []

    for num in arr:

        inverted_num = -num

        inverted_arr.append(inverted_num)

    return inverted_arr


input_list = [1, 5, -2, 4]
result = invert_list(input_list)
print(result)  # Should return [-1, -5, 2, -4]


#Task3
def max_diff(arr: list):

    if len(arr) == 0:
        return 0

    arr.sort()

    smallest = arr[0]
    largest = arr[-1]
    difference = largest - smallest

    return difference


input_list = [3, 5, 7, 2]
result = max_diff(input_list)
print(result)  # Should return 3


#task4
def count_larger_neighbors(arr: list):

    count = 0

    for i in range(1, len(arr) - 1):

        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:

            count += 1

    return count


input_list = [2, 56, 7, 21, 22, 19, 26]
result = count_larger_neighbors(input_list)
print(result)  # Should return 2


#Task5
def subtract_min(arr: list):

    min_element = min(arr)

    for i in range(len(arr)):
        arr[i] -= min_element

    return arr


input_list = [9, 2, 5, 4, 7, 6, 1]
result = subtract_min(input_list)
print(result)  # Should return [8, 1, 4, 3, 6, 5, 0]
