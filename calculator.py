

Number1 = int(input("Enter a number: "))
Number2 = int(input("Enter another number: "))
operator = input( "+")
if operator == "+":
    print(Number1 + Number2)
elif operator == "-":
    print(Number1 - Number2)
elif operator == "*":
    print(Number1 * Number2)
elif operator == "/":
    print(Number1 / Number2)
else:
    print("Invalid operator")
