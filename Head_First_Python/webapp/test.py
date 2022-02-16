# def outer():
#     def inner():
#         print('This is inner function')
#
#     print('This is outer function')
#     inner()
#
#
# outer()
# print('-' * 20)
#
#
# def outer():
#     def inner():
#         print('This is inner function')
#
#     print('This is outer function')
#     return inner
#
#
# outer()()
# print('-' * 20)
# i = outer()
# print(type(i))
# i()
# i()


# def my_function(*args):
#     print(args)
#     print(type(args))
#
#
# my_function(1, 2, 3, 4, 5)
# print('-' * 20)
#
# def my_function(*args):
#     for a in args:
#         print(a, end=' ')
#     else:
#         print()
#
#
# my_function(10)
# my_function()
# my_function(10, 20, 30)
# my_function(10, 'hello', 30)
#
# values = [10, 20, 30]
# my_function(values)
# my_function(*values)
#
#
# def my_function2(**kwargs):
#     for k, v in kwargs.items():
#         print(k, v, sep='->', end=' ')
#         print()
#     if kwargs:
#         print('kwargs is not empty')
#     else:
#         print('kwargs is empty')

#
# my_function2(a=10, b=20, c=30)
# my_function2()
#
# def my_function3(*args, **kwargs):
#     if args:
#         for a in args:
#             print(a, end=' ')
#         print()
#     if kwargs:
#         for k, v in kwargs.items():
#             print(k, v, sep='->', end=' ')
#         print()
#
#
# my_function3(1, 2, 3, a=10, b=20, c=30)
# my_function3()
# my_function3(a=10, b=20, c=30)
# my_function3(1, 2, 33)
#
# type_list = [int, float, str, bool]
# try:
#      with open('todos.txt' 'r') as f:
#           print(f.read(2))
# except FileNotFoundError as e:
#      print(e)
import sys

#
# try:
#     1 / 0
# except:
#     err = sys.exc_info()
#     print(err)
#     for a in err:
#         print(a)


try:
    1 / 0
except Exception as err:
    print(err.__repr__())
    print(err.__str__())
    print(err.__cause__)
    print(err.__context__)
    print(err.__traceback__)
    print(err.__suppress_context__)