# Given two strings, check if one is a permutation of the other.
# Confirm if string characters are case sensitve or not.
# Do spaces count?

def ck_permutation(string1, string2):
    if len(string1) != len(string2): # string lengths must be equal
        return False
    for char in string1:
        if char no in string2:
            return False
        else:
            return True
