#print numbers 1 to n in one line

# [print(i, end = " ") for i in range(1, int(input("upto?:")) + 1)]


# print([i for i in range(1, int(input("upto?:")) + 1)])


print(r"C:\Users\harry\Desktop")

print("C:\\Users\\harry\\Desktop")


# Oh soldier Prettify my Folder

# path, dictionary file, format

# def soldier("C://", "harry.txt", "jpg")

# import os
# def soldier(path, file, format):
#     os.chdir(path)
#     i = 1
#     files = os.listdir(path)
#     with open(file) as f:
#         filelist = f.read().split("\n")
#
#     for file in files:
#         if file not in filelist:
#             os.rename(file, file.capitalize())
#
#         if os.path.splitext(file)[1] == format:
#             os.rename(file, f"{i}{format}")
#             i +=1
#
# soldier(r"C:\Users\Haris\Desktop\testing",
#         r"C:\Users\Haris\PycharmProjects\PythonTuts\ext.txt", ".png" )


# a = input("What is your name")
# b = input("How much do you earn")
# if int(b)==0:
#     raise ZeroDivisionError("b is 0 so stopping the program")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
#
# print(f"Hello {a}")
# 1000 lines taking 1 hour

# Task - Write about 2 built in exception

c = input("Enter your name")
try:
    print(a)

except Exception as e:

    if c =="harry":
        raise ValueError("Harry is blocked he is not allowed")

    print("Exception handled")

