# def func():
#     print('Run')


# func()
# //////////////////////////////////////////////////

# defining a function within a function
# def func():
#     print('Run')

#     def func():
#         print('hi')
#     func()


# func()

# /////////////////////////////////////////////////////

# def func(x, y):
#     print('Run', x, y)
#     return x * y


# print(func(5, 6))

# ///////////////////////////////////////////////////

# multiple answers
# def func(x, y):
#     print('Run', x, y)
#     return x * y, x / y


# print(func(5, 6))

# //////////////////////////////////////////////////////

# Separating the answers into variables
# def func(x, y):
#     print('Run', x, y)
#     return x * y, x / y


# r1, r2 = func(5, 6)
# print(r1, r2)

# //////////////////////////////////////////////////////////

# Optional Parameter
# def func(x, y, z=None):
#     print('Run', x, y, z)
#     return x * y, x / y


# r1, r2 = func(5, 6)
# print(r1, r2)


# def func(x, y, z=None):
#     print('Run', x, y, z)
#     return x * y, x / y


# r1, r2 = func(5, 6, 7)
# print(r1, r2)


# ////////////////////////////////////////////////////////////////

# Adv example of a function
def func(x):
    def func2():
        print(x)

    return func2


# func(3)()

x = func(3)
x()
