first_number = int(input("what is ur first number?"))    
second_number = int(input("what is ur second number?"))
operator = input("what is ur operator? (+,-,*,/)")
if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    result = first_number / second_number
else:
    result = "invalid operator"
print(f"result is {result}")


