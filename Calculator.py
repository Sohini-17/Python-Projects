def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def avg(a,b):
    return (a+b)/2

print("Choose an Operation:\n" \
      "1. Addition\n" \
      "2. Subtraction\n" \
      "3. Multiplication\n" \
      "4. Division\n" \
      "5. Average")

select = int(input("Select option from above: "))

say1 = float(input("Enter 1st num: "))
say2 = float(input("Enter 2nd num: "))

if select == 1:
    print(say1,"+",say2,"=",add(say1, say2))

elif select == 2:
    print(say1,"-",say2,"=", sub(say1, say2))

elif select == 3:
    print(say1,"X",say2,"=", multiply(say1, say2))

elif select == 4:
    print(say1 ,"/",say2,"=", divide(say1, say2))

elif select == 5:
   print("("say1,"+",say2,")","/","2","=", avg(say1, say2))

else:
    print("Invalid option")
