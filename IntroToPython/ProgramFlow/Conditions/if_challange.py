name = input("Please enter your name: ")

age = int(input("Please enter your age: "))

if (age >= 18) and (age < 31):
    print(name + " is welcome to the party")
elif (age < 18):
    print(name + " is not old enough for the party")
else:
    print(name + " is too old for the party")
