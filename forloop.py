list1 = [ ["Harry", 1], ["Carry", 2], ["Larry", 6], ["Marry", 25]]

for item, lollypop in list1:
    print(item, lollypop)

dict1 = dict(list1)

print(dict1)
for item, lollypop in dict1.items():
    print(item, lollypop)

for item in dict1:
    print(item)

items = [int, float, "harry", 4, 8, 12]

for item in items:
    print(item)

for item in items:
    if str(item).isnumeric() and item > 6:
        print(item)