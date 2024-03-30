import helpers as cc
while True:
    try:
        num1 = float(input("Enter the first Number: "))
        num2 = float(input("Enter the second Number: "))
        mat_operation = input("Enter Mathematical Operations [+ - * /]")
        try:    
            if mat_operation== '+':
                    res = cc.Mathematical_Operations.Addition(num1, num2)
            elif mat_operation== '-':
                    res = cc.Mathematical_Operations.Subtraction(num1, num2)
            elif mat_operation== '*':
                    res = cc.Mathematical_Operations.Multiplication(num1, num2)
            elif mat_operation== '/':
                    res = cc.Mathematical_Operations.Division(num1, num2)
            else:
                print("You have entered an Invalid operation")
            print("\nResult =", res)
            break
        except ZeroDivisionError:
            print("Division by Zero Error in programming is not possible")
    except ValueError:
        print("You must enter an integer number")