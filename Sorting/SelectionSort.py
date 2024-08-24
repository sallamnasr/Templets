
# Selection Sort 
# time = O(n^2)
# space = O(1)

def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
        mn = arr[i]
        mn_idx = i 
        for j in range(i + 1, n):
            if arr[j] < mn:
                mn = arr[j]
                mn_idx = j

        if mn < arr[i]:
            arr[i], arr[mn_idx] = arr[mn_idx], arr[i] 

    return arr


Array = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
print(SelectionSort(Array))
