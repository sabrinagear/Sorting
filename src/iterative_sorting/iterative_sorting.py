# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for e in range (i+1, len(arr)): #for each element in range iterator+1 through len of array
            if arr[e] < arr[smallest_index]: #check if array[element] is less than array of small i
                smallest_index = e #if so, set that element to be the small i
        if smallest_index != cur_index: #if iterator is not equal to small i
            arr[cur_index],arr[smallest_index] = arr[smallest_index],arr[cur_index] #swap positions
        
    return arr

test = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(selection_sort(test))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    b = True
    while b:
        b = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                x = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = x
                b = True
    return arr

print(bubble_sort(test))
print(bubble_sort(['a','z','d','o']))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr