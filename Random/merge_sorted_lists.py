"""My friend and I are going to merge our cookies orders and
enter as one unit. Each order is represented by an "order id" (an integer).
We have our lists of orders sorted numerically already, in lists.
Write a function to merge our lists of orders into one sorted list."""

list1 = [3, 4, 6, 10, 11, 15]
list2 = [1, 5, 8, 12, 14, 19]
# merged_lists = [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

def merged_lists_function(list1, list2):
    combined_size = len(list1) + len(list2)
    merged_lists = [None] * combined_size

    # iterators for each list
    # i - list1, j - list2, k - merged_lists
    i=j=k=0

    while k < combined_size:
        list1_finished = i >= len(list1)   # IndexError edge case
        list2_finished = j >= len(list2)

        if(not list1_finished and
            (list2_finished or
            list1[i] < list2[j])):
            merged_lists[k] = list1[i]
            i += 1
        else:
            merged_lists[k] = list2[j]
            j += 1
        k += 1

    return merged_lists


print(merged_lists_function(list1, list2))
