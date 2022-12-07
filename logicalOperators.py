# logical operators (and,or,not) = used to check if two or more conditional statements are true

temp = int(input("What is the temperature today?: "))

#if temp >= 0 and temp <= 30:
#    print("The weather is nice today!")
#    print("Go outside!")

#elif temp < 0 or temp > 30:
#    print("Its not a good day to be outside")
#    print("Dont go outside!")

if not(temp >= 0 and temp <=30):
    print("Its not a good day to be outside")
    print("Dont go outside!")

if not(temp < 0 or temp > 30):
    print("The weather is nice today!")
    print("Go outside!")
