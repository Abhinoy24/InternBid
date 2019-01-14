
price_dictonary = {
    "apple":40,
    "orange":50,
    "kiwi":100,
    "avacado":130,
    "watermelon":150
}
print("We have the prices of the following items:")
for item in price_dictonary:
    print(item)

print("Enter the item name for which you wanna search the price:")
item = input()
item = item.lower()

if item in price_dictonary:
    print('{}\'s price is {}.'.format(item, price_dictonary[item]))
else:
    print('Sadly, we don\'t have {}\'s item.'.format(item))
     