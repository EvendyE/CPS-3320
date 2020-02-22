import random

# Hangman game! 
 
# Assume the answer is "hangman" 
 
Answer = ['hangman', 'variable','polymorphism', 'encapsulation', 'camelcase', 'object', 'class', 'inheritance', 'extend', 'function', 'overload', 'call', 'pass',
          'return', 'recursion', 'accessor', 'mutator', 'argument', 'index', 'compiler', 'boolean', 'double', 'float', 'long', 'string', 'list', 'dictionary', 'key',
          'value', 'break', 'continue', 'elif', 'range', 'declare', 'initialize', 'extends', 'import', 'syntax', 'interpreter', 'idle', 'python', 'java', 'idle',
          'override', 'private', 'public', 'return']

randomNumber = random.randint(0, len(Answer)-1)

A = Answer[randomNumber]
L = ['_'] * len(A)

incorrectGuessCounter = 6

play = True 
 
while play == True:

    if incorrectGuessCounter == 0:
        play = False
            
    # Ask the user to guess a letter

    letter = str(input("Guess a letter: ").lower())

    # Check to see if that letter is in the Answer

    if letter not in A:

        incorrectGuessCounter = incorrectGuessCounter - 1
        print("BAD GUESS!")
    
    i = 0
    for currentletter in A:

        # If the letter the user guessed is found in the answer,
        # set the underscore in the user's answer to that letter

        if letter == currentletter:

            L[i] = letter

        i = i + 1
        
    # Display what the player has thus far (L) with a space
    # separating each letter

    print(' '.join(str(n) for n in L))

    # Test to see if the word has been successfully completed,
    # and if so, end the loop

    if '_' not in L:

        play = False
        
        print("GREAT JOB!")

    elif incorrectGuessCounter == 0:
        
        play = False
        
        print("GAME OVER! \nThe answer is", A, end='')
        print(".")

        

        
