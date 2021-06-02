list1 = [1,2,3,4,5]
new_list2 = list(filter(lambda
                            x: (x%2 == 0),list1))
print(new_list2)