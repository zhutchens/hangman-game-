# ***************************************
# file where the game functions are coded
# ***************************************

import random 

def playGame():
    # open dictionary file and read it
    allStrings = open('dictionary.txt').read().splitlines()
    # choose a random word
    word = random.choice(allStrings).lower()
    # print out # of lines corresponding to the length of the word
    completeWord = '_' * len(word)
    # array to store used guesses from the user
    allGuesses = []
    # boolean value to check if the user has already guessed the word
    ifGuessed = False 
    # variable to hold total number of guesses that are availabe to user
    numGuesses = 6
    # print hang man phase from the phase list function using the number of guesses variable to determine the phase
    print(phaseList(numGuesses))
    # print the number of lines
    print(completeWord)
    # start the game using a while loop to determine if the game ends or not
    while (numGuesses > 0 and ifGuessed == False):
        # ask for user input and get a letter
        userGuess = input('Please enter a letter to guess. ')
        # checking if the letter has already been guessed
        if (userGuess in allGuesses):
                # if it has, ask user to enter another letter
                userGuess = input('Already guessed that word. Please enter another. ')
        # make sure letter is valid and isnt a string or number
        while (userGuess not in 'abcdefghijklmnopqrstuvwxyz' or len(userGuess) != 1):
            # if it is, loop the user guess variable until the guess is valid
            userGuess = input('Not a valid guess. Please try again. ')
        # check if the ltter the user guessed is the word
        if (userGuess not in word):
            # decrement number of guesses
            numGuesses -= 1
            # print statement telling user guess is not in the word
            print(userGuess + ' is not in the word. Try again! ')
            # add the letter to the array of guessed letters
            allGuesses.append(userGuess)
            # print current phase of game
            print(phaseList(numGuesses))
            # print number of brackets or letters if user has guessed correct letters
            print(completeWord)
        # check if letter is the in word
        elif (userGuess in word):
            # tell the user that the letter is in the word
            print(userGuess + ' was in the word! Please enter another guess. ')
            # add that letter to the array of guesses
            allGuesses.append(userGuess)
            # find where the user guess occurs in the word
            index = [x for x, letter in enumerate(word) if letter == userGuess]
            # convert complete word to a list 
            listWord = list(completeWord)
            # loop through the index variable to replace each _ with the correct letter
            for i in index:
                # replacing the index with the letter
                listWord[i] = userGuess
            # convert complete word back to string
            completeWord = ''.join(listWord)
            # print current phase 
            print(phaseList(numGuesses))
            # print the number of underlines or letters to the user
            print(completeWord)
            # check if complete word contains underlines, if not then the boolean variable becomes true and game ends
            if ('_' not in completeWord):
                ifGuessed = True

    # checking if the boolean variable is true
    if (ifGuessed == True and numGuesses > 0):
        # tell the user they won if the boolean variable is true
        print('User wins!')
    # if the boolean variable is not true 
    elif (ifGuessed == False or numGuesses == 0):
        # tell the user they did not win
        print('Sorry, you ran out of guesses. The word was '+ word)

# function to store the phases of hangman, with each index corresponding to a phase of the game
def phaseList(numGuesses):
    phases = [  # seventh phase: 6 incorrect letters, game loss
                '''
               --------
               |      |
               |      
               |     
               |    
               |     
               |
               ------------
                ''',
                # sixth phase: 5 incorrect letters, head
                '''
               --------
               |      |
               |      O
               |
               |     
               |     
               |
               ------------
                ''',
                # fifth phase: 4 incorrect letters, head, body
                '''
                --------
                |      |
                |      O
                |      |
                |      
                |      
                |
                ------------
                ''',
                # fourth phase: 3 incorrect letters, head, body, one arm
                '''
               --------
               |      |
               |      O
               |     /|
               |      
               |     
               |
               ------------
                ''',
                # third phase: 2 incorrect letters, head, body, both arms
                '''
               --------
               |      |
               |      O
               |     /|\\
               |      
               |     
               |
               ------------
                ''',
                # ssecond phase: 1 incorrect letter, head, body, both arms, one leg
                '''
                --------
                |      |
                |      O
                |     /|\\
                |     /
                |     
                |
                ------------
                ''',
                # first phase: no incorrect letters
                '''
                --------
                |      |
                |      O
                |     /|\\
                |     / \\ 
                |     
                |
                ------------
                '''
    ]
    # return statement to send back to the play game method
    return phases[numGuesses]
