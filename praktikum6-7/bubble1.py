#sort asc
def bubbleshort(data):
    for passnum in range(len(data)-1,0,-1):
        for i in range(passnum):
            if data[i]>data[i+1]:
                #tukar data bersebelahan yang urutannya salah
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp

data = [54,26,93,17,77,31,44,55,20]
bubbleshort(data)
print(data)


#lebih evisien
#sort asc
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]> alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum -1

alist=[110,20,80,50,40,70,30,100,90,60]
shortBubbleSort(alist)
print(alist)
