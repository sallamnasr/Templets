
# Merge Sort 
# time = O(nLog(n))
# space = O(n)


def MergeSort(arr) :
    n = len(arr)
    if n == 1 :
        return arr
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    
    L = MergeSort(L)
    R = MergeSort(R)
    
    sortedarr = [0] *n 
    i = 0 
    
    l,r = 0,0 
    lnL = len(L)
    lnR = len(R)
    
    while l < lnL and r < lnR :
        if L[l] < R[r] :
            sortedarr[i] = L[l]
            l += 1
        else :
            sortedarr[i] = R[r]
            r += 1
        i += 1
    while l < lnL :
        sortedarr[i] = L[l]
        l += 1
        i += 1
        
    while r < lnR :
        sortedarr[i] = R[r]
        r += 1
        i += 1
    return sortedarr


Array = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
print(MergeSort(Array))