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

print ("Menu: \n"
       "Add \n"
       "Subtract \n"
       "Multiply \n"
       "Divide \n"
       "Exit \n")

choice = int(input ("Enter your choice (1-5): "))

if choice == 1:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(f"Result: {add(x, y)}")
elif choice == 2:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(f"Result: {sub(x, y)}")
elif choice == 3:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(f"Result: {mul(x, y)}")
elif choice == 4:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(f"Result: {div(x, y)}")    
elif choice == 5:
    print("Thank you for using Simple Calculator!")
else:
    print( "Invalid input. Please enter a valid choice.")
