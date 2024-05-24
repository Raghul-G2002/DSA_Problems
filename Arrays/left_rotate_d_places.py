def method1(arr, d):

    #Rotate an array using three arrays by splitting 
    #First denormalize the d value
    d = d%len(arr)

    temp  = [0]*d

    #Step 1 - Storing the first part of the array
    for i in range(0, d):
        temp[i] = arr[i]

    #Step 2 - Traversing the Second Part of an array and swapping its position
    for i in range(d, len(arr)):
        arr[i-d] = arr[i]
    
    #Step 3 - Appending the Temp array elements to the end of the array
    for i in range(0,d):
        arr[len(arr)-d+i] = temp[i]
    
    return arr

def method2(arr, d):

    #Efficient Method - Reversal Algorithm
    def rotate(arr, left, right):
        while left<=right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left+=1
            right-=1
    rotate(arr, 0, d-1)
    rotate(arr, d, len(arr)-1)
    rotate(arr, 0, len(arr)-1)
    return arr

arr1 = [1,2,3,4,5,6,-1,-2]
arr2 = [1,2,3,4,5,6,-1,-2]
print(method1(arr1,3))
print(method2(arr2,3))