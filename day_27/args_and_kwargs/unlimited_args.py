# Here how to make a function accept any number of arguments. We can see these in libraries and module
# Also Known as Unlimited Positional Arguments because the positions matters so much

def func(*args):
    for arg in args:
        print(arg)


func(1, "Hello", ["l;", 3, '-'], "$$$")
print("\n\n\n")


# Challenge - Create a function that takes any number of arguments (in this case numbers) and then sum up
def add(*args):
    return sum(args)


print(add(1, 324, 4, 4, 224, 23, 2, 34, 242, 42, 34, 234, 234, 32))