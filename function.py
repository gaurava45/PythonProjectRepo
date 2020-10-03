a = 9
b = 8
c = sum((a, b)) #builtin function
print(c)

def fn1():
    print("you are in function 1")

fn1()
print(fn1())

def average(a, b):
    """This function calculates average of two numbers"""
    average = (a + b)/2
    return average

v = average(a, b)
print(v)

print(average.__doc__)