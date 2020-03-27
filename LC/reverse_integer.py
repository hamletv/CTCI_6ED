'''Given a 32-bit signed integer, reverse digits of an integer.
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−2**31,  2**31 − 1]. For the purpose of
this problem, assume that your function returns 0 when the reversed integer
overflows.'''


def reverse_digits_of_integer(number):
    min_value = -2 ** 31
    max_value = 2 ** 31 - 1
    new_number = 0

    if number > 0:
        new_number = int(str(number)[::-1])
    if number < 0:
        new_number = - + int((str(number)[1:])[::-1])
    if new_number not in range(min_value, max_value):
        return 0
    else:
        return new_number

print(reverse_digits_of_integer(-3210))
