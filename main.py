from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#Function to check users guess against the actal answer
def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining"""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


#Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty.Type 'easy or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    #Choose a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("Im thinking of a number between 1 and 100")
    answer = randint(1, 100)
    #print(f"Psst the correct answer is {answer}")

    turns = set_difficulty()

    #Repeating the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #Let the user guess a number
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of gueses. You lose")
            return
        elif guess != answer:
            print("Guess again.")


#TRACK THE NUMBER OF TURNS AND REDUCE IF THEY GET IT WRONG
game()
