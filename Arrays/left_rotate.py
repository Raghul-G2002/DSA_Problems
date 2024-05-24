def method1(arr):

    #Using an external array -- O(n) has the space complexity
    temp = [0]*(len(arr))
    for i in range(1, len(arr)):
        temp[i-1] = arr[i]
    temp[len(arr)-1] = arr[0]

    return temp

def method2(arr):

    #Without using external array -- O(1) has the space complexity
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = temp

    return arr

arr1 = [1,2,3,4,5,6,-1,-2]
arr2 = [-2,-1,1,2,3,4,5,6]
print(method1(arr1))
print(method2(arr1))

print(method1(arr2))
print(method2(arr2))
