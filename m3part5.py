grades = {}

def add_score(subject, score):
    grades[subject] = score
    print("Score added.")

def calculate_average():
    if grades:
        average = sum(grades.values()) / len(grades)
        print(f"Average Grade: {average:.2f}")
    else:
        print("No scores to average.")

def grade_calculator():
    while True:
        print("\n===Student Grade Calculator===\n"
              "1. Add Score\n"
              "2. Calculate Average\n"
              "3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            subject = input("Enter the subject: ")
            score_input = input("Enter the score: ")
            
            if score_input.replace('.', '', 1).isdigit():  # checks for float values too
                score = float(score_input)
                add_score(subject, score)
            else:
                print("Invalid score. Please enter a number.")
                
        elif choice == "2":
            calculate_average()
        elif choice == "3":
            print("Thank you for using Student Grade Calculator!")
            break
        else:
            print("Invalid input. Please try again.")

grade_calculator()
