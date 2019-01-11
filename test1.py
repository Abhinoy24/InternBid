import random
password_length = int(input("Enter the length of password you want: "))
s = "abcdefghijklmnopqrstuvwxyz123456789!@#$%^&*()_?><{}[]-+~,.ABCDEFGHIJKLMNOPQRSTUVWXYZ"
password = " ".join(random.sample(s,password_length))
print("Password Generated is:",password)