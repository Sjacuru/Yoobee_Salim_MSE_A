import random

def guessGame():
    # Create a random word and store it in word variable
    word = random.choice(['goal', 'stairs', 'paint'])
    count = 0

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

        # Check if one letter only was given and if it was not a number
        if len(userGuess) != 1:
            print("Enter only one letter at a time")
            print("You still have", lives, "lives")
            print(guess)
            continue
        elif not userGuess.isalpha():
            print("Numbers are not valid, please enter a letter")
            print("You still have", lives, "lives")
            print(guess)
            continue

        # Check if the letter was already used and count how many attempts occurred 
        if userGuess in attemptsLst:
            print("You already tried this letter")
            print("You still have", lives, "lives")
        elif userGuess not in word:
            lives -= 1
            print("You have", lives, "lives remaining")
        else:
            count += 1
        attemptsLst.append(userGuess)

        # Check for matches in the chosen word
        for i in range(len(word)):
            if userGuess == word[i]:
                guess[i] = word[i]

        print(guess)
        print("You have", lives, "lives remaining")

        if lives == 0:
            print("Game Over. Try again")

        if "_" not in guess:
            print("Congratulations! You got it!!! The word was:", word)
            break

if __name__ == "__main__":
    guessGame()