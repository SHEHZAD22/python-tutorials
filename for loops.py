# list1 = ["shehzad","bilal","intzar","sarfraj","sahraj"]
# list1 = [["shehzad",1],["bilal",2],["intzar",3],["sarfraj",5],["sahraj",6]]
# dict1 = dict(list1)
# print(dict1)
# for item,marks in dict1.items():
#     print(item,marks)
list = [int,float,"shehzad",3,5,6,76,87,45,67]
for item in list:
    if str(item).isnumeric() and item > 6:
        print(item)