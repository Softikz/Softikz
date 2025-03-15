def calculator():
    while True:
        operation = input('Введите действие(+,-,*,/,выход):')
        if operation == 'выход':
            break
        if operation in('+','-','*','/'):
            num1 = float(input('Введите первое число:'))
            num2 = float(input('Введите второе число:'))
            if operation =='+':
                print(num1+num2)
            elif operation == '-':
                print(num1-num2)
            elif operation == '*':
                print(num1*num2)
            elif operation == '/':
                print(num1/num2)
        else:
            print('Невереная операция(')
calculator()