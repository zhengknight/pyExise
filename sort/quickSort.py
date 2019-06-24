#encoding=gbk
"""
快速排序练习
快速排序将列表分为左右2部分，每部分继续使用快速排序算法，因此用递归实现
"""
def quick_sort(arr):
    if arr==[]:
        return []
    else:
        first = arr[0]
        left=quick_sort([l for l in arr[1:] if l<first])
        right=quick_sort([r for r in arr[1:] if r>=first])
        return left + [first] + right

arr=[2,5,1,7,9,4]
result_list=quick_sort(arr)
print(result_list)
