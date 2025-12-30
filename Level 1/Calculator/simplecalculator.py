#addition operation
def add(a,b):
   return a + b

#subtraction operation
def sub(a,b):
   return a - b

#multiplication operation
def multi(a,b):
   return a * b

#division operation
def div(a,b):
   if b == 0 :
      return "Error: division by zero is not allowed"
   return a / b

#SIMPLE CALCULATOR
print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")


#choose an operator
op = input("Choose an operator(1/2/3/4):")


#enter the values
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

if op == "1":
   print("Result is:", add(num1,num2))
elif op == "2":
   print("Result is:", sub(num1,num2))
elif op == "3":
   print("Result is:", multi(num1,num2))
elif op == "4":
   print("Result is:", div(num1,num2))
else:
   print("Invalid Choice")