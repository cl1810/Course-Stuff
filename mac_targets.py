#This script correctly formats MAC addresses for addition to your Kismet .conf files for MAC Targeting.
inputUser = input('Type a list of target MACs separated by spaces ')
print("\n")

targetListFound = inputUser.split()
targetListLost = inputUser.split()

#manipulate the list to add the required prefixes

foundString = "devicefound=" 
lostString = "devicelost="

print("Here are your .conf inputs douche. \n")

for n in targetListFound:
	newFoundString = foundString + n
	print(newFoundString)

print("\n")

for n in targetListLost:
	newLostString = lostString + n
	print(newLostString)

