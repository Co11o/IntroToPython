for index, character in enumerate("abcedfg"):
    print(index, character)

print("\n=====================\n")

# tuple
for t in enumerate("abcdefg"):
    index, character = t
    print(index, character)

index, character = (0, 'a')
print(index, character)
