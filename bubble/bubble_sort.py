"""Bubble Sort Algorithm"""
from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    """This function takes a list of integers and returns in the sorted order"""
    size = len(array)
    for i in range(size-1):
        swapped = False
        for j in range(0, size-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    arr = [1, 2, 8, 3, 7, 4, 5]
    print(f"unsorted array------->{arr}<-----------")
    bubble_sort(arr)
    print("sorted array--------->", arr, "<----------")
