primeslist = []
with open('PrimeNumber.txt') as primefile:
    line = primefile.readline()
    while line:
        primeslist.append(int(line))
        line = primefile.readline()
        
happylist = []
with open('HappyNumber.txt') as happyfile:
    line = happyfile.readline()
    while line:
        happylist.append(int(line))
        line = happyfile.readline()
overlaplist = []

for elem in primeslist:
    if elem in happylist:
        overlaplist.append(elem)

print(overlaplist)