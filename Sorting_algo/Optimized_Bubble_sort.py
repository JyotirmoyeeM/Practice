"""
I will be writing the optimized version of Bubble Sort.

In the basic Bubble Sort implementation, we use an outer loop to repeatedly run an inner loop that compares and swaps elements. However, after each pass, the largest unsorted element moves to its correct position. So, there's no need to recheck the sorted portion in the subsequent passes.

Also, in many cases, the list might become sorted before all the passes are completed, but the loop still continues unnecessarily. To improve efficiency, we will apply two optimizations:

1. Reduce the number of inner loop comparisons after each pass by shrinking the range — since the last elements are already sorted.
2. Introduce a boolean flag (`swapped`). If no swap happens during a pass, it means the list is already sorted, so we can break early and skip remaining iterations.

This will help reduce the overall number of comparisons and improve performance for nearly sorted inputs.
"""
def bubble_sort(lst):
    size = len(lst)
    for i in range(size):
        Swapped = False
        for j in range(size-1-i):
            #optimization 1, here i decreased the range by number of iteration
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                Swapped = True
        if not Swapped:
            break
        
    return lst
    
#data = list(map(int, input().split()))
data = [9, 8, 5, 4, 3, 2]
accending_order_data = bubble_sort(data)
print(accending_order_data)




"""
Here,
 the time complexity is O(n2) and 
the space complexity is O(1)  
Bubble Sort is an in-place sorting algorithm, 
so it uses only a constant amount of extra space (e.g., for temp variables and flags like swapped).
"""
