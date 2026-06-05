import random
secret_number = random.randint(1, 10)
number = 0
attempts = 0
while number != secret_number:
    number = int(input("Guess the number!"))
    attempts = number + 1
    if number > secret_number:
        print("Too high!")
    elif number < secret_number:
        print("Too low!")
print(f"You got it bro in {attempts} attempts!")

        




