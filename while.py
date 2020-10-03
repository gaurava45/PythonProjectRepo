i = 0

while i < 10 :
    print(i, end = " ")
    i = i + 1

while True:
    if i < 15:
        i = i + 1
        continue
    print(i, end = " ")
    if i == 20:
        break
    i = i + 1

while 1:
    print(i, end = " ")
    if i == 30:
        break
    i = i + 1