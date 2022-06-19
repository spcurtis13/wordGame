import random

def changeBlanks(guess,secretWord,blanks):
    index = -2
    while(index != -1):
        index = secretWord.find(guess)
        if(index != -1):
            temp = list(blanks)
            temp[index] = guess
            blanks = "".join(temp)
            temp = list(secretWord)
            temp[index] = '*'
            secretWord = "".join(temp)
    return secretWord, blanks


words = ['peanut', 'butter', 'jelly']
secretWord = random.choice(words)
print(secretWord)
incorrectGuessCounter = 0
win = False
blanks = '_' * len(secretWord)
print("This is game is basically hangman you have 8 incorrect guess to get all the letters in the word")
while(incorrectGuessCounter < 9 and win == False):
    print(blanks)
    guess = input("Guess a character\n")
    if(guess in secretWord):
        secretWord, blanks = changeBlanks(guess,secretWord,blanks)

