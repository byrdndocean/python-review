# def func(*args, **kwargs):
#     pass


# x = [1, 23, 236363, 2727]
# print(*x)
# ////////////////////////////////////////////////////////
# def func(x, y):
#     print(x, y)


# pairs = [(1, 2), (3, 4)]

# for pair in pairs:
#     func(*pair)
# /////////////////////////////////////////////////////////////


# def func(x, y):
#     print(x, y)


# func(**{'x': 2, 'y': 5})

# //////////////////////////////////////////////////////////////

# def func(x, y):
#     print(x, y)


# func(**{'y': 5, 'x': 2})

# ////////////////////////////////////////////////////////////////

# def func(*args, **kwargs):
#     print(args, kwargs)


# func(1, 2, 3, 4, 5, one=0, two=1)


# ////////////////////////////////////////////////////////////

def func(*args, **kwargs):
    # print(*args)
    print(**kwargs)


func(1, 2, 3, 4, 5, one=0, two=1)
