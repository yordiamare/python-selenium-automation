#When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
# The arithmetical mean is the sum of all elements divided by the number of elements.
#Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

def below_ar_mean(arr):
    ar_mean = sum(arr) / len(arr)
    final_list = []
    for i in arr:
        if i < ar_mean:
            final_list.append(i)
    return final_list

test_array = [1, 3, 5, 6, 4, 10, 2, 3]
print(test_array)
print(below_ar_mean(test_array))

#Two Lowest Elements
#When given a list of elements, find the two lowest elements.
#They can be equal to each other or different.
#Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def lowest_elements(arr):
    arr.sort()
    return arr[:2]

test_list = [198, 3, 4, 9, 10, 9, 2]
print (lowest_elements(test_list))