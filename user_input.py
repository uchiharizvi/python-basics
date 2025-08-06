name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age.isDigit():
    age = int(age)
    print (f"Hello, {name}! You are {age} years old. Next year, you will be {age + 1}. Keep going strong!")
    