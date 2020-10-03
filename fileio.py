f = open("harry.txt", "rt")

for line in f:
    print(line, end = "")
f.close()
print()

f2 = open("harry.txt", "rt")
print(f2.readlines())         #each line has \n in the end
f2.close()

f3 = open("harry.txt", "r+")
print(f3.readline())
f3.write("\nthank you")

f3.close()

