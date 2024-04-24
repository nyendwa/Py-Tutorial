import MathematicalModules

result_add = MathematicalModules.Addition(2, 4)
result_multiplication = MathematicalModules.Multiplication(7, 3)
print('The sum of num1 and num2 is ', result_add)
print('The product of num1 and num2 is ' + str(result_multiplication))

multiply = lambda num1, num2: num1 * num2
print("The lambda result is ", multiply(6, 7))
