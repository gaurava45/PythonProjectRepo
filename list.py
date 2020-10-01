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

print(tu)

# tu[1] = 5   tuple is immutble

a = 1
b = 2
a,b = b,a

print(a,b)