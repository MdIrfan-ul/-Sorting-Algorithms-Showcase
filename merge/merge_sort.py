"""merge sort algorithms"""
"""This Algorithm can be approached in two ways"""

"""The Approach"""


def merge_sort(arr, low, high):
    """merge sort"""
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge1(arr, low, mid, high)


"""The Algorithm Approach start here"""


def merge1(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    for i in range(low, high + 1):
        arr[i] = temp[i - low]


"""The Second Way for merge sort algorithm"""


def merge2(arr):
    """The alternative method for merge sort"""
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge2(left)
        merge2(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


if __name__ == "__main__":
    array = [5, 4, 3, 2, 1]
    merge_sort(array, 0, len(array) - 1)
    merge2(array)
    print("Sorted---->", array, "<----")
    print("Sorted---->", array, "<----")
