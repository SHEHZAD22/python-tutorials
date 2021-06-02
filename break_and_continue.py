# i=0
#
# while(True):
#     if i+1<5:
#         i = i +1
#         continue #this control statement jump the loop or condition where continue is placed
#     print(i+1, end=" ")
#     if (i==19):
#        break # stop the loop
#     i = i +1

while(True):
    a = int(input("Enter a number:\n"))
    if a>100:
        print("congrats you have entered a number greater than 100")
        break
    else:
        print("try again\n")
        continue
