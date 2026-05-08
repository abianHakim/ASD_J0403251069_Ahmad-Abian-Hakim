#============================================================================
#sorting data   : Quick Sort (asc)
#Nama           : Ahmad Abian Hakim
#NIM            : J0403251069
#============================================================================

def quickSort(data):
    process(data,0,len(data)-1)

def process(data,kiri,kanan):
    if kiri < kanan :

        splitpoint = partitionData(data,kiri,kanan)

        process(data,kiri,splitpoint - 1)

        process(data,splitpoint+1,kanan)

def partitionData(data,kiri,kanan):
    pivotvalue = data[kiri]

    leftmark = kiri + 1
    rightmark = kanan
    done = False

    while not done:

        while leftmark <= rightmark and data[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while data[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True

        else:
            temp = data[leftmark]
            data[leftmark] = data[rightmark]
            data[rightmark] = temp
    
    temp = data[kiri]
    data[kiri] = data[rightmark]
    data[rightmark] = temp

    return rightmark

data = [8,3,10,2,7]

quickSort(data)

print(data)