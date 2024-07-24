Options = ["Shower", "Workout", "Eat", "Coffee", "Brush teeth", "Drive to work"]

for i, activity in enumerate(Options):
    print(f"{i + 1}. {activity}")
print("\nChoose an activity:")

current_input = None

while current_input != 0:
    current_input = int(input())

    if current_input == 1:
        print("Showering...")
    elif current_input == 2:
        print("Working out...")
    elif current_input == 3:
        print("Eating...")
    elif current_input == 4:
        print("Taking a coffee...")
    elif current_input == 5:
        print("Brushing teeth...")
    elif current_input == 6:
        print("Driving to work...")
    else:
        print("Invalid choice. Please try again.")
else:
    print("Goodbye, Program exited successfully.")
