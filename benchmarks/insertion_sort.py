from typing import List

class InsertionSort:
    """
    Implementation of insertion sort algorithm.
    """

    @staticmethod
    def sorter(arr: List[int]) -> List[int]:
        """
        Sorts an array in ascending order using the insertion sort algorithm.

        Args:
            arr (List[int]): The array of elements to be sorted.

        Returns:
            List[int]: The sorted array.
        """
        # Traverse through 1 to len(arr)
        for i in range(1, len(arr)):
            key = arr[i]
            # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
