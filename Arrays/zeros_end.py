def method1(arr):
    # Brute force approach
    new_arr = []
    for i in arr:
        if i > 0:
            new_arr.append(i)
    for i in range(len(arr)-len(new_arr)):
        new_arr.append(0)
    
    return new_arr

def method2(arr):

    #Without the use of new array
    i, j = 0, 1
    while i<len(arr) and j<len(arr):
        if arr[i] == 0:
            if arr[j] != 0:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                i+=1
                j+=1
            else:
                j+=1
        else:
            i+=1
            j+=1
    return arr

arr = [1,0,2,0,3,0,4,5,0]
print(method1(arr))
print(method2(arr))