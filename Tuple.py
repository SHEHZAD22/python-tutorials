# # tupel in python
# t=(9,7,6)
# # they are  called immutable: which cannot be modified again and can't be updated again
# and the other operation which was performed on the list can be performed on the tuple
# t[2]=5
# print(t)

# set  in python :
# tupel can be involved in set but list cannot be involved it shows error(because list is mutable i.e can be updated again
# s1={5,8,8,10,"you",8.11,(4,3),[6,7],2,1}
# indexing cannot be performed on set
# s1[1]
# print(s1)

# set does not involve the repetation value
# set is a unordered collection and it is a data structure
# s={4,5,6,8,9,9}
# print(len(s))
# print(sorted(s))
# print(max(s))
# print(min(s))
# print(type(s))
# s.add(7)
# print(s)

# for adding multiple values we need to consider the values in the curly braces
# s.update({89,87})
# print(s)

# for removing items#if the items exist ..it simply remove the items and if does not exist ...gives error#
# s={4,7}
# s.remove(4)
# print(s)


# s={4,5,8,"bilal"}
# s.discard(9) #if the items exist ..it simply remove the items and if does not exist print the result#
# print(s)
# s3={ "bilal",2,3,4,5}
# s3.pop()
# print(s3)


# s1={3,4,5,2}
# s2={4,5,2,7}
# s1=s1.union(s2)
# print(s1)
# s1=s1.intersection(s2)
# print(s1)
# s1=s1.difference(s2)
# print(s1)


# Dictionary is a collection which is unordered, changeable,and indexed
dict={"name":"bilal","sem":6}
dict1={1:2,3:4,5:6}
print(dict.values())
print(dict.keys())
print(dict1)
dict1.pop(3)   #in dictionary pop is used when we provide the item in the brackets
print(dict1)
