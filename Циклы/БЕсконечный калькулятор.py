num1 = float(input())
num2 = float(input())
oper = input('оператор')
while oper !='c':
    if oper == '*':
        print('Ответ:',num1*num2)
    elif oper == '+':
        print('ОТвет:',num1+num2)
    elif oper == '-':
        print('ОТвет:',num1-num2)
    elif oper == '/':
        print('ОТвет:', num1 / num2)
    else:
        print()
    num1 = float(input())
    num2 = float(input())
    oper = input('оператор')
