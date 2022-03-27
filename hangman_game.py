#import the random module
import random


#Define a function welcome
def greetings():
    
    #Define a name variable
    name = input("""
               Welcome: Enter your name:
                """).capitalize()
    
    #Use a decision making process to accept only alphabets as name
    if name.isalpha() == True:
        print(""">> Hi!""",name,"""Simple Instructions
                You will be playing against the computer today.
                The computer will randomly choose a word and you will try to guess what the word is.
                You can always invite your friends for a fun time together
                ==========================================================
                Good Luck! Have fun playing""")
        
           
    else:
        print('Please enter your name using letter only')
        name = input('Enter a game name here:  ')
        print('Hi!',name,'Please go through the rules of the game below')
        

#Define another function play_again
#Add a docstrings
def reset_play():
    
    """function lets you play the game gain"""
    response = input("Would you like to play again? yes/no. Enter 'Y' for Yes or 'N' for No").lower()

    #Create a decision making process
    if response == 'y':
        hangman_game_execute()
    else:
        print('Hope you had fun playing the game. See you next time')
        

#Define another function get_word for generating random words for the user to guess.
#Add a docstrings
def word_fetch():
    """ This function generates the word the user will attempt guessing"""
    words = ['Python', 'cool', 'Weather', 'exciting', 'happy', 'matlab', 'swift', 'ruby', 'julia', 'java', 'quantum',
             'physics', 'entaglement', 'matter', 'relativity', 'string', 'quasar', 'galaxy', 'continuum', 'signal']
    return random.choice(words).lower()

#Define another function game_run()
#Add a docstring if desired

def hangman_game_execute():
    #call the welcome function to get the game running
    greetings()
    
    #Define a variable alpahabet
    alpha = ('abcdefghijklmnopqrstuvwxyz')
    
    #Set guess word to get_word function for a random word to be generated
    word = word_fetch()
    
    #Initiate an empty list for guessed letter
    guess_alpha = []
    
    #Initiate a tries variable for number of tries by the user
    chances = 7
    
    #Set inital guess to false
    cond = False
    
    #Print an empty line
    print()
    
    #Print a guess hint for the user for number of letters contained in the word

    print('The word contains', len(word), 'letters.')
    print(len(word) * '_')
    
    #Initate a while loop and create decisions, taking into consideration if the user decides to enter just a single letter or  the full word
    #Also a create decisions for if user inputs a wrong entry and if user inputs letters and it is not equal to the total number of letters in the word to guess
    #Deduct tries each user fails to guess incorrectly
    while cond == False and chances > 0:
        print('You have ' + str(chances) + ' attempts')
        guess = input('Guess a letter in the word or enter the full word.').lower()
        #user inputs a letter
        if len(guess) == 1:
            if guess not in alpha:
                print('Check whether your entry is a letter not a number.')
            elif guess in guess_alpha:
                print('You have already guessed that letter before.Try again!')
            elif guess not in word:
                print('Sorry, you guessed it wrong :(')
                guess_alpha.append(guess)
                chances -=1
            elif guess in word:
                print('Great! You guessed it right!')
                guess_alpha.append(guess)
            else:
                print('Check your entry!You might have entered the wrong entry')

        #user inputs the full word
        elif len(guess) == len(word):
            if guess == word:
                print('Great Job! You guessed the word correctly!')
                cond = True
            else:
                print('Sorry, that was not the word we were looking for :(')
                chances -= 1

        #user inputs letters and it is not equal to the total number of letters in the word to guess.  
        else:
            print('The length of your guess is not the same as the length of the correct word.')
            chances -=1

        status = ''
        if cond == False:
            for letter in word:
                if letter in guess_alpha:
                    status += letter
                else:
                    status += '_'
            print(status)
           

        if status == word:
            print('Great Job! You guessed the word correctly!')
            cond = True
        elif chances == 0:
            print("Opps! You ran out of attempts and you couldn't guess the word.")
            print(f"The desired word was ")

    #Initiate play_again function if user wishes to continue
    reset_play()

#Full program run
hangman_game_execute()