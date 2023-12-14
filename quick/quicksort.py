"""Importing typing module"""
from typing import List

"""The Algorithm"""


def qsort(arr: List[int], low: int, high: int) -> List[int]:
    """Quick Sort"""
    if low < high:
        partition_Index = quick_sort(arr, low, high)
        qsort(arr, low, partition_Index - 1)
        qsort(arr, partition_Index + 1, high)


"""Quick Sort Algorithm"""


def quick_sort(arr: List[int], low: int, high: int) -> List[int]:
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        while arr[j] >= pivot and j >= low + 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j


if __name__ == "__main__":
    array = [1, 2, 8, 3, 7, 4, 5]
    print(f"unsorted array------->{array}<-----------")
    qsort(array, 0, len(array) - 1)
    print("sorted array--------->", array, "<----------")
