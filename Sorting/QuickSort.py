
# Quick Sort
# time : O(nLog(n)) in avrage
# time : O(n^2) in worst case
# space : O(n)

def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    mid = arr[-1]
    L = [x for x in arr[:-1] if x <= mid]
    R = [x for x in arr[:-1] if x > mid]

    L = QuickSort(L)
    R = QuickSort(R)

    return L + [mid] + R


Array = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
print(QuickSort(Array))
