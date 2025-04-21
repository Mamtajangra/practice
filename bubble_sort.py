# define a function 
def bubble_sort(arr):
    # loop on lenth of array 
    for i in range(len(arr)):
        # now checking the internal elements also 
        for j in range(len(arr)-i-1):
            # now check the condition 
            if arr[j] > arr[j+1]:
                # swapping 
                arr[j] ,arr[j+1] = arr[j+1], arr[j]





# main
array = [12,21,11,1,5,2,8,5,9,4] 
bubble_sort(array)
print(array)