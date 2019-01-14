import json

pricelist = {}

with open('price.json','r') as f:
    pricelist = json.load(f)

def add_entry():
    item = input("Enter the name of the item:\n").title()
    price = input('Enter the {} price \n'.format(item))
    pricelist[item] = price
    with open('price.json','w') as f:
        json.dump(pricelist,f)
    print('{} was added to the pricelist\n'.format(item))

def find_price():
    item = input('Enter the item name for which you wanna search the price:').title()
    try:
        if pricelist[item]:
            print(' {} price is {}\n'.format(item,pricelist[item]))
    except KeyError:
        print('{} is not in the list'.format(item))

def list_entries(): 
    print("Current Entries in the list are:\n")
    for key in pricelist:
        print(key.ljust(31), ':', pricelist[key])
    print()


