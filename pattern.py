n=int(input("enter the number="))
k=2*n-2
for i in range(0,n):

    for j in range(0,k):
        print(end=' ')
    k = k - 2
    for j in range(0,i+1):
        print("*" ,end=' ')
    print(" ")
#pattern for pyramid
n=int(input("\nenter the number="))
k=2*n-1
for i in range(0,n):

    for j in range(0,k):
        print(end=' ')
    k = k - 1
    for j in range(0,i+1):
        print("*" ,end=' ')
    print(" ")
