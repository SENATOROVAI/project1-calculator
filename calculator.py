def run_calculator():
    while True:
      num1, num2, operator = input_data()
      
        if operator == '+':
           print(num1 + num2)
        elif operator == '-':
           print(num1 - num2)
        elif operator == '*':
           print(num1 * num2)
        elif operation == '/':
                result = divide(num1, num2)
                if result is not None:
                    print(num1 / num2)
        elif operation == '**':
           print(num1 ** num2)
        else:
           print('ERROR')
           continue 


     
