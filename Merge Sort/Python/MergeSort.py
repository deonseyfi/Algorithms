'''
Merge Sort is a divide and conquer algorithm that trys to divide the array into
smaller arrays then, merges them based on the order.

Time Complexity : O(N log N)

Steps:
1. Divide the array into two smaller arrays by half using the middle position.

2. Conquer the solution by sorting each subarray.

3. Merge the solution of each subarray into a single array.
'''

'''
This is a recursive solution for the merge sort algorithm.
@params: the input array
@returns: none
'''
def mergeSort(arr):
    if len(arr) > 1:
        h = len(arr) // 2

        left = arr[:h]
        right = arr[h:]

        mergeSort(left)
        mergeSort(right)

        merge(left,right,arr)
    
'''
This is the function that merges the two subarrays into, the single array, it
also sorts the arrays.
@params: left subarray, right subarray, to be sorted array
@returns: none
'''
def merge(left,right,arr):
    i,j,k = 0,0,0
    while (i < len(left) and j < len(right)):
        if left[i] < right[j]:
            arr[k] = left[i]
            i+= 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i+= 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


'''
Create tests for possible lists passed through the mergeSort Method.
Contraints.
0 <= arr[i] <= 1000. arr[i] is not unique in the list.
1 <= n <= 100 possible size of the lists
'''
import random
import unittest
class TestBinarySearch(unittest.TestCase):
    def testMethods(self):
        for i in range(100):
            size = random.randint(1,100)
            arr = []
            for j in range(size):
                value = random.randint(0,1000)
                arr.append(value)
            compare_arr = arr.copy()
            compare_arr.sort()
            mergeSort(arr)
            self.assertEqual(arr,compare_arr,"Did not produce the correct solution for array recursivly.")


if __name__ == "__main__":
    unittest.main()
  
