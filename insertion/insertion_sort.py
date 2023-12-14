"""Insertion sort Algorithm"""
"""we can sort this algorithm in two ways"""



def insertion_sort(array):
    """insertion sort"""
    size = len(array)
    for i in range(1, size):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


"""The Second Way"""

def insertion_sort2(array):
    """sorting two"""
    size = len(array)
    for i in range(1, size):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1


if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    insertion_sort(arr)
    print("Sorted Array---->", arr, "<---")
    insertion_sort2(arr)
    print("Sorted Array---->", arr, "<---")
