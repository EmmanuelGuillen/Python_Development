# while loop = a statement that will execute its block of code as long as its condition remains true
#          2 different ways to do the same code

#while 1==1:                (Infinite loop!)
#    print("Help im stuck in a loop!")

#name = ""

#while len(name) == 0:
#    name = input("what is your name?: ")
#print("Hello "+name)

name = None

while not name:
    name = input("What's your name?: ")
print("Hello "+name)
