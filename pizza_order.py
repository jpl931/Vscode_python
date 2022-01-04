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

    
