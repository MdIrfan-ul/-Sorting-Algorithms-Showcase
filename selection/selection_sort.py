"""This is a module docstring."""
from typing import List

def selection_sort(arr:List[int])->List[int]:
    """looping through index"""
    size=len(arr)
    for index in range(size-1):
        mini=index
        for pos in range(mini+1,size):
            if arr[pos]<arr[mini]:
                mini=pos
            arr[index],arr[mini]=arr[mini],arr[index]

array=[5,4,3,2,1]
selection_sort(array)
print("sorted array------------>:",array)
                