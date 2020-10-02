s = set()
print(type(s))

s_from_list = set([1, 2, 4, 4])
print(s_from_list)

s.add(1)
s.add(1)
s.add(2)
print(s)

s = s.union([1, 2, 3])
print(s)

s = s.intersection([1, 4])
print(s)

print(len(s_from_list))
print(min(s_from_list))

s1 = set([9, 7, 4])
s1.remove(4)
print(s_from_list.isdisjoint(s1))
