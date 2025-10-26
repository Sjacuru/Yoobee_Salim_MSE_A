import random

def inputCheck(userGuess,guess, lives):
    if len(userGuess) != 1:
        print("Enter only one letter at a time")
        print("You still have", lives, "lives")
        print(guess)
        return True
    elif not userGuess.isalpha():
        print("Numbers are not valid, please enter a letter")
        print("You still have", lives, "lives")
        print(guess)
        return True
    return False

def ctrlCount (userGuess, attemptsLst, lives, guess):
    if userGuess in attemptsLst:
        print("You already tried this letter")
        print("You still have", lives, "lives")
        print(guess)
        return True
    
def ctrlLst (userGuess, word):
    if userGuess not in word:
        return True

def gameOverMsg (lives):        
    if lives == 0:
        return True    

def guessGame():
    # Create a random word and store it in word variable
    word = random.choice(['goal', 'stairs', 'paint'])

    # Create blank spaces for the word to be guessed
    guess = []
    attemptsLst = []

    for letter in range(len(word)):
        guess.append("_")
    print(guess)

    # Number of attempts for the guessing user
    lives = 10

    while lives > 0: 
        userGuess = input("Guess a letter: ").lower()

        if inputCheck(userGuess,guess, lives):    
            continue
        
        if ctrlCount(userGuess, attemptsLst, lives, guess):
            continue
        elif ctrlLst (userGuess, word):
            lives -= 1
            print("You have", lives, "lives remaining")
            print(guess)
            if gameOverMsg(lives):
                print("Game Over. Try again")  
            attemptsLst.append(userGuess)
            continue

        # Check for matches in the chosen word
        for i in range(len(word)):
            if userGuess == word[i]:
                guess[i] = word[i]

        print(guess)
        print("You have", lives, "lives remaining")

        if "_" not in guess:
            print("Congratulations! You got it!!! The word was:", word)
            break

if __name__ == "__main__":
    guessGame()
