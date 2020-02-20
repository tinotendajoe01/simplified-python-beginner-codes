num1 = int(input("enter a number: "))
num2 = int(input("enter another number:  "))
op = input("enter the mathematical operation you want to use: ")


def cal(num1, num2):
    if op == "+":
        return (num1 + num2)
    elif op == "-":
        return (num1 - num2)
    elif op == "/":
        return (num1 / num2)
    elif op == "*":
        return (num1 * num2)
    elif op == "**" or "^":
        def pow(num1, num2):
            result = 1
            for i in range(num2):
                result = result * num1
            return result

        print(pow(num1, num2))
print(cal(num1,num2))