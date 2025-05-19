

def bubble_sort(lst):
    
    size = len(lst)

    #outer loop to go through all the elemts in lst
    for i in range(size):

        #inner loop to imply the bubble sort to all the elemsts
        for j in range(size-1):
            #the bubble sort condition in descending order
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    
    return lst


# take integer inputs and convert it to a list    
data_list = list(map(int, input().split()))

sorted_list = bubble_sort(data_list)
print(sorted_list)
