import random
import sys
import os

# print("Hello World")

# Comment

'''
Multiple
Line
Comment
'''

'''
First = "Peter"
Last = "Du"
print("%s %s\n" % (First, Last) * 5)
'''

'''

grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print('The first item is', grocery_list[1])

# You can change the value stored in a list box
grocery_list[0] = "Green Juice"
print(grocery_list)

# You can get a subset of the list with [min:up to but not including max]

print(grocery_list[1:3])

# You can put any data type in a a list including a list
other_events = ['Wash Car', 'Pick up Kids', 'Cash Check']
to_do_list = [other_events, grocery_list]  # this is NOT a copy; it holds them "by reference"

print(to_do_list)

# Get the second item in the second list (Boxes inside of boxes)
print(to_do_list[1][1])

# You add values using append
grocery_list.append('onions')
print(to_do_list)

tdl = other_events + grocery_list  # This is a copy; changes to either list won't change tdl
print(tdl)
other_events.remove('Cash Check')
print(tdl)
print(other_events)
print(to_do_list)

'''

# # Simple closure example
# def outer(x):
#     def inner():
#         print(x)
#     return inner
#
# print1 = outer(1)
# print2 = outer(2)
# print1()
# print2()
#
# print(print1.__closure__)
# print(print2.__closure__)
#


# # Simple decorator example
# def outer(some_func):
#     def inner():
#         print("before some_func")
#         ret = some_func()
#         print(ret + 1)
#     return inner
#
#
# def foo():
#     return 1
#
# decorated = outer(foo)
# decorated()


# More useful decorator example
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Coord: " + str(self.__dict__)


def wrapper(func):
    def checker(a, b):
        if a.x < 0 or a.y < 0:
            a = Coordinate(max(a.x, 0), max(a.y, 0))
        if b.x < 0 or b.y < 0:
            b = Coordinate(max(b.x, 0), max(b.y, 0))
        ret = func(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = Coordinate(max(ret.x, 0), max(ret.y, 0))
        return ret
    return checker


@wrapper
def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)


@wrapper
def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)

one = Coordinate(100,200)
two = Coordinate(300,200)

print(add(one, two))
three = sub(one, two)
print(three)
print(add(one, three))


# Another (more general) decorator example
def logger(func):
    def inner(*args, **kwargs):
        print("Arguments were: %s, %s" % (args, kwargs))
        return func(*args, **kwargs)
    return inner


@logger
def foo1(x, y=1):
    return x * y


@logger
def foo2():
    return 2

res1 = foo1(5, 4)
print(res1)

res2 = foo1(2,y=3)
print(res2)

res3=foo2()
print(res3)