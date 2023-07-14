def divide(num1, num2):
    if not (num1 and num2): # но ты здесь не проверяешь переменную на 0 
        print("Делить на ноль нельзя")
        return None
    
    return num1 / num2
