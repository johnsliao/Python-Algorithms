list = [5,1,4,2,3]

def topDownSplitMerge(A, iBegin, iEnd, B):
    if iEnd - iBegin < 2:
        return

    iMiddle = (iEnd + iBegin) / 2

    topDownSplitMerge(A, iBegin, iMiddle, B)
    topDownSplitMerge(A, iMiddle, iEnd, B)
    topDownMerge(A, iBegin, iMiddle, iEnd, B)
    copyArray(B, iBegin, iEnd)

def topDownMerge(A, iBegin, iMiddle, iEnd, B):
    i, j = iBegin, iMiddle

    for k in range(iBegin, iEnd):
        print A[i], A[j], A[k]
        print i,j,k
        if i < iMiddle and (j >= iEnd or A[i] <= A[j]):
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1

def copyArray(B, iBegin, iEnd):
    for k in range(iBegin, iEnd):
        list[k] = B[k]

topDownSplitMerge(list, 0, len(list), list)
print list