#Bubble Sort
arr = [50,90,150,3,1,56,77,31,12]

#create a copy of the array

arr_copy = arr[:]

#loop through the array
#Loop thru the array length from index 0 to the last index
for i in range(len(arr_copy)):
    #loop therough each index
    #0 rep the 1st index, -1 rep the last index
    for j in range(0,len(arr_copy)-1):
        #compare the two indcese
        if arr_copy[j] > arr_copy[j+1]:
            #swap the two indcese
            arr_copy[j], arr_copy[j+1] = arr_copy[j+1],arr_copy[j]
print('The original list = ', arr)
print('The sorted list = ', arr_copy)
