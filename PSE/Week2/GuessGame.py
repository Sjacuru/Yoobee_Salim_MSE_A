import random

def guessGame():
    word = random.choice(['goaal', 'staairs', 'paaint'])
    guess = []
    tries = []

    for letter in range(len(word)):
        guess.append("_")
    print(guess)

    lives = 10
    total = []
    partial = []
    
    while lives>0: 
        userGuess = input("Guess a letter: ")
        print("Chosen letter: ", userGuess)
    
        for i in range(len(total)):
            if userGuess == total[i]:
                


            

        total.append(userGuess)   
        print("Total", total)     
            
       

        for letter in range(len(word)):
            if word[letter] == userGuess:
                partial.append(word[letter]) 
            elif word[letter] != userGuess:
                partial.append("_") 
        print(partial)
        print("Remaining lives", lives)
        lives -= 1



        #if letter%2 == 0:
        #    guess.append("_")
        #else:    
        #    guess.append(word[letter])
        
        #print (guess)
                


        #al = random.randrange(len(word))
        #print(al)
        #if al/2 == 0:
        #    guess[letter] = word[letter-1]
        #    print("Control", guess)
            #if letter == 0:
            #    i = 1
            #elif letter == len(word):
            #    i = len(word) - 1
    

if __name__ == "__main__":
    ans = guessGame()