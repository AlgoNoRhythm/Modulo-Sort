from typing import List


class CountingSortRadix:

    """
    Implementation of counting sort to be used as a sub-routine in radix sort.
    """

    @staticmethod
    def sorter(arr: List[int], exp: int) -> None:
        """
        Performs counting sort on the array based on the digit represented by exp.

        Args:
            arr (List[int]): The array of integers to be sorted.
            exp (int): The digit's place to sort by (1 for units, 10 for tens, etc.).

        Returns:
            None: The array is sorted in place based on the current digit.
        """
        n = len(arr)
        output = [0] * n  # Output array that will have sorted arr
        count = [0] * 10  # Initialize count array for digits (0-9)

        # Store count of occurrences of digits
        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1

        # Modify count so that it now contains the actual positions of digits in output[]
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array
        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1

        # Copy the output array to arr, so that arr contains the sorted numbers
        for i in range(n):
            arr[i] = output[i]


class CountingSort:
    """
    Implementation of counting sort algorithm.
    """

    @staticmethod
    def sorter(arr: List[int]) -> List[int]:
        """
        Sorts an array in ascending order using the counting sort algorithm.

        Args:
            arr (List[int]): The array of integers to be sorted.

        Returns:
            List[int]: The sorted array.
        """
        if not arr:
            return arr

        # Find the maximum value in the array to know the range of numbers
        max_val = max(arr)

        # Initialize a count array with zeros, having a length of max_val + 1
        count = [0] * (max_val + 1)

        # Store the count of each element in the count array
        for num in arr:
            count[num] += 1

        # Rebuild the original array using the count array
        index = 0
        for i in range(len(count)):
            while count[i] > 0:
                arr[index] = i
                index += 1
                count[i] -= 1

        return arr
