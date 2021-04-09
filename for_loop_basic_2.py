# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list


print(biggie_size([-1, 3, 5, -5]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it


def count_positives(list):
    posValues = 0
    for i in range(len(list)):
        if list[i] > 0:
            posValues += 1
    list[len(list)-1] = posValues
    return list


print(count_positives([-1, 1, 1, 1]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7


def sumTotal(list):
    sum = 0
    for i in list:
        sum += i
    return sum


print(sumTotal([1, 2, 3, 4]))

# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5


def average(list):
    sum = 0
    for i in list:
        sum += i
    return sum/len(list)


print(average([1, 2, 3, 4]))


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(list):
    return len(list)


print(length([]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False


def minimum(list):
    if len(list) > 0:
        min = list[0]
        for i in list:
            if i < min:
                min = i
        return min
    else:
        return False


print(minimum([-1, 34, -3, 18]))

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False


def maximum(list):
    if len(list) > 0:
        max = list[0]
        for i in list:
            if i > max:
                max = i
        return max
    else:
        return False


print(maximum([37, 2, 1, -9]))
# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }


def ultimate_analysis(list):
    newDict = {
        'sumTotal': 0,
        'average': 0,
        'minimum': list[0],
        'maximum': list[0],
        'length': len(list)
    }
    if len(list) > 0:
        for i in list:
            newDict['sumTotal'] += i
            if i < newDict['minimum']:
                newDict['minimum'] = i
            elif i > newDict['maximum']:
                newDict['maximum'] = i
        newDict['average'] = newDict['sumTotal']/len(list)
        return newDict
    else:
        return False


print(ultimate_analysis([37, 2, 1, -9]))

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]


def reverse_list(list):
    list[0], list[len(list)-1] = list[len(list)-1], list[0]
    return list
    # this method (below) works too


def reverse_list2(list):
    first_elem = list[0]
    last_elem = list[len(list)-1]
    list[0] = last_elem
    list[len(list)-1] = first_elem
    return list


print(reverse_list([1, 2, 3, 4]))
print(reverse_list2([1, 2, 3, 4]))
