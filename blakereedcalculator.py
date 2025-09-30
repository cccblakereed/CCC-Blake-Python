# Chapter 3 Calculator
# Blake Reed
# CIS 202
# 9/9/2025

# Step 1: Ask user for two numbers
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input! Please enter numeric values only.")
    exit()

#Ask user for an operator
operator = input("Enter an operator (+, -, *, /): ")

#Verify valid operator
if operator not in ['+', '-', '*', '/']:
    print("Invalid operator! Only +, -, *, / are allowed.")
    exit()

#Handle division by zero
if operator == '/' and num2 == 0:
    print("Error: Division by zero is not allowed.")
    exit()

#Perform the operation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2

#Display result
print(f"\nYou entered the two numbers {num1} and {num2} and the operator entered was {operator}.")
print(f"The result of {num1} {operator} {num2} is {result}.")
