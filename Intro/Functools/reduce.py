import functools as f

a=[True,False,True,False]
print(f.reduce(lambda a,b: a and b,a))

