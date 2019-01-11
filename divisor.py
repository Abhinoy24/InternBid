number = int(input("Enter a number to check for its divisor: "))
listRange = list(range(1,number+1))
divisorList = []
for i in listRange:
    if number % i == 0:
        divisorList.append(i)
print(divisorList)

