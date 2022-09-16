# MANNY'S QUIZ GAME !!

name = input("Would you like to play a game? ")

if name != ("yes"):
    print("Okay :(")
    quit()
elif name == ("yes"):
    print("Hello welcome to Manny's guessing game!!")
    print("Good luck!")

age = input("First question! " + ("How old is Manny? "))

while age != '26':
    age = input()

    if age == '26':
        print("Great job!")
    if age <= '26':
        print("A little higher")
    elif age >= '26':
        print("A little lower")

car = input("Is Manny's Shelby fast? ")

if car != ("yes"):
    print("WRONG! It's super fast!")
    quit()
if car == ("yes"):
    print("Wow you really know Manny huh?")
    print("Next question!")

son = input("What's Manny's sons name? ")

if son != ("kai"):
    print("Almost!")
    quit()
if son == ("kai"):
    print("Isn't he the cutest! :)")

truck = input("Is Manny's viper slow? ")

if truck != ("yes"):
    print("WRONG! It's super slow!")
    quit()
if truck == ("yes"):
    print("CORRECT! It's super slow!")
elif truck == ("yes"):
    print("Congratz you've completed Manny's guessing game!")