def occurInBothSorted(A,B):
    i = 0
    j= 0
    k = 0
    lenA = len(A)
    lenB = len(B)

    if lenA < lenB:
        rA = [None] * lenB
    else:
        rA = [None] * lenA
    
    lenC = len(rA)
    while i < lenA and j < lenB and k < lenC:
        if A[i] == B[j]:
            if A[i] != rA[k]:
                    rA[k] = A[i]
                    k = k + 1
                    j = j + 1
                    i = i + 1
        elif A[i] < B[j]:
            i = i + 1
        else:
            j = j + 1
        
    fA = rA[:k]
    return fA

# some tests, but you can add your own ones as well
tests = (([1,3,5,5,17,17,23,24,31,56,57],[3,5,5,10,23,23,37,42,56]),
         ([1,3,5,5,17,17,23,24,31,56,57],[4]),
         ([4],[4,7,8,31,42]),
         ([],[4,7,8,31,42]),
         ([4],[]))

for (A,B) in tests: print(occurInBothSorted(A,B))