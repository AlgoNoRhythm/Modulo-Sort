import random
from typing import List

class QuickSort:
    """
    Implementation of quicksort algorithm.
    """

    @staticmethod
    def sorter(arr: List[int]) -> List[int]:
        """
        Sorts an array in ascending order using the quicksort algorithm.

        Args:
            arr (List[int]): The array of elements to be sorted.

        Returns:
            List[int]: The sorted array.
        """
        QuickSort._quicksort(arr, 0, len(arr) - 1)
        return arr

    @staticmethod
    def _quicksort(arr: List[int], low: int, high: int) -> None:
        """
        The main quicksort algorithm that recursively sorts elements before and after partition.

        Args:
            arr (List[int]): The array of elements to be sorted.
            low (int): The starting index.
            high (int): The ending index.
        """
        if low < high:
            pi = QuickSort._partition(arr, low, high)
            QuickSort._quicksort(arr, low, pi - 1)
            QuickSort._quicksort(arr, pi + 1, high)

    @staticmethod
    def _partition(arr: List[int], low: int, high: int) -> int:
        """
        Helper function that selects a random pivot, places it in the correct position
        in the sorted array, and places all smaller elements to the left of the pivot and all
        greater elements to the right.

        Args:
            arr (List[int]): The array of elements to be sorted.
            low (int): The starting index.
            high (int): The ending index.

        Returns:
            int: The partitioning index.
        """
        # Select a random pivot index between low and high
        pivot_index = random.randint(low, high)
        # Swap the pivot with the last element
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
