# x = [x for x in range(5)]
# print(x)


# x = [x + 5 for x in range(5)]
# print(x)

# x = [0 for x in range(5)]
# print(x)


# List
# x = [[0 for x in range(100)] for x in range(5)]
# print(x)

# List
# x = [i for i in range(101) if i % 5 == 0]
# print(x)

# Dictionary
# x = {i: 0 for i in range(101) if i % 5 == 0}
# print(x)

# Set
# x = {i for i in range(101) if i % 5 == 0}
# print(x)

# Tuple // Generator Object
x = tuple(i for i in range(101) if i % 5 == 0)
print(x)
