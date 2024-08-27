from typing import List, Optional
from quick_sort import QuickSort
from radix_sort import RadixSort

class BucketSort:
    """
    Implementation of bucket sort algorithm with a radix sort subroutine.
    """

    @staticmethod
    def sorter(arr: List[int], minimum: Optional[int] = None, maximum: Optional[int] = None) -> List[int]:
        """
        Sorts an array in ascending order using the bucket sort algorithm.

        Args:
            arr (List[int]): The array of elements to be sorted.
            minimum (Optional[int]): The minimum value in the array. If not provided, it will be calculated.
            maximum (Optional[int]): The maximum value in the array. If not provided, it will be calculated.

        Returns:
            List[int]: The sorted array.
        """
        if len(arr) == 0:
            return arr

        # Determine the range of the input array
        min_value = minimum if minimum is not None else min(arr)
        max_value = maximum if maximum is not None else max(arr)
        bucket_range = (max_value - min_value) / len(arr) + 1  # bucket size

        # Create buckets
        buckets = [[] for _ in range(len(arr))]

        # Distribute input array values into buckets
        for num in arr:
            index = int((num - min_value) / bucket_range)
            # Ensure the index is within the correct range
            index = min(index, len(arr) - 1)
            buckets[index].append(num)

        # Sort each bucket using insertion sort and concatenate the results
        sorted_arr = []
        for bucket in buckets:
            sorted_arr.extend(RadixSort.sorter(bucket))

        return sorted_arr




class QuickBucketSort:
    """
    Implementation of bucket sort algorithm with a quicksort subroutine.
    """

    @staticmethod
    def sorter(arr: List[int], minimum: Optional[int] = None, maximum: Optional[int] = None) -> List[int]:
        """
        Sorts an array in ascending order using the bucket sort algorithm.

        Args:
            arr (List[int]): The array of elements to be sorted.
            minimum (Optional[int]): The minimum value in the array. If not provided, it will be calculated.
            maximum (Optional[int]): The maximum value in the array. If not provided, it will be calculated.

        Returns:
            List[int]: The sorted array.
        """
        if len(arr) == 0:
            return arr

        # Determine the range of the input array
        min_value = minimum if minimum is not None else min(arr)
        max_value = maximum if maximum is not None else max(arr)
        bucket_range = (max_value - min_value) / len(arr) + 1  # bucket size

        # Create buckets
        buckets = [[] for _ in range(len(arr))]

        # Distribute input array values into buckets
        for num in arr:
            index = int((num - min_value) / bucket_range)
            # Ensure the index is within the correct range
            index = min(index, len(arr) - 1)
            buckets[index].append(num)

        # Sort each bucket using insertion sort and concatenate the results
        sorted_arr = []
        for bucket in buckets:
            sorted_arr.extend(QuickSort.sorter(bucket))

        return sorted_arr
