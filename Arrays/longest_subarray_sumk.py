def method1(arr,nok):

    #Method1 - Brute Force Method
    length = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum = 0
            for k in range(i,j+1):
                sum+=arr[k]
            if sum == nok:
                length = max(length, j-i+1)
    return length

def method2(arr,nok):

    #Method2 -  Better Approach
    length = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum+= arr[j]
            if sum == nok:
                length = max(length,j-i+1)
    return length

def method3(arr, nok):

    #Method3 - Optimal Approach
    length = 0
    mpp = {}
    sum = 0
    mpp[sum] = 1
    for i in range(len(arr)):
        sum+=arr[i]

        if sum == nok:
            length = i+1
        else:
            rem = nok-sum
            if rem in mpp:
                length = max(length, i-mpp[rem])
            else:
                mpp[sum] = i
    return length


arr = [2,3,5,1,9]
nok = 10
print(method1(arr,nok))
print(method2(arr,nok))
print(method3(arr,nok))