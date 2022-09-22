# tuple = collection which is ordered and unchangeable
#           used to group together related data


student = ("Manny", 26, "male")
print(student.count("Manny"))
print(student.index("male"))

for x in student:
    print(x)

if "Manny" in student:
    print("Manny is here!")


