name = "Manny Alvarez"
#indexing
#To start can leave blank (will assume 0) and to end you can leave blank (will assume end)

#first_name = name[0:5] - [:5]
#last_name = name[6:13] - [6:end]
#print(first_name)
#print(last_name)

#Can also do [::2] (will assume start to finish)
#funky_name = name[0:13:2] - [::2] # [0:end:2]
#print(funky_name)

#reversed_name = name[::-1] - [0:end:-1]
#print(reversed_name)

####slicing

website1 = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4)

print(website1[slice])
print(website2[slice])