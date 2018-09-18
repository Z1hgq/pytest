#coding=utf-8
def getMaxIndex(arr):
    i = 0
    maxIndex = 0
    max = arr[0]
    while(i < len(arr)):
        if arr[i] > max:
            max = arr[i]
            maxIndex = i
        i = i + 1
    return maxIndex

arr = [1,2,4,5,2,3,4]
print(getMaxIndex(arr))