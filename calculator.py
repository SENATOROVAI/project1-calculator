from input_data import input_data
from operations import subtract, multiply, add
from divide_zero import divide
from mod_division import *


# Рефакторинг кода
def run_calculator():
    while True:
        num1, num2, operator = input_data()

        operations = {"+": add, "-": subtract, "*": multiply, "/": divide, "%": mod}  # Вынес все операции между числами в словарь, ключи - знаки операций
        if opertor not in operations:  # Проверка, если оператора нету в словаре
            print("ERROR")

        print(operations[operator](num1, num2))  # Забираем ссылку на функцию со словаря по ключю, вызываем и передаем аргументы

        # if operator == "+":
        #     print(add(num1, num2))
        # elif operator == "-":
        #     print(subtract(num1, num2))
        # elif operator == "*":
        #     print(multiply(num1, num2))
        # elif operator == "/":
        #     print(divide(num1, num2))
        # elif operator == "%":
        #     print(mod(num1, num2))
        # else:
        #     print("ERROR")
            
