"""Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings."""

def balancedStringSplit(s:str) -> int:
    output, balance = 0

    for i in range(len(s)):
        if s[i] == 'L':
            balance += 1
        if s[i] == 'R':
            balance -= 1
        if balance == 0:
            output += 1
    return output
