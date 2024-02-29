def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while(low <= high):
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1


mar = [24,33,22,12,1,2,8,55,78]
print(binary_search(mar, 2))

