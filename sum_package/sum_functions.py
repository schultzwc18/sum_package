def sum_two_numbers(num1, num2):
    total = num1 + num2
    return total


def sum_any_numbers(*args):
    total = 0
    for num_arg in args:
        total = total + num_arg
    return total
