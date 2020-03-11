'''Given head which is a reference node to a singly-linked list.
The value of each node in the linked list is either 0 or 1.
The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        current = head
        binary_list = []
        total = 0

        while current:
            binary_list.append(current.val)
            current = current.next

        for i in range(len(binary_list)):
            total += (2**i) * (int(binary_list[~i]))
        return total
