word = input("Enter the word:")
newword = ''
for i in range(len(word)):
    newword += word[len(word)-i-1]
if newword == word:
    print("Pallindrome")
else:
    print("Not a Pallindrome")