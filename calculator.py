from input_data import input_data
from operations import subtract, multiply, add
from divide_zero import divide


# Рефакторинг кода
def run_calculator():2
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
        else:
            raise ValueError("division by zero")
        
