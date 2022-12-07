# nested loops =    The "inner loop" will finish all of it's iterations before
#                   finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()        # make sure this print statement is not in the inner loop which is why its indented only once not twice
