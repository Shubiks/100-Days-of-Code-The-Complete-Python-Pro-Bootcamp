def add(n1, n2):
    """This function takes two numbers and returns their sum."""
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

dictionary = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

def calc():
    repeat = True
    ans = 0
    first_number = int(input("Enter the First Number: "))
    while repeat:
        print("Select Operation")
        for key in dictionary:
            print(key)
        operation = str(input())
        second_number = int(input("Enter the Second Number: "))
        if operation == '+':
            ans = dictionary['+'](first_number,second_number)
        elif operation == '-':
            ans = dictionary['-'](first_number,second_number)
        elif operation == '*':
            ans = dictionary['*'](first_number,second_number)
        elif operation == '/':
            ans = dictionary['/'](first_number,second_number)
        print(f"{first_number} {operation} {second_number} = {ans}")
        a = str(input(f"press y if you want to continue with {ans} or n for new calculation ")).lower()
        if a == 'y':
            first_number = ans
        else:
            print("\n"*20)
            calc()

calc()





