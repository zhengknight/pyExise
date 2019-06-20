"""
bubble sort algorithm
"""
def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [2, 5, 1, 3, 70, 30, 10, 8]

result_list = bubbleSort(arr)
print(result_list)
