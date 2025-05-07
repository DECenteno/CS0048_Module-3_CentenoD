import random
tasks = []
grades = {}
number_to_guess = 0
def add(x, y):
    return x + y

def sub(x, y):
    if y < x:
        return x - y
    else:
        return "Error! First number must be bigger than the second."

def mul(x, y):
    return x * y

def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def add_task(task):
    if task in tasks:
        print("Task already exists.")
    else:
        tasks.append(task)
        print("Task added.")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed.")
    else:
        print("Task not found.")

def view_tasks():
    if tasks:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks in the list.")

def generate_number():
    global number_to_guess
    number_to_guess = random.randint(1, 100)

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
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

def add_score(subject, score):
    grades[subject] = score
    print("Score added.")

def calculate_average():
    if grades:
        average = sum(grades.values()) / len(grades)
        print(f"Average Grade: {average:.2f}")
    else:
        print("No scores to average.")

def calculator_menu():
    print("\nCalculator Menu:\n"
          "1. Add\n"
          "n2. Subtract\n"
          "3. Multiply\n"
          "4. Divide\n")
    
    choice = input("Enter your choice (1-4): ")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    if choice == "1":
        print(f"Result: {add(x, y)}")
    elif choice == "2":
        print(f"Result: {sub(x, y)}")
    elif choice == "3":
        print(f"Result: {mul(x, y)}")
    elif choice == "4":
        print(f"Result: {div(x, y)}")
    else:
        print("Invalid choice.")

def temperature_converter():
    print("\nTemperature Converter:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n")
    choice = input("Enter your choice (1-2): ")
    temp = float(input("Enter temperature: "))
    if choice == "1":
        print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(temp):.2f}")
    elif choice == "2":
        print(f"Temperature in Celsius: {fahrenheit_to_celsius(temp):.2f}")
    else:
        print("Invalid choice.")

def todo_list():
    print("\nTo-Do List:")
    view_tasks()
    task = input("Enter a task to add: ")
    add_task(task)

def grade_calculator():
    print("\nGrade Calculator:")
    subject = input("Enter the subject: ")
    score = float(input("Enter the score: "))
    add_score(subject, score)
    calculate_average()

def main_menu():
    while True:
        print("\n=== Compiled Programs ===\n"
              "1. Calculator\n"
              "2. Temperature Converter\n"
              "3. To-Do List\n"
              "4. Number Guessing Game\n"
              "5. Grade Calculator\n"
              "6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            calculator_menu()
        elif choice == "2":
            temperature_converter()
        elif choice == "3":
            todo_list()
        elif choice == "4":
            generate_number()
            guess_number()
        elif choice == "5":
            grade_calculator()
        elif choice == "6":
            print("Thank you for using the Combined Utility Program!")
            break
        else:
            print("Invalid input. Please try again.")

main_menu()
