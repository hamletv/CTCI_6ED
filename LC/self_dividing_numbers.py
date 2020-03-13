"""A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0,
and 128 % 8 == 0. Also, a self-dividing number is not allowed to contain the digit
zero. Given a lower and upper number bound, output a list of every possible self
dividing number, including the bounds if possible."""

# The boundaries of each input argument are 1 <= left <= right <= 10000.

def self_dividing_number(left, right):
    def check_number(number):
        for digit in str(number):
            if digit == '0' or number % int(digit) != 0:
                return False
        return True

    self_dividing_number_list = []

    for num in range(left, right):
        if check_number(num):
            self_dividing_number_list.append(num)

    return self_dividing_number_list


def self_dividing_number2(left, right):
    return [num for num in range(left, right+1) if '0' not in str(num) and \
    all((num % int(digit)) == 0 for digit in str(num))]


print(self_dividing_number(1,200))
print(self_dividing_number2(1,100))
