shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)
#
# print("-" * 30)
#
# for item in shopping_list:
#     if item == "spam":
#         continue
#     print("Buy " + item)

item_to_find = "eggs"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Found at position {0}".format(found_at))
else:
    print("Not found")
