number = input("Enter score: ")
if(number.isdigit() and int(number) >= 0 and int(number) <= 100):
    number = int(number)
    if number >= 90:
        print("A")
    elif number >= 80 and number <= 89:
        print("B")
    elif number >= 70 and number <= 79:
        print("C")
    elif number >= 60 and number <= 69:
        print("D")
    else:
        print("F")
else:
    print("Invalid input. Please enter a number between 0 and 100.")           