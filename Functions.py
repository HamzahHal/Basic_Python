
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


def square(n1):

    return n1 * n1


print("1. Add")
print("2. Subtract")
print("3. Divide")
print("4. Multiple")
print("5. Squared")

choice = input("Choose operator number: ")

if choice == '5':
    n1 = float(input("Enter number you'd like to square: "))
elif choice == '1':
    n1 = float(input("insert first value: "))
    n2 = float(input("insert second value: "))
elif choice == '2':
    n1 = float(input("insert first value: "))
    n2 = float(input("insert second value: "))
elif choice == '3':
    n1 = float(input("insert first value: "))
    n2 = float(input("insert second value: "))
elif choice == '4':
    n1 = float(input("insert first value: "))
    n2 = float(input("insert second value: "))

result = ''

if choice == '1':
    result = add(n1, n2)
elif choice == '2':
    result = sub(n1, n2)
elif choice == '3':
    result = divide(n1, n2)
elif choice == '4':
    result = multiply(n1, n2)
elif choice == '5':
    result = square(n1)
print(result)
