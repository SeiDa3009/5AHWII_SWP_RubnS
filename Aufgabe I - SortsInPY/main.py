def bubblesort (mlist):
    n = len(mlist)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if mlist[j] > mlist[j+1]:
                mlist[j], mlist[j+1] = mlist[j+1], mlist[j]
    print(mlist)
def insertionsort (mlist):
    for i in range(1, len(mlist)):
        key = mlist[i]
        j = i-1
        while j >= 0 and key < mlist[j]:
            mlist[j+1] = mlist[j]
            j -= 1
        mlist[j+1] = key
    print(mlist)

def selectionsort (mlist):
    for i in range(len(mlist)):
        min = i
        for j in range(i+1,len(mlist)):
            if mlist[min] > mlist[j]:
                min = j
        mlist[i], mlist[min] = mlist[min], mlist[i]
    print(mlist)

if __name__ == "__main__":
    nlist = [1,2,5,6,3,9,7,8,0,4]
    bsortlist = bubblesort(nlist)
    nlist = [1,2,5,6,3,9,7,8,0,4]
    isortlist = insertionsort(nlist)
    nlist = [1,2,5,6,3,9,7,8,0,4]
    ssortlist = selectionsort(nlist)
