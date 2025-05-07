import random
number_to_guess = 0

def generate_number():
    global number_to_guess
    number_to_guess = random.randrange(1, 100)

def guess_number():
    guess = 0
    attempts = 0

    while guess != number_to_guess:
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts.")

def show_menu():
    print("*******Welcome to the Number Guessing Game!*******")
    print("1. Play the Game")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        generate_number()
        guess_number()
    elif choice == "2":
        print("Goodbye!")
    else:
        print("Invalid choice. Try again.")
        show_menu()  

show_menu()
