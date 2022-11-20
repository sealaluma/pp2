import random

greets = str(input("Hello! What is your name?\n"))
x = random.randint(1, 20)
cnt = 0
print ("Well, " + greets + ", I am thinking of a number between 1 and 20.")

while cnt < 100000000:
    cnt += 1
    guess = int(input("Take a guess.\n"))

    if x == guess:
        print("Good job, " + str(greets) + "! You guessed my number in ", cnt, " guesses!")
        break
    elif guess > x:
        print("Your guess is too high.")
        
    elif guess < x:
        print("Your guess is too low.")