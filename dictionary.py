d1 = {}
print(type(d1))

d2 = {"harry":"burger", "rohan":"fish", "shubham":{"B":"maggi","L":"roti","D":"chicken"}}

print(d2["shubham"]["L"])

name = "harry"

d3 = {name:"burger", "rohan":"fish", "shubham":{"B":"maggi","L":"roti","D":"chicken"}}

name = "shubham"

print(d3[name])

d3[420] = "kebabs"
print(d3)

del d3[420]
print(d3)

d4 = d3.copy() #d4 is a copy of d3
del d4["harry"]
print(d3)
print(d4)

d4 = d3 #d4 points to d3
del d4["harry"]
print(d3)
print(d4)

print(d3.keys())
print(d3.items())
