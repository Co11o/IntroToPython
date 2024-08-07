# Write a function named sum_eo with the following parameters:
# n: a positive number
# t: a str
#
# If t has the value 'e', the function should return the sum of all even natural numbers less than n.
# Else if t has the value 'o', the function should return the sum of all odd natural numbers less than n.
# For any other values of t return -1.
#
# Examples:
# 1. sum_eo(10, 'e') should return 20, since 2 + 4 + 6 + 8 = 20
#
# 2. sum_eo(7, 'o') should return 9, since 1 + 3 + 5 = 9
#
# 3. sum_eo(11, 'spam') should return -1

def sum_eo(n, t):
    if t == "e":
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))


# Test cases
print(sum_eo(10, 'e') == 20)
print(sum_eo(7, 'o') == 9)
print(sum_eo(10, 'other') == -1)