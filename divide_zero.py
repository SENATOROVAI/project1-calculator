# функция divide принимает два параметра и проверяет если не ноль


def divide(num1, num2):
    if num1 == 0 or num2 == 0:
        print("Делить на ноль нельзя")
        return None
    return num1 / num2
