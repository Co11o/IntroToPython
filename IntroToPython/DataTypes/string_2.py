# number = "9,223;372;036 854,775;807"
# separator = number[1::4]
# print(separator)
#
# values = "".join(char if char not in separator else "" for char in number).split()
# print([int(val)for val in values])

number = input("Please enter a series of numbers, using any separators: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators += char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))
