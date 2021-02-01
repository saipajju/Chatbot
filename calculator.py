number_1 = int(input('Number1- '))
number_2 = int(input('Number2- '))
operation = input('Which operation? ')
if operation == '*' or "x":
    result_of_x = number_1 * number_2
    print(result_of_x)
elif operation == '+':
    result_of_addition = number_1 + number_2
    print(result_of_addition)
elif operation == "-":
    results_of_subtraction = number_1 - number_2
    print(results_of_subtraction)
elif operation == '/' or '÷':
    results_of_division = number_1 / number_2
    print(results_of_division)