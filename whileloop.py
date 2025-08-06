secret_number = 7
guess = int(input("Guess the number: "))
while (guess != secret_number):
    if(guess < secret_number):
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess the number: "))
    
print("Correct!")