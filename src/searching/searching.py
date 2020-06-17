[1, 3, 5, 7, 9, 10, 13]

# TO-DO: Implement a recursive implementation of binary search


def binary_search(arr, target, start, end):
    # Your code here
    if start <= end:
        mid = (start + end) // 2
        # if target is equal to middle value return that value
        if arr[mid] == target:
            return mid

        # if target is smaller than mid it has to be left
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid-1)

        # if target is larger than mid it has to be right
        else:
            return binary_search(arr, target, mid+1, end)
    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
