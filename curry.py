import functools

def func(a, b, c):

	return a, b, c	

f_func = functools.partial(func, 10)
print f_func(3, 4)

f_func = functools.partial(func, 10, 12)
print f_func(3)
