import random

def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("The computer will pick a random number between 1 and 100.")
    print("You need to guess the number!")
    print("Choose a difficulty level to determine how many attempts you get.")

def select_difficulty():
    difficulty = ""
    while difficulty not in ["easy", "medium", "hard"]:
        difficulty = input("Select difficulty (easy, medium, hard): ").lower()
    
    if difficulty == "easy":
        return 10
    elif difficulty == "medium":
        return 7
    elif difficulty == "hard":
        return 5

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Invalid input. Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def play_game():
    welcome_message()
    
    random_number = random.randint(1, 100)
    attempts = select_difficulty()
    attempts_left = attempts
    
    while attempts_left > 0:
        print(f"\nYou have {attempts_left} attempts left.")
        guess = get_user_guess()
        
        if guess == random_number:
            print(f"Congratulations! You've guessed the correct number {random_number} in {attempts - attempts_left + 1} attempts.")
            break
        elif guess < random_number:
            print("The number is greater than your guess.")
        else:
            print("The number is less than your guess.")
        
        attempts_left -= 1
    
    if attempts_left == 0:
        print(f"\nYou've run out of attempts! The correct number was {random_number}. Better luck next time!")

if __name__ == "__main__":
    while True:
        play_game()
        replay = input(f"Continue? y/n").lower()
        if replay != 'y':
            print("Quit")
            break
