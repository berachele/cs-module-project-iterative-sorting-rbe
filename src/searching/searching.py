def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr)-1
    while low <= high:
        middle = int((low+high)/2) #<-- infinite loop of number is lower, inifinite loop of NUMBER IS HIGHER if I do (low+high)//2
        if target < arr[middle]:
            high = middle -1
        elif target > arr[middle]:
            low = middle +1
        else:
            return middle
    return -1  # not found
