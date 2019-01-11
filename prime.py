def get_integer():
    return int(input("Give me a number: "))
number = get_integer()
flag = 1
for i in range(2,number):
    if number % i == 0:
        flag = 0
        break
if flag == 1:
    print("prime number")
else:
    print("Not Prime")