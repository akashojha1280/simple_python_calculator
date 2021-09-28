def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    print("Choose 1 for Add")
    print("Choose 2 for Subtract")
    print("Choose 3 for Multiply")
    print("Choose 4 for Divide")
    user_selection = input("Select 1, 2, 3, or 4: ")

    if user_selection in ('1', '2', '3', '4'):
        num1 = float(input("First number in: "))
        num2 = float(input("Second number in: "))

        if user_selection == '1':
            print(num1, " + ", num2, " = ", add(num1, num2))

        elif user_selection == '2':
            print(num1, " - ", num2, " = ", subtract(num1, num2))

        elif user_selection == '3':
            print(num1, " * ", num2, " = ", multiply(num1, num2))

        elif user_selection == '4':
            print(num1, " / ", num2, " = ", divide(num1, num2))

        run_again = input("Would you like to run another calculation? (yes/no): ")

        if run_again == "no":
            break;

    else:
        print("Invalid Input")
