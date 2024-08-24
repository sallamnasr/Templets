

# Counting Sort
# Time = O(n+k) where k is the avrage of the date
# space = O(k)

def CountingSort(arr):
    n = len(arr)
    mx = max(arr)
    counts = [0] * (mx+1)

    for x in arr:
        counts[x] += 1

    i = 0
    for c in range(mx+1):
        while counts[c] > 0:
            arr[i] = c
            i += 1
            counts[c] -= 1
    return arr

Array = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

print(CountingSort(Array))
