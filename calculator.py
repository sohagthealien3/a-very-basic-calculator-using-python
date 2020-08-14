Number1 = float(input("Enter your first Number here: "))
Operator = input("Enter your Operator here: ")
Number2 = float(input("Enter your second Number here: "))

if Operator == "+":
    print(Number1 + Number2)
    
elif Operator == "-":
    print(Number1 - Number2)
    
elif Operator == "*":
    print(Number1 * Number2)
    
elif Operator == "/":
    print(Number1 / Number2)
    
else:
    print("Invalid Character! Try Again!! ")
