# # simple for loop
# a = ('hi')
# for i in a:
#     print(i)
# else:
#     print("Loop terminated")
#
# #for loop with range
# # for i in range(5):
# # for i in range(1,5):
# # for i in range(1,10,2):
# # for i in range(10,0,-2):
# for i in range(2,11,2):
#     print(i)
#
# # for loop with else
# print("Table of 2 is: ")
# for i in range(2,20,2): #range(2,20,2) ---> this will print from 2 to 18 by stepping two steps or we can say that will print the table of two
#     print(i)
# else:
#     print("table printed....thanks for using our program\n\"Have a good day\"")
#
# st = "SHEHZAD"
# n = len(st)
# for i in range(n):
#     print(i,'=',st[i])
# else:
#     print("bye")
#
a = ("the wonderful women kings wife and the wonderful king is queen husband and queen is the wife of king is the husband of the wife the wife is the dughter of the king father and the king son of the wife father sothis matter is on the supreme court i cannot amaing this mentality so i not consulting of this case put on the high and supreme court who is father king father say i am the fayher you are the father and you  marriage our son and why what do you think and what do you ask your hair color is pink so youre monster this called adjurned")
res = len(a.split()) #split() function is used for counting words in any given sentence
print("No. of words are: ",(res))

b = "hi shehzad hello"
count = len(b.split())
print(count)
