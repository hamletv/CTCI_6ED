"""
Given an integer array nums, find the contiguous subarray (containing at
least one number) which has the largest sum and return its sum.
"""

def maximum_subarray(arr):
    if len(arr) == 1:
        return arr[0]
    largest_sum = current_sum = arr[0]

    for number in arr[1:]:
        current_sum = max(number, current_sum + number)
        largest_sum = max(largest_sum, current_sum)
    return largest_sum


print(maximum_subarray([-2,1,-3,4,-1,2,1,-5,4]))
print(maximum_subarray([83, -165, 16, -5, -123, 231]))
