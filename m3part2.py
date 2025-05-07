def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    while True:
        print("=======Welcome to Temperature Converter!=======\n" 
        "Menu:\n" 
        "1. Convert Celsius to Fahrenheit\n" 
        "2. Convert Fahrenheit to Celsius\n" 
        "3. Exit\n" )

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            temp = float(input("Enter temperature in Celsius: "))
            print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(temp):.2f}\n")
        elif choice == "2":
            temp = float(input("Enter temperature in Fahrenheit: "))
            print(f"Temperature in Celsius: {fahrenheit_to_celsius(temp):.2f}\n")
        elif choice == "3":
            print("Thank you for using Temperature Converter. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")
    
temperature_converter()