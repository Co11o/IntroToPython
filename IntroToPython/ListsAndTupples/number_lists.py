empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# numbers = even + odd
# print(numbers)

other_numbers = [even, odd]
print(other_numbers)

for number_list in other_numbers:
    print(number_list)

    for value in number_list:
        print(value)

# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
#
# digits = list("432985617")
# print(digits)
#
# # more_numbers = list(numbers)
# # more_numbers = numbers[:]
# more_numbers = numbers.copy()
# print(more_numbers)
# print(numbers is more_numbers)
# print(numbers == more_numbers)
#
# print(min(odd))
# print(max(odd))
# print(min(even))
# print(max(even))
#
# print()
# print(len(odd))
# print(len(even))
#
# print()
# print("Mississippi".count("iss"))
#
# even.extend(odd)
# print(even)
# even.sort()
# print(even)
# another_even = even
# even.sort(reverse=True)
# print(even)
# print(another_even)
