ShoppingItems = ["Grains","Peas","Sugar","Kodho"]
for item in ShoppingItems:
    if item == 'Sugar':
        continue
#continue escapes the item i.e is pointed and prints every items from the list
    print("Items are: "+item)
print("\n")

for item in ShoppingItems:
    if item == "Sugar":
        break
#Where as break doesnot read the items that are after the pointed item but prints the item that were before the p.item
    print("Buy "+item)
print("\n")

#Complex One

ItemsSold = ["Wardrobe" , "Sofa" , "Bed" , "Dining Tables" , "Dressing Table"]

#Kei kei bujhi rakhya xa hai guyz
for item in ItemsSold:
    if item =="Dining Tables":
        break
    else:
        Breaker = item
#Breaker = item if vitra hunxa vaney it has to be defined already
#But Breaker = item idf vitra na vaye xai we don't need to defined it earlier

if Breaker:
    print("{} ruined your knowledge".format(item))