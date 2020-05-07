# Function to add items to Fantasy Inventory

def displayInventory(inventory):
    item_total = 0
    if type(inventory) == dict:
        print('Inventory: ')
        for k, v in inventory.items():
            print(str(v) + ' ' + k)
            item_total += v
        print('Total number of items: ' + str(item_total) + '\n')
    elif type(inventory) == list:
        count = {}
        for thing in inventory:
            count.setdefault(thing, 0)
            count[thing] = count[thing] + 1
        displayInventory(count)
    else:
        print('Cannot work with this data type for inventory')
        

def addToInventory(inventory, addedItems):
    count = {}
    for item in addedItems:
        count.setdefault(item, 0)
        count[item] = count[item] + 1
    for item in count:
        if item in inventory:
            inventory[item] = inventory[item] + count[item]
        else:
            inventory[item] = count[item]
        
