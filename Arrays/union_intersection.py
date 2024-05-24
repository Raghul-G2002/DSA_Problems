def union1(arr1, arr2):

    #Method 1 - Using Dictionary to find the frequency of the elements
    new_arr = []
    freq = {}
    for i in range(len(arr1)):
        if freq.get(arr1[i]) == None:
            freq[arr1[i]] = 1
        else:
            freq[arr1[i]] += 1
    
    for i in range(len(arr2)):
        if freq.get(arr2[i]) == None:
            freq[arr2[i]] = 1
        else:
            freq[arr2[i]] += 1
    
    for i in freq.keys():
        new_arr.append(i)
    
    return new_arr

def union2(arr1, arr2):

    #Method 2 -  Using set to add all the values of both the arrays
    new_arr = set()
    for i in arr1:
        new_arr.add(i)
    for i in arr2:
        new_arr.add(i)
    
    return_arr = []
    for i in new_arr:
        return_arr.append(i)
    
    return return_arr

def union3(arr1, arr2):

    #Method 3 - Two Pointer Approach
    #Works only when both the arrays are in sorted order
    i, j = 0, 0
    new_arr = []
    while i<len(arr1) and j<len(arr2):
        if arr1[i] <= arr2[j]:
            if len(new_arr) == 0 or new_arr[len(new_arr)-1] != arr1[i]:
                new_arr.append(arr1[i])
            i+=1
        else:
            if len(new_arr) == 0 or new_arr[len(new_arr)-1] != arr2[j]:
                new_arr.append(arr2[j])
            j+=1
    
    #When the size of the arrays are not equal
    while i<len(arr1):
        if len(new_arr) == 0 or new_arr[len(new_arr)-1] != arr1[i]:
            new_arr.append(arr1[i])
        i+=1
    
    while j<len(arr2):
        if len(new_arr) == 0 or new_arr[len(new_arr)-1] != arr2[j]:
            new_arr.append(arr2[j])
        j+=1

    return new_arr

def intersection(arr1, arr2):
    new_arr = []
    freq = {}
    for i in range(len(arr1)):
        if freq.get(arr1[i]) == None:
            freq[arr1[i]] = 1
        else:
            freq[arr1[i]] += 1

    for i in arr2:
        if freq.get(i) != 0:
            new_arr.append(i)
            freq[i] -= 1
    
    return new_arr



arr1 = [1,2,3,4,5]
arr2 = [2,3,4,4,5]
# print(union1(arr1, arr2))
# print(union2(arr1, arr2))
# print(union3(arr1, arr2))  
print(intersection(arr1, arr2)) 