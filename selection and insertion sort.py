# import sys
# A = [87,54,5,6,0,45]
#
# for i in range(len(A)):
#     min_indx = i
#     for j in range(i + 1, len(A)):
#         if A[min_indx] > A[j]:
#             min_indx = j
#     A[i], A[min_indx] = A[min_indx], A[i]
#
# print('Sorted array: ')
# for i in range(len(A)):
#     print("%d" % A[i])

#Insertion sort
def insertion_sort(list1):

    for i in range(1, len(list1)):

        value = list1[i]

        j = i - 1
        while j >= 0 and value < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = value
    return list1


list1 = [10, 5, 13, 8, 2]
print("The unsorted list is:", list1)

print("The sorted list1 is:", insertion_sort(list1))