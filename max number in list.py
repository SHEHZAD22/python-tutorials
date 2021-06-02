# creating empty list
list1 = []

num = int(input("Enter number of elements in list: "))

for i in range(1, num + 1):
    a = int(input("Enter elements: "))
    list1.append(a)

# print maximum element
print("Largest element is:", max(list1))