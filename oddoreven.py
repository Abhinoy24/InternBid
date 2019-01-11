number = input("Enter a number to check for odd or even: ")
number = int(number)
if number % 2 == 0:
    print(number,"is an even number")
else:
    print(number,"is an odd number")
if number % 4 == 0:
    print(number,"is an multiple of 4")