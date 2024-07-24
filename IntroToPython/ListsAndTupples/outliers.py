# 2 outliers both sides
# data = [ 4,5,104,105,110,120,130,130,150,
#          160,170,183,185,187,188,191,350,
#          360]
# No outliers
# data = [ 104,105,110,120,130,130,150,
#          160,170,183,185,187,188,191]
# # All outliers
# data = [1,3,5,78,404,405,504,606,1000]
# Empty list
data = []

min_valid = 100
max_valid = 200

data.sort()
# Process low values
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop)
del data[:stop]
print(data)

# process the high values
start = 0
# Starts at max, goes backwards, goes to first value
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        # Index of last item to keep
        # Set start to the position of the first index
        # Item to delete is 1 after 'index'
        start = index + 1
        break

print(start)
del data[start:]
print(data)

# del data[0:2]
# print(data)
# del data[14:]
# print(data)
#
#
# for index, value in enumerate(data):
#     if value < min_valid or value > max_valid:
#         del data[index]
#
# print(data)
