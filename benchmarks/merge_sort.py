from typing import List


class MergeSort:
    """
    Implementation of merge sort algorithm.
    """

    @staticmethod
    def sorter(arr: List[int]) -> List[int]:
        """
        Sorts an array in ascending order using the merge sort algorithm.

        Args:
            arr (List[int]): The array of elements to be sorted.

        Returns:
            List[int]: The sorted array.
        """
        if len(arr) <= 1:
            return arr

        # Find the middle point and divide the array into two halves
        middle = len(arr) // 2
        left_half = arr[:middle]
        right_half = arr[middle:]

        # Sort each half recursively
        left_sorted = MergeSort.sorter(left_half)
        right_sorted = MergeSort.sorter(right_half)

        # Merge the sorted halves
        return MergeSort._merge(left_sorted, right_sorted)

    @staticmethod
    def _merge(left: List[int], right: List[int]) -> List[int]:
        """
        Merges two sorted lists into a single sorted list.

        Args:
            left (List[int]): The sorted left half list.
            right (List[int]): The sorted right half list.

        Returns:
            List[int]: The merged and sorted list.
        """
        sorted_list = []
        left_index, right_index = 0, 0

        # Compare elements from both halves and merge them in sorted order
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                sorted_list.append(left[left_index])
                left_index += 1
            else:
                sorted_list.append(right[right_index])
                right_index += 1

        # Collect the remaining elements from both halves
        sorted_list.extend(left[left_index:])
        sorted_list.extend(right[right_index:])

        return sorted_list
