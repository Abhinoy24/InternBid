def max_of_three(a,b,c):
    max_3 = 0
    if a>b:
        if a>c:
            max_3=a
        else:
            max_3=c
    else:
        if b>c:
            max_3=b
        else:
            max_3=c
    return max_3

number1 = int(input("Enter the 1st number:"))
number2 = int(input("Enter the 2nd number:"))
number3 = int(input("Enter the 3rd number:"))

max = max_of_three(number1,number2,number3)
print("Maximun:",max)