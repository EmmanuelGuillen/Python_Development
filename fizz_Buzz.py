# 3 fizz , 5 buzz , 3 and 5 fizzbuzz
# % means divisible by
# 12%12 == 0

for x in range(1,21):
    if x % 15 == 0:
        print("fizzbuzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else :
        print(x)