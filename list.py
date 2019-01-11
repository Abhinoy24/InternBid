a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input("Choose a number: "))
mylist = []
for i in a:
    if i < num:
        mylist.append(i)
        
print(mylist)