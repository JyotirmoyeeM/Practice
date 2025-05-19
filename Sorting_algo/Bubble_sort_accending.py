"""Bubble sort algorithm 
    is a sorting algorithm where 
    every element is compare to its immediate adjacent element 
    and then swapped , if sorting condition is not met. 
    Most of the sorting is done either in asending or desending order"""

#Example, write a program to sort elements in list in accesnding order

def bubble_sort(lst):
  size = len(lst)
  # running an outer loop to run bubble_sort condition for each and every element in the lst
  for i in range (size):

    #running an inner loop to imply the condition to the all elemnt in the list
    for j in range(size-1):

      if lst[j] > lst[j+1]:
        lst[j], lst[j+1] = lst[j+1], lst[j]

  return lst

unsorted_lst =[1,9,2,8,3,7]
print(f"Unsorted list : {unsorted_lst}")

sorted_lst = bubble_sort(unsorted_lst)
print(f"Sorted list : {sorted_lst}")
