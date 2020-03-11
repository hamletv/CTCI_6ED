"""Write an efficient function that tells us whether or not an input
string's openers and closers are properly nested."""

# openers = ['(', '{', '[']
# closers = [')', '}', ']']

def bracket_validator_function(string):
    bracket_dict = {'(':')', '{':'}', '[':']'}
    openers = ['(', '{', '[']
    closers = [')', '}', ']']
    bracket_stack = []

    for char in string:
        if char in openers:
            bracket_stack.append(char)
        elif char in closers:
            if not bracket_stack:
                return False
            else:
                bracket_stack_top = bracket_stack.pop()
                if not bracket_dict[bracket_stack_top] == char:
                    return False

    return bracket_stack == []

print(bracket_validator_function('({{{[[]]}}})'))
print(bracket_validator_function('({[[]}}})'))
