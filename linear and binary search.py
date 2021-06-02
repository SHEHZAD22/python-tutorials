# def linearsearch(arr, x):
#    for i in range(len(arr)):
#       if arr[i] == x:
#          return i
#          return -1
# arr = ['R','E','K','H','A','M','A','M']
# x = 'K'
# print("Element found at index "+str(linearsearch(arr,x)))


#binary search
def bin_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1

# Test Array
arr = [2,8,89,54,0,100]
x = int(input("Enter the given above any number: "))

result = bin_search(arr, x)
if result != -1:
    print("Element is found at index ", str(result))
else:
    print("Error! Please check your input")