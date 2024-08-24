
# Insertion Sort 
# time : O(n^2)
# space : O(1)

def InsertionSort(arr) :
    n = len(arr)
    
    for i in range(1,n) :
        for j in range(i,0,-1) :
            if arr[j] < arr[j-1] :
                arr[j] , arr[j-1] = arr[j-1] , arr[j]
            else :
                break
    return arr

Array = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

print(InsertionSort(Array))