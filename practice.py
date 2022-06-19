import random

def findall(p,s):
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)

def changeBlanks(guess, secretWord, blanks):
    index = -2
    while(index != -1):
            index = secretWord.find(guess)
            if(-1 < index < len(secretWord)):
                temp = list(blanks)
                temp[index] = guess
                blanks = "".join(temp)
                temp = list(secretWord)
                temp[index] = "*"
                secretWord = "".join(temp)
    return secretWord, blanks

    
words = ['peanut', 'butter', 'jelly']
secretWord = random.choice(words)
blanks = '_' * len(secretWord)
incorrectGuessCounter = 0
win = False
print("This is basically hangman you have 8 guesses of letters and then you lose")
while(incorrectGuessCounter < 9 and win == False):
    print(blanks)
    guess = input("Guess a letter\n")
    if guess in secretWord:
        secretWord, blanks = changeBlanks(guess,secretWord, blanks)
    else:
        incorrectGuessCounter += 1
        print("You're wrong you have " + str(8-incorrectGuessCounter) + " incorrect guesses left")
    if(('_' not in blanks)):
        win = True
print(blanks)
if(win == True):
    print("You're a winner")
else:
    print("You're a loser")
#print(list(findall("a","banana")))





