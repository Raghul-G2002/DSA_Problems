def method1(arr):

    #Inplace - Without creating any new array or new datastructure
    current_index = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr[current_index] = arr[i]
            current_index+=1
    print("Using Inplace Method")
    for i in range(0, current_index):
        print(arr[i], end = "\t")
    print(end = "\n")
def method2(arr):

    #Using datastructure - {set} to remove the duplicates and storing it back in the same array
    st = set()
    for i in range(len(arr)):
        st.add(arr[i])
    index = 0
    for i in st:
        arr[index] = i
        index+=1  
    print("Using Secondary Data Structure")
    for i in range(len(st)):
        print(arr[i], end = "\t")

arr = [1, 1, 2, 2, 2, 3, 3]
method1(arr)
method2(arr)