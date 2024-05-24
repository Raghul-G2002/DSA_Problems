import sys
def method1(arr):
    # Sorting the Array and find the second largest element
    arr.sort()
    return arr[len(arr)-2]

def method2(arr):
    #Efficient method to find the second largest element
    maxi = -(sys.maxsize)
    for i in range(len(arr)):
        maxi = max(maxi, arr[i])
    
    secmaxi = -(sys.maxsize)
    for i in range(len(arr)):
        if arr[i]>secmaxi and arr[i] != maxi:
            secmaxi = arr[i]
    
    return secmaxi

arr = [1,2,3,4,5,6,-1,-2]
print(method1(arr))
print(method2(arr))