# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you can't use additional data structures?
# Need to potentially check through the entire string in to find a character that may repeat: O(n) runtime

class Solution:

    def isUnique(string):
        unique_chars = []
        if len(string) > 128:   # ask if string is ASCII (128 characters) or UNICODE.
            return False
        for char in string:
            if char in unique_chars:
                return False
            else:
                unique_chars.append(char)
        return True
