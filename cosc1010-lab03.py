# Riley Green
# UWYO COSC 1010
# 9/26/24
# Lab 03 
# Lab Section: 
# Sources, people worked with, help given to: Bradley Ekstrom, Nolan Hottell 
# your
# comments
# here


# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 


print("Part One------------------------------------------------------------------------")
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list

cities = ["Wyoming", "Colorado", "Montana"]


#print the entire list

print(cities)

#now print the first element in the list

print(cities[0])

#Print the last element using the syntax shown in class to access the final element (hint, think negatives)

print(cities[-1])

#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided

print(f"{cities[1]} is south of {cities[0]}")

print("Part Two------------------------------------------------------------------------")
#Append the following states to your list: Washington, Oregon, California and print your list

cities.append("Washington")
cities.append("Oregon")
cities.append("California")
print(cities)

#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 

cities[-2] = "Maine"
print(cities)

#Insert the state Texas to be the third element in the list, again printing your list

cities.insert(2, "Texas")
print(cities)

#Using the `del` statement remove the fourth item from the list, print your list 

del cities[3]
print(cities)

#Remove Texas using its value, print the list

cities.remove('Texas')
print(cities)

print("Part Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 

print(sorted(cities))

#Permanently sort your list in reverse order, printing it out

print(sorted(cities, reverse=True))

#Using the reverse method reverse the list and print it

cities.reverse()
print(cities)