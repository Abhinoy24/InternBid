number = int(input("Enter the range till you want to find the series:"))
i=1
if number == 0:
    fib = []
elif number == 1:
    fib = [1]
elif number == 2:
    fib = [1,1]
elif number > 2:
    fib = [1,1]
    while i < (number-1):
        fib.append(fib[i]+fib[i-1])
        i+=1
print(fib)
