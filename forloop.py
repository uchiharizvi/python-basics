n = input("Enter a number: ")
if n.isdigit():
    n = int(n)
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(f" sum: {sum} ")
else:
    print("Invalid input. Please enter a valid number.")
    exit()