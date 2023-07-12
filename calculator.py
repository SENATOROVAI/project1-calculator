from input_data import input_data
from operations import subtract
from divide_zero import divide

def run_calculator():
    while True:
      
         num1, num2, operation = input_data()

         # if operation == "+":
         #    print(num1 + num2)
         if operation == "-":
            print(subtract(num1, num2))
      #   elif operation == "*":
      #       print(num1 * num2)
      #   elif operation == "/":
         #   result = divide(num1, num2)
         #   if result is not None:
          #      print(num1 / num2)
      #  elif operation == "**":
      #      print(num1**num2)
      #  else:
      #      print("ERROR")
      #      continue
