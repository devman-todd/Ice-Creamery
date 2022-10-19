print("Welcome to The Ice Creamery")
flavorList = ["Vanilla", "Chocolate", "Strawberry", "Pistachio", "Butter Pecan", "Cookie Dough", "Neapolitan"]
flavorList[3] = "Rocky Road"
new_flavor = "Mint Chip"
flavorList.append(new_flavor)
flavorList.sort(key=str.lower)
print("\nThese are the 8 flavors we are serving today at The Ice Creamery:\n")
for i in range(len(flavorList)):
    print("Flavor #: {} {}".format(i + 1, flavorList[i]))
conePrices = {"S":"$1.50","M":"$2.50","L":"$3.50"}
coneSizes = {"S":"smallish","M":"more for me","L":"lotta lickin"}
customerSize = input("\nPlease enter a cone size of your choosing: S, M, or L: ").upper()
if customerSize == "S":
    print("You selected S")
elif customerSize == "M":
    print("You selected M")
elif customerSize == "L":
    print("You selected L")
else:
    print("Invalid Size Selected")
customerFlavor = int(input("Please enter your flavor number: "))-1
if customerFlavor == int(1)-1:
    print("You selected Butter Pecan")
elif customerFlavor == int(2)-1:
    print("You selected Chocolate")
elif customerFlavor == int(3)-1:
    print("You selected Cookie Dough")
elif customerFlavor == int(4)-1:
    print("You selected Mint Chip")
elif customerFlavor == int(5)-1:
    print("You selected Neapolitan")
elif customerFlavor == int(6)-1:
    print("You selected Rocky Road")
elif customerFlavor == int(7)-1:
    print("You selected Strawberry")
elif customerFlavor == int(8)-1:
    print("You selected Vanilla")
else:
    print("Invalid Flavor Selected")

costTotal = conePrices[customerSize]
costFlav = flavorList[customerFlavor]
costSize = coneSizes[customerSize]
print()
print("Your total is: " + costTotal)
print("Your " + costSize + " sized cone of the Ice Creamery's " + costFlav + " will arrive shortly")
print()
print("Thank you for visiting the Ice Cream Creamery!")