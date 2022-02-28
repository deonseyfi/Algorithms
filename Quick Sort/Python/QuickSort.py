
def quickSort(low,high,arr):
    if high > low:
        pivot_index = partition(low,high,arr)
        quickSort(low, pivot_index - 1, arr)
        quickSort(pivot_index + 1, high, arr)
        

def partition(low,high,arr):
    pivot = arr[low]
    j = low
    for i in range(low+1,high+1):
        if arr[i] < pivot:
            j += 1
            arr[i] , arr[j] = arr[j], arr[i]
    arr[low] , arr[j] = arr[j], arr[low]
    return j    
    


if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    quickSort(0, len(arr)-1, arr)
    print(arr)
