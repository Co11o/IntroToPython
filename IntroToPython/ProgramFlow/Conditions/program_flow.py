name = input("Please enter your name: ")
age = int(input("How old are your, {0}? ".format(name)))
print(age)

if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("You are Yoda")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")

# Other way of checking logic
# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18-age))
