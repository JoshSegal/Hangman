import random
from words import words
from hangman_visual import lives_visual_dict
import string

def getValidWord(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()

def hangman():
    word = getValidWord(words)
    wordLetters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    usedLetters = set() #what the user has guessed
    
    lives = 7
    
    #getting user input
    while len(wordLetters) > 0 and lives > 0:
        #letters used
        #' '.join(['a', 'b', 'cd'])
        print('You have', lives, 'lives left and you have used these letters: ',' '.join(usedLetters))
        
        #what current word is ( W - R D)
        wordList = [letter if letter in usedLetters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(wordList))
        
        userLetter = input('Guess a letter: ').upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            
            else:
                lives = lives -1
                ('Letter is not in word.')
                
        elif userLetter in usedLetters:
            print('You have already guessed that letter. Please choose a different letter.')    
        else:
            print('You have entered an invalid character')
    
    #userInput = input('Type something: ')
    
    
    ##gets here when len(wordLetters) == 0 or when lives == 0 
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry! The word was ', word)
    else:    
        print ('Yay! You guessed the word', word, '!!')
 
hangman()