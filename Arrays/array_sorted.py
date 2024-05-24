def check_sorted1(arr):
    #Using nested loop to check whether the array is sorted or not -- less efficiency
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                return False
    return True

def check_sorted2(arr):
    #Using single array to check whether the array is sorted - Efficient Solution
    for i in range(1, len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True

arr1 = [1,2,3,4,5,6,-1,-2]
arr2 = [-2,-1,1,2,3,4,5,6]
print(check_sorted1(arr1))
print(check_sorted2(arr1))

print(check_sorted1(arr2))
print(check_sorted2(arr2))