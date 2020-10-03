l = 10 #global

def function1():
    global l  #allows function to change global variable
    l = l + 45
    print(l)

function1()