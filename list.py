grocery = ["harpic", "vim bar", "deodorant"]
print(grocery[1])

numbers = [3, 7, 2, 4, 9]
# numbers.sort()
# numbers.reverse()
print(numbers[::2])

print(numbers[::-1])

numbers.append(12)

print(numbers)

numbers.insert(2, 67)

print(numbers)

numbers.remove(2)  #removes 2 from list

print(numbers)

numbers.pop() # removes last element

print(numbers)

tu = (1, 2)   #tuple

tup1 = (1)  #takes it as as int
tup2 = (1,)  #need to give extra ',' to make it a tuple

print(type(tup1))
print(type(tup2))
print("tup1 : " ,tup1)
print("tup2 : " ,tup2)

print(tu)

# tu[1] = 5   tuple is immutble

a = 1
b = 2
a,b = b,a

print(a,b)