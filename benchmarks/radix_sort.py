from typing import List, Optional
from counting_sort import CountingSortRadix


class RadixSort:

    """
    Implementation of radix sort, to be used as a sub-process in modulo sort
    """

    @staticmethod
    def sorter(arr: List[int], maximum: Optional[int] = None) -> List[int]:
        """
        Performs radix sort on the given array of integers.

        Args:
            arr (List[int]): The array of integers to be sorted.
            maximum (Optional[int]): The maximum value in the array. If not provided,
                                     it will be calculated.

        Returns:
            List[int]: The sorted array.
        """

        if len(arr) == 0:
            return arr

        # Find the maximum number to determine the number of digits
        max_num = max(arr) if maximum is None else maximum

        # Perform counting sort for each digit, starting from the least significant digit
        exp = 1
        while max_num // exp > 0:
            CountingSortRadix.sorter(arr, exp)
            exp *= 10

        return arr