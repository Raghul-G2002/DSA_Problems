def method1(arr):

    #Method1 - Using Linear Search
    for i in range(max(arr)):
        if i+1 not in arr:
            return i+1

def method2(arr):
    #Uses Hashing
    freq = {}
    for i in range(len(arr)):
        if freq.get(arr[i]) == None:
            freq[arr[i]] = 1
        else:
            freq[arr[i]]+=1
    for i in range(max(arr)):
        if i+1 not in freq:
            return i+1
    return -1

def method3(arr):
    #Summation of series 1+2+3+4+....+n = n(n+1)//2
    s1 = (max(arr)*(max(arr)+1))//2
    s2 = sum(arr)
    return s1-s2

def method4(arr):
    xor1, xor2 = 0,0
    for i in range(max(arr)):
        xor1 = xor1^(i+1)
    for i in range(len(arr)):
        xor2 = xor2^arr[i]
    return xor1^xor2

arr = [4,2,1,5]
print(method1(arr))
print(method2(arr))
print(method3(arr))
print(method4(arr))