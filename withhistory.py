# Arithmetic functions
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    try:
        return a/b
    except Exception as e:
        print(e)
        return None

def power(a,b):
    return a**b

def remainder(a,b):
    return a%b

# List to store calculation history
history_list = []

# Function to handle operations and history
def select_op(choice):
    global history_list

    if choice == '#':
        return -1
    elif choice == '$':
        return 0
    elif choice == '?':  # Display history
        if not history_list:
            print("No past calculations to show")
        else:
            for item in history_list:
                print(item)
        return 0
    elif choice in ('+','-','*','/','^','%'):
        # Get first number
        while True:
            num1s = input("Enter first number: ")
            if num1s == '#':
                return -1
            if num1s.endswith('$') or num1s == '$':
                return 0
            try:
                num1 = float(num1s)
                print(num1s)
                break
            except ValueError:
                print("Not a valid number,please enter again")

        # Get second number
        while True:
            num2s = input("Enter second number: ")
            if num2s == '#':
                return -1
            if num2s.endswith('$') or num2s == '$':
                return 0
            try:
                num2 = float(num2s)
                print(num2s)
                break
            except ValueError:
                print("Not a valid number,please enter again")

        # Perform calculation
        result = None
        if choice == '+':
            result = add(num1, num2)
        elif choice == '-':
            result = subtract(num1, num2)
        elif choice == '*':
            result = multiply(num1, num2)
        elif choice == '/':
            result = divide(num1, num2)
        elif choice == '^':
            result = power(num1, num2)
        elif choice == '%':
            result = remainder(num1, num2)

        # Format and display result
        last_calc = f"{num1} {choice} {num2} = {result}"
        print(last_calc)

        # Save to history
        history_list.append(last_calc)

        return 0
    else:
        print("Unrecognized operation")
        return 0

# Main calculator loop
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    print("8.History  : ? ")

    choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
    print(choice)

    if select_op(choice) == -1:
        print("Done. Terminating")
        exit()
