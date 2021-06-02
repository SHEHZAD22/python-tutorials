        # In this tutorials we're gonig to learn about IF ELSE
# var1 = 6
# var2 = 56
# var3 = int(input())
#
# if var3 > var2:
#     print("greater")
# elif var3==var2:
#     print("equal")
# else:
#     print("Lesser")

# list1 = [5,7,3]
# print(5 in list1)   #in: fucntion is used to check the elment if it is inside the variables
# if 5 in list1:
#     print("Yes, it in the list")
# print(6 not in  list1)
# if 6 not in  list1:
#     print("NO, its not in the list")

print("What is your age?")
age = int(input())
if 18 < age < 100:
    print("You are able to drive")
elif age == 18:
    print("We cannot decide right now.You have to visit in our given location.\n\"Thank you\" ")
elif age < 18:
    print("You are not able to drive")
else:
    print("Error:\nPlease enter valid age")