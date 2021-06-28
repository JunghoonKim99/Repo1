
#Bubblesort compares j with j+1 for N times, i.e. after the first iteration the largest
#value should be in the last entry of the list

def BubbleSort(L):
    N = len(L)
    comp = 0
    for i in range(N):
        for j in range(N-i-1):
            comp += 1
            if i > j:
                z = L[i]
                L[i] = L[j]
                L[j] = z
    return L, comp

L1 = [1, 2, 3, 4, 6]
#print(BubbleSort(L1))

def BubbleSortQuicker(L):
    N = len(L)
    changes = 1
    for i in range(N):
        if changes > 0:
           changes = 0
           for j in range(N-i-1):
               if L[j] > L[j+1]:
                changes += 1
                z = L[i]
                L[i] = L[j]
                L[j] = z
    return L

L2 = [1, 3, 2, 4, 6]

#print(BubbleSortQuicker(L2))

#######
'''
def InsertionSort(L):
    assert isinstance(L, list)
    n = len(L)
    comp_total = 0
    if n <= 1: # if L is very short there is nothing to do
                # This will catch lists of length 0 as well
        return L, comp_total
    done = [L[0]]
    for i in range(1,n):
        j  = 0
        while ((j < len(done)) and (done[j] < L[i])):
            j += 1
            comp_total += 1
        done = done[:j] + [L[i]] + done[j:]
    return done, comp_total
'''

def BasicInsertionSort(L):
    K = [L[0]]
    L.remove(L[0])
    NL = len(L)
    NK = len(K)
    for i in range(NL):
        j = 0
        while (j < len(K) and L[i] > K[j]):
            j += 1
        K = K[:j] + [L[i]] + K[j:] 
    '''
    while len(L) >0 :
        for i in range(NK):
            if L[0] < K[i]:
                K[:i] + [L.pop(0)] + K[i:]
    '''##Why does this not work
    return K

#print(BasicInsertionSort(L2))


########
def Insert(k, L):
    assert isinstance(k, int)
    assert isinstance(L, list)
    left = 0
    right = len(L) -1
    if len(L) == 0:
        return [k]
    if len(L) == 1:
        if L[0] > k:
            return [k] + L
        else:
            return L + [k]
    if k > max(L):
        return L + [k]
    if k < min(L):
        return [k] + L
    
    while abs(left-right) > 1:
        m = int((right+left)/2)
        if k > L[m]:
            left = m
        else:
            right = m
    L = L[:right] + [k] + L[right:]
    return L

##The list of length two will not approximate exactly as to how we want thus watch out
##In order to squeeze in between left and right it should be [:right] + L[0] + [right:]

print(Insert(3, [1, 2, 4]))
        
def BisectionSort(L):
    N = len(L)
    K = []
    for i in range(N):
        K = Insert(L[i], K)
    return K

L1 = [3, 7, 4, 5, 1, 2]
print(BisectionSort(L1))


###QuickSort


##If we dont get rid of pivot the recursion will not stop

def QuickSort(L):
    if len(L) <= 1:
        return L
    pivot = L[0]
    Small = []
    Big = []
    for i in range(1, len(L)):
        if L[i] < pivot:
            Small.append(L[i])
        else:
            Big.append(L[i])
    Small = QuickSort(Small)
    Big = QuickSort(Big)
    return Small + [pivot] + Big

print(QuickSort(L1))


###MidQuickSort

def MidQuickSort(L):
    if len(L) <= 1:
        return L
    mid = int(len(L)/2)
    pivot = mid
    Small = []
    Big = []
    for i in range(1, len(L)):
        if L[i] < pivot:
            Small.append(L[i])
        else:
            Big.append(L[i])
    Small = QuickSort(Small)
    Big = QuickSort(Big)
    return Small + [pivot] + Big