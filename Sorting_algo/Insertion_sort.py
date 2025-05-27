"""
Insertion Sort is a comparison-based sorting algorithm.

It divides the list into a sorted and an unsorted part. 
Initially, the first element is considered sorted. 
Then, one by one, it picks elements from the unsorted part and places them at the correct position in the sorted part.

👉 For ascending order:
We keep moving left while the current value (key) is smaller than the value on its left.
We stop when we find a value smaller than or equal to the key.

👉 For descending order:
We reverse the comparison.

This continues until all elements are placed in the correct position.
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        # we are iterating this loop from 1, because we are assuming arr[0] is part of sorted sublist
        key = arr[i] #right side
        j = i - 1 #left side
        
        #impplying the condition that when j is moving to left side it dos not reaches to condition 0 or -1 so j>=0
        # while key moving to wards right as it looses one of its element oward left side  it will stay in limits of j so key > arr[j]
        while j>=0 and key > arr[j]:
            arr[j+1], = arr[j]
            j -=1 #moving j to more of its left side manually
        arr[j+1] = key
    return arr
arr= [5,6,4,2,1]
sorted_arrray = insertion_sort(arr)
print(sorted_arrray)
