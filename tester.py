def binaryInsert(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2               
        if target < arr[mid]:
            high = mid - 1
        elif target > arr[mid]:
            low = mid + 1
        else:
            return mid
    return low



arr = []
payload = [2, 3, 1, 6, 2, 1, 8, 2, 1]

for n in payload:
    idx = binaryInsert(arr, n )
    print(idx)
    arr.insert(idx, n)
    print(arr)
    
