from input_data import input_data
from operations import subtract, multiply, add
from divide_zero import divide
from integer_division import int_division 
from mod_division import *


# Рефакторинг кода
def run_calculator():
    while True:
        num1, num2, operator = input_data()

        if operator == "+":
            print(add(num1, num2))
        elif operator == "-":
            print(subtract(num1, num2))
        elif operator == "*":
            print(multiply(num1, num2))
        elif operator == "/":
            print(divide(num1, num2))
        elif operator == "//":
            print(int_division(num1, num2))
        elif operator == "%":
            print(mod(num1, num2))
        else:
            print("ERROR")
            