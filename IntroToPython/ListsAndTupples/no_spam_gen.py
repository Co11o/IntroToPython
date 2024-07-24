menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
]

for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]

        print(meal)

print("\n================================\n")

for meal in menu:
    if "spam" in meal:
        for item in meal:
            if item == "spam":
                meal.remove("spam")
    print(meal)

print("\n================================\n")

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=", ")
    print()

print("\n================================\n")

for meal in menu:
    items = ", ".join((item for item in meal if item != "spam"))
    print(items)
