# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for x in arr[cur_index:]:
            if arr[cur_index] > x:
                if arr[smallest_index] > x:
                    smallest_index = arr.index(x)

        # TO-DO: swap
        if cur_index != smallest_index:
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
            # arr[smallest_index] = arr[i]

    return arr

new_arr = [9,8,7,6,5,4,3,2,1]
print(selection_sort(new_arr))
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    has_swapped = True
    while has_swapped:
        has_swapped = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                has_swapped = True
    return arr
arr = [9,8,7,6,5,4,3,2,1]
print(bubble_sort(arr))
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr