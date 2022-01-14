from collections import OrderedDict


thatsAlowPrice = 7.50
thatsAhighPrice = 10.50

myMenu = OrderedDict()

myMenu["Sandwich"] = thatsAlowPrice
myMenu["Burger"] = thatsAhighPrice
myMenu["Steak"] = thatsAhighPrice

i=1
for k, v in myMenu.items():
    print(i, k, v)
    i += 1

itemNumber = int(input("Please enter the number of the item you would like to order: "))
item=list(myMenu.keys())[itemNumber-1]

print("You have ordered the following:", item)
print("The price is:  $", myMenu[item])
print("Thank you for your order!")
 
 # print(myMenu))
 # print(myMenu.keys())
 # print(myMenu.values())
 # print(myMenu.items())
    # print(myMenu.get("Sandwich"))
    # print(myMenu.get("Burger"))
    # print(myMenu.get("Steak"))
    # print(myMenu.get("Pizza"))

    
