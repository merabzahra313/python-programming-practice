#Basic Calculator

try:
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    print("Addition: ", a+b)
    print("Subtraction: ",a-b)
    print("Multiplication: ",a*b)
    if b!=0:
        print("Division: ", a/b)
    else:
        print("Cannot possible")
except ValueError:
    print("Please enter valid number")

#Even or Odd
try:
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

except ValueError:
    print("Please enter an integer")

#Age Checker
try:
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You are eligible to vote")

    else:
        print("You are not eligible to vote")

except ValueError:
    print("Please enter a valid age")


#Largest Number
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))

    if a >= b and a >= c:
        print("Largest number:", a)

    elif b >= a and b >= c:
        print("Largest number:", b)

    else:
        print("Largest number:", c)

except ValueError:
    print("Please enter valid numbers")


#Temperature Converter
try:
    celsius = float(input("Enter temperature in Celsius: "))

    fahrenheit = (celsius * 9/5) + 32

    print("Temperature in Fahrenheit:", fahrenheit)

except ValueError:
    print("Please enter a valid temperature")


#Calculator Using if/elif/else
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        print("Result:", a + b)

    elif operator == "-":
        print("Result:", a - b)

    elif operator == "*":
        print("Result:", a * b)

    elif operator == "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")

    else:
        print("Invalid operator")

except ValueError:
    print("Please enter valid numbers")

#Multiplication Table
try:
    num = int(input("Enter a number: "))

    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

except ValueError:
    print("Please enter an integer")

#Factorial
try:
    num = int(input("Enter a number: "))

    if num < 0:
        print("Factorial is not defined for negative numbers")

    else:
        fact = 1

        for i in range(1, num + 1):
            fact = fact * i

        print("Factorial:", fact)

except ValueError:
    print("Please enter an integer")

#Prime Number
try:
    num = int(input("Enter a number: "))

    if num <= 1:
        print("Not a prime number")

    else:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print("Prime number")
        else:
            print("Not a prime number")

except ValueError:
    print("Please enter an integer")

#Number Reversal
try:
    num = int(input("Enter a number: "))

    original = abs(num)
    reverse = 0

    while original > 0:
        digit = original % 10
        reverse = reverse * 10 + digit
        original = original // 10

    if num < 0:
        reverse = -reverse

    print("Reversed number:", reverse)

except ValueError:
    print("Please enter an integer")


#Number Guessing Game
import random

secret_number = random.randint(1, 100)

guess = 0
attempts = 0

while guess != secret_number:

    try:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")

        elif guess > secret_number:
            print("Too high! Try again.")

        else:
            print("Congratulations! You guessed correctly.")
            print("Total attempts:", attempts)

    except ValueError:
        print("Please enter a valid integer")


#Fibonacci Series
try:
    n = int(input("Enter number of terms: "))

    if n <= 0:
        print("Enter a positive number")

    else:
        a = 0
        b = 1

        for i in range(n):
            print(a, end=" ")

            c = a + b
            a = b
            b = c

except ValueError:
    print("Please enter an integer")


#Armstrong Number
try:
    num = int(input("Enter a number: "))

    if num < 0:
        print("Negative numbers are not Armstrong numbers")

    else:
        original = num
        digits = len(str(num))
        total = 0

        while num > 0:
            digit = num % 10
            total = total + digit ** digits
            num = num // 10

        if total == original:
            print("Armstrong number")
        else:
            print("Not an Armstrong number")

except ValueError:
    print("Please enter an integer")


#Login System

correct_username = "admin"
correct_password = "12345"

attempts = 0

while attempts < 3:

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        break

    else:
        attempts += 1
        remaining = 3 - attempts

        if remaining > 0:
            print("Incorrect credentials!")
            print("Attempts remaining:", remaining)

        else:
            print("Access blocked! Too many attempts.")


#Input Validator
user_input = input("Enter a number or text: ")

try:
    number = float(user_input)

    print("You entered a number:", number)
    print("Square:", number ** 2)
    print("Double:", number * 2)

except ValueError:
    if user_input.strip():
        print("You entered text:", user_input)
        print("Uppercase:", user_input.upper())
        print("Lowercase:", user_input.lower())
    else:
        print("Empty input is not allowed")