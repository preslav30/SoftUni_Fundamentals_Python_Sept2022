def factorial_calc(n):
    factor = 1
    for num in range(1, n + 1):
        factor *= num
    return factor


def factorial(n1, n2):
    number1 = factorial_calc(n1)
    number2 = factorial_calc(n2)
    division = number1 / number2
    return f"{division:.2f}"


num1, num2 = int(input()), int(input())
print(factorial(num1, num2))
