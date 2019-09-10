# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    if arrA[0] > arrB[0]:
        merged_arr = list(arrB + arrA)
    else:
        merged_arr = list(arrA + arrB)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
import math

def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        left = []
        right = []
        pivot = arr[0]

        for i in arr[1:]:
            if i <= pivot:
                left.append(i)
            else: 
                right.append(i)
        return list(merge_sort(left) + [pivot] + merge_sort(right))

    return arr
arr = [4,3,2,5,6,12,34,3,4]

print(merge_sort(arr))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
