# Heap

maxHeap = [None, 99, 72, 61, 58]

print(maxHeap)

def insertValueInHeap(maxHeap:list, value):
    maxHeap.append(value)
    childIndex = len(maxHeap)-1
    parentIndex = len(maxHeap)-1
    while parentIndex>1:
        parentIndex = childIndex // 2
        if maxHeap[parentIndex] < maxHeap[childIndex]:
            temp = maxHeap[parentIndex]
            maxHeap[parentIndex] = maxHeap[childIndex]
            maxHeap[childIndex] = temp
            childIndex = childIndex // 2
        else:
            break
    return maxHeap

def removeValueFromHeap(maxHeap:list):
    temp = maxHeap[1]
    maxHeap[1] = maxHeap[len(maxHeap)-1]
    maxHeap[len(maxHeap)-1] = temp

    maxHeap.pop()
    idx = 1
    while idx < len(maxHeap):
        if(idx < len(maxHeap) and idx*2<len(maxHeap) and idx*2+1 < len(maxHeap)):
            if(maxHeap[idx*2] > maxHeap[idx*2+1] and maxHeap[idx*2] > maxHeap[idx]):
                temp = maxHeap[idx]
                maxHeap[idx] = maxHeap[idx*2]
                maxHeap[idx*2] = temp
                idx = idx*2
            elif(maxHeap[idx*2+1] > maxHeap[idx*2] and maxHeap[idx*2+1] > maxHeap[idx]):
                temp = maxHeap[idx]
                maxHeap[idx] = maxHeap[idx*2+1]
                maxHeap[idx*2+1] = temp
                idx = idx*2+1
            else:
                break
        else:
            break
    return maxHeap

print(insertValueInHeap(maxHeap, 100))
print(insertValueInHeap(maxHeap, 75))
maxHeap1 = [None, 80, 75, 65, 55, 50, 60]
maxHeap2 = [None, 95, 75, 80, 55, 60, 50, 65]

print(maxHeap2)
print(removeValueFromHeap(maxHeap2))
print(removeValueFromHeap(maxHeap2))

# print(maxHeap[7])