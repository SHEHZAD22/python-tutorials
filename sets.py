# s_from_list=set([1,2,3,4])
# print(s_from_list)
# print(type(s_from_list))
s = set()
s.add(1)    #for adding the elements in the set we use add function
s.add(2)
# # s1 = s.union({1,2,3})
# s1 = s.intersection({1,2,3})
# print(s,s1)

s1 = {4,6}
print(s.isdisjoint(s1))
print(s.issubset(s1))
print(s.issuperset(s1))
