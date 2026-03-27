

numberOfUsers = int(input("How many users do you want to add: "))

userAndItemDict = {}
for i in range(numberOfUsers):
    name = input("Enter username: ")
    itemCount = int(input("How many items? "))

    items = []
    for j in range(itemCount):
        items.append(input(f"Item {j+1}: "))

    userAndItemDict[name] = items

print("User DATA: ")
for (key,values) in userAndItemDict.items():
    print(f"{key} -> ",end="")
    print("[",end="")
    for value in values:
        print(f"'{value}' ", end="")
    print("]")
    print()



allItems = []

for item in userAndItemDict.values():
    allItems.extend(item)


noDuplicateItems = set(allItems)



commonItems = []
uniqueItems = []
itemsSelectionNumber = {}





for item in noDuplicateItems:
    count = 0
    for value in userAndItemDict.values():
        if item in value:
            count += 1

    itemsSelectionNumber[item] = count

    if count > 1:
        commonItems.append(item)
    else:
        uniqueItems.append(item)




print()
print()
print("COMMON ITEMS: ")
for item in commonItems:
    print(item)


print()
print()
print("UNIQUE ITEMS:")

for item in uniqueItems:
    print(item)

popularItem = ""
maxCount = 0
for item,count in itemsSelectionNumber.items():
    if count > maxCount:
        maxCount = count
        popularItem = item


print()
print()
print("MOST POPULAR ITEM")
print(popularItem)
