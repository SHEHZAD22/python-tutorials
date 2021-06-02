# list1 = [['shehzad',57],['bilal',83],['sahraj',90],['sarfraj',73],['intzar',95]]
#
# for item,value in list1:
#     if (item == 'bilal') :
#         print(item,"and the marks is:",value)


# list2 = (('shehzad',99),('bilal',98),('sahraj',34),('intzar',54))
# for item in list2:
#     print(item)list1 = [['shehzad',57],['bilal',83],['sahraj',90],['sarfraj',73],['intzar',95]]

list3 = [1,'shehzad',76,'hi',89,34,23,90,'hello','nand','bilal','98']
for item in list3:
    if str(item).isnumeric() and item=='98':
        print(item)
