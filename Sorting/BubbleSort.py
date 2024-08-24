# Bubble Sort :
# time = O(n^2)
# space = O(1)

def BubbleSort(arr):
    flag = True
    n = len(arr)

    while flag:
        flag = False
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                # increasing order -> for decreasing {arr[i]>arr[arr[i-1]]}
                flag = True
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                # increasing order -> for decreasing {arr[i]>arr[arr[i-1]]}
                arr[i], arr[j] = arr[j], arr[i]
    return arr


Array = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
print(BubbleSort(Array))
print(bubble_sort(Array))
