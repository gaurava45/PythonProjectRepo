var1 = 6
var2 = 56
var3 = int(input())

if var3 > var2:
    print("greater")
elif var3 == var2: #else if is needed to avoid useless checking of if conditions in case there is a relation among statements
    #in them
    print("equal")
else:
    print("lesser")

list1 = [5, 7, 9]

if 5 in list1:
    print("yes")

if 15 not in list1:
    print("no")



