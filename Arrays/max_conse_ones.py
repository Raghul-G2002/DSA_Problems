def method(arr):
    ctr = 0
    max_ctr = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            ctr+=1
        else:
            ctr = 0
        max_ctr = max(max_ctr, ctr)
    return max_ctr

arr = [1,0,1,1,0,1]
print(method(arr))