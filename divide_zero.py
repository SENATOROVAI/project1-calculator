def divide(num1, num2):
    """Check second num by zero"""
    if num2 == 0:
        print("Делить на ноль нельзя")
        return None
    elif num1 == 0:
        return 0
    return num1 / num2
