def add(x, y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide (x,y):
    return x / y

print("Select operation:")
print("+")
print("-")
print("*")
print("/")

num1 = float(input("Enter first number:"))
choice = input("Enter choice(+/-/*//):")
num2 = float(input("Enter second number:"))


if   choice =='+':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '-':
     print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '*':
     print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '-':
     print(num1,"/",num2,"=", divide(num1,num2))

else: print("invalid input")
