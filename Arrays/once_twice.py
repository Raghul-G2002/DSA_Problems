def method1(arr):

    #Method 1 - Brute Force Approach
    for i in range(len(arr)):
        ctr = 0
        temp = arr[i]
        for j in range(len(arr)):
            if temp == arr[j]:
                ctr+=1
        if ctr == 1:
            return arr[i]
    return -1

def method2(arr):

    #Method2 - Hashing Frequency
    freq = {}
    for i in range(len(arr)):
        if freq.get(arr[i]) == None:
            freq[arr[i]] = 1
        else:
            freq[arr[i]] += 1

    for i in freq.keys():
        if freq[i] == 1:
            return freq[i]
    return -1

def method3(arr):

    #Use XOR
    xor = 0
    for i in range(len(arr)):
        xor = xor^arr[i]
    return xor


arr = [2,2,1]
print(method1(arr))
print(method2(arr))
print(method3(arr))              