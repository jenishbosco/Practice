import sys

def findMinMax(arr):
    max = min = arr[0]

    for i in range(1,len(arr)):
        if arr[i] > max:
            max = arr[i]
        elif arr[i] < min:
            min = arr[i]

    print("The minimum element in the array is: ", min)
    print("The maximum element in the array is: ", max)

arr = [5,7,2,4,9,6]
findMinMax(arr)    