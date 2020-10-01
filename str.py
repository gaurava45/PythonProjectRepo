mystr = "harry is a good boy"
print(len(mystr))

print(mystr[0:5]) #including first argument i.e. 0 and excluding second argument i.e. 5

print(mystr[0:79]) #doesnt give error prints till length of string

print(mystr[0:])  #takes length of string as second paramenter by default

print(mystr[0:5:2])

print(mystr[::-1]) # reverses the string

print(mystr.find("good"))

print(mystr.replace("is", "are"))