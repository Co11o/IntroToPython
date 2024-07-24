current_choice = "-"
computer_parts = []
available_parts = ["computer", "mouse", "keyboard", "monitor", "mouse mat"]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)

while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("List now contains: {}".format(computer_parts))
    else:
        print("Please add a number from below")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input("Enter your choice: ")

print(computer_parts)
