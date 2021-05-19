
def user_calc():
    num1 = int(input("Please enter your first number: "))
    operate = input("What operator do you choose: ")
    num2 = int(input("Please enter your second number: "))
    if operate == "+":
        print(num1 + num2)
    elif operate == "-":
        print(num1 - num2)
    elif operate == "*":
        print(num1 * num2)
    elif operate == "/":
        print(num1 / num2)
    else:
        print("Error")


user_calc()
