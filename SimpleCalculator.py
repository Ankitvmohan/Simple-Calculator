#import art,  This is just to show the art of a calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
} 

def calculator():
    #print(art.logo)        this is to print the logo of the Calculator
    accumulate = True
    num1 = float(input("Enter your first number: "))

    while accumulate: 
        
        for symbols in operations:
            print(symbols)

        operation_symbol = input("Enter your choice of operation: ")
        num2 = float(input("Enter your second number: "))
        answer = operations[operation_symbol](num1,num2)
        print(f"{answer}")

        choice = input(f"If you need to continue type  'y', else type 'n' for a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            accumulate = False
            print("\n"*5)
            calculator()        #This is used for Recursion

calculator()




