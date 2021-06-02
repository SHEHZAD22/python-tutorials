# swaping of two numbers with the help of third variables
a=int(input("Enter the value of a="))
b=int(input("Enter the value of b="))
temp=a
a=b
b=temp
print("After swapping:")
print("Value of a is",a)
print("Value of b is",b,)

#swaping of two number without the help of third variables
a=int(input("Enter the value of a="))
b=int(input("Enter the value of b="))
a=a+b
b=a-b
a=a-b
print("After swapping:")
print("Value of a is",a)
print("Value of b is",b)


