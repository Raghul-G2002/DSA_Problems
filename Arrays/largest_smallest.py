import sys
def method1(arr):
    # Sorting the Array and getting the last element and first element
    arr.sort()
    return arr[-1], arr[0]

def method2(arr):
    # Using the Max Variable and Min Variable
    maxi = -(sys.maxsize)
    for i in range(len(arr)):
        if arr[i]>maxi:
            maxi = arr[i]
    
    mini = sys.maxsize
    for i in range(len(arr)):
        if arr[i]<mini:
            mini = arr[i]
    
    return mini, maxi


arr = [1,2,3,4,5,6,-1,-2]
print(method1(arr))
print(method2(arr))