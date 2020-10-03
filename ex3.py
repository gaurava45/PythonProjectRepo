numG = 3
num = 20

guess = 1

while 1:
    inp = int(input("Enter the number\n"))
    if (inp > num):
        print("your number is bigger")
    elif (inp < num):
        print("your number is smaller")
    else:
        print("Correct")
        print("You guessed in", guess, "attempts")
        break;
    remG = numG - guess
    if remG == 0:
        print("You are out of guesses")
        break;
    else:
        print("Number of guesses left: ", remG)
    guess = guess + 1





