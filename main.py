# ------------------------------------------------------------------
#  main execution - December 24 2022
# ------------------------------------------------------------------

from rules import playGame

# welcome message to user
print('Welcome to my hang-man game! Developed by zhutchens using Python 311.')

# print out hangman graphic
print( '''
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |     / \\
                   |     
                   |
                   ------------
                ''')
print('                           ')
# print out selection menu with options user can choose
print('***** Selection Menu: *****')
print('Enter 1 to play.')
print('Enter 2 to read the rules of this hang-man game.')
print('Enter 3 to exit the program.')
print('****************************')

# collect user input from the menu
choice = input('')

# check if user entered a number from the menu selection
while (choice not in '123' or len(choice) > 1):
    # if they did not, tell them the input is invalid and to try again
    choice = input('Sorry, you entered an invalid input. Please only enter a number from the menu list. ')

# check if user wanted to play
if (choice == '1' or choice == ' 1'):
    # variable to check if user wants to keep playing
    keepPlaying = 'Y'
    # while loop so user to can decide to keep playing or stop
    while (keepPlaying == 'Y'):
        # play game method from the rules file
        playGame()
        # ask user if they want to play again and collect their input
        keepPlaying = input('Would you like to play again? Enter Y for yes and N for no ').upper()
        # check if user entered a number from the selection
        while (keepPlaying not in 'YN' or len(keepPlaying) > 1):
            # if they did not, tell them the input is invalid and to try again
            keepPlaying = input('Sorry, you entered an invalid input. Please only enter a letter. Y to keep playing and N to stop. ')

    # check if user doesnt wish to keep playing
    if (keepPlaying == 'N'):
        # thank user
        print('Thanks for trying out my program, hope you had fun!')
        # exit program
        exit()

# check if user wanted to read the rules
if (choice == '2' or choice == ' 2'):
    # print out rules 
    print('Rules: ')
    print('1: User will have six total guesses, the game will end win either the user guesses the word or runs out of guesses.')
    print('2: User will not be able to guess the word. Only letters will be accepted in this program.')
    # new variable to collect user input 
    newChoice = input('Would you like to play or exit? Enter 1 to play and 3 for exit ')
    # checking if user entered the correct number to play 
    if (newChoice == '1' or newChoice == ' 1'):
        # variable to keep track of when the user wants to stop playing
        keepPlay = 'Y'
        # while loop to control how long the user can play 
        while (keepPlay == 'Y'):
            # play game method from the rules file
            playGame()
            # ask user if they would like to play again
            keepPlay = input('Would you like to play again? Enter Y for yes and N for no ').upper()
            # check if user entered a number from the selection
            while (keepPlay not in 'YN' or len(keepPlay) > 1):
                # if they did not, tell them the input is invalid and to try again
                keepPlay = input('Sorry, you entered an invalid input. Please only enter a letter. Y to keep playing and N to stop. ')

        # checking if user doesnt want to play
        if (keepPlay == 'N'):
            # thank them for downloading 
            print('Thanks for trying out my program, hope you had fun!')
            # exit program
            exit()
    
    elif (newChoice == '3' or newChoice == ' 3'):
        # thank them for trying out my program
        print('Thanks for trying out my program, hope you had fun!')
        # exit program
        exit()

# check if user wants to exit
if (choice == '3' or choice == ' 3'):
    # thank user for trying it out
    print('Thanks for trying out my program, hope you had fun!')
    # exit program
    exit()

