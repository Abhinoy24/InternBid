import random
word = []
with open('sowpods.txt','r') as f:
    line = f.readline().strip()
    word.append(line)
    while line:
        line = f.readline().strip()
        word.append(line)

random_index = random.randint(0,len(word))
print("Random Word: ",word[random_index])

'''
guess = "_" * len(word)
word = list(word)
guess = list(guess)

lstguessed = []
letter = input("guess letter:")
while True:
    if letter.upper() in lstguessed:
        letter = ''
        print("Guessed")
    elif letter.upper() in word:
        index = word.index(letter.upper())
        guess[index] = letter.upper()
        word[index] = '_'
    else:
	    print(''.join(guess))
		if letter is not'':
			lstGuessed.append(letter.upper())
		letter = input("guess letter: ")

	if '_' not in guess:
		print("You won!!")
		break
'''