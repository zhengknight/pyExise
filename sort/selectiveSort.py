def selectiveSort(arr):
    for i in range(1,len(arr)):
        min_num=arr[i-1]
        for j in range(0,len(arr)-i):
            if arr[j]>arr[j+1]:
                min_num=arr[j+1]
        arr[i-1]=min_num

    return arr

arr=[2,5,1,7,9,4]
result_list=selectiveSort(arr)
print(result_list)