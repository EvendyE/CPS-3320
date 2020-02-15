def letterScore(letter):

    abc = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")

    scoreSets = (("a","e","i","l","n","o","r","s","t","u"),("d","g",),("b","c","m","p"),("f","h","v","w","y"),("k"),("j","x"),("q","z"))
    
    if letter in abc[0:26]:

        if letter in scoreSets[0][0:10]:
            return 1
                
        elif letter in scoreSets[1][0:2]:
            return 2
                
        elif letter in scoreSets[2][0:4]:
            return 3
                
        elif letter in scoreSets[3][0:5]:
            return 4
                
        elif letter in scoreSets[4][0:1]:
            return 5
                
        elif letter in scoreSets[5][0:2]:
            return 8
                
        elif letter in scoreSets[6][0:2]:
            return 10

    else:
        return 0
        

def wordScore(letter,dictionary):

    sum = 0
    
    for i in range(len(letter)):
        sum = sum + dictionary.get(letter[i])

    return sum


#main                      

word = input("Enter a word. " ).lower()

value = []

for i in range(len(word)):

    value.append(letterScore(word[i]))
    
dictionary = dict(zip(word,value))

print("The Scrabble score of this word is", wordScore(word,dictionary))






