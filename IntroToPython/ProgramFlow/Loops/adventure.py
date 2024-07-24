available_exits = ["North", "East", "South", "West"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit == "Quit":
        print("Game Over")
        break
else:
    print("Aren't you glad you excaped")
