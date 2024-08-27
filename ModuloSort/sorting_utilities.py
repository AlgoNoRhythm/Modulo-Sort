from typing import Dict, List, Tuple
from collections import defaultdict

class SortingUtils:

    """
    Collection of auxiliary methods for sorting integer arrays
    """

    @staticmethod
    def sort_small_array(arr: List[int], length: int) -> List[int]:
        """
        Sorts an array of integers with up to 3 elements in ascending order.

        Args:
            arr (List[int]): The array of integers to sort.
            length (int): The number of elements in the array (should be 1, 2, or 3).

        Returns:
            List[int]: The sorted array in ascending order.

        Notes:
            - If the length is 1, the array is already sorted.
            - If the length is 2, it performs one comparison and a possible swap.
            - If the length is 3, it performs up to three comparisons and necessary swaps.
        """
        if length == 1:
            return arr
        elif length == 2:
            # Only two elements to sort
            if arr[0] > arr[1]:
                arr[0], arr[1] = arr[1], arr[0]
        elif length == 3:
            # Three elements to sort
            if arr[0] > arr[1]:
                arr[0], arr[1] = arr[1], arr[0]
            if arr[0] > arr[2]:
                arr[0], arr[2] = arr[2], arr[0]
            if arr[1] > arr[2]:
                arr[1], arr[2] = arr[2], arr[1]
        return arr

    @staticmethod
    def count_duplicates(arr: List[int]) -> Dict[int, List[int]]:
        """
        Appends elements to a dictionary key corresponding to each unique element,
        preserving their original order for stability.

        Args:
            arr (List[int]): The array of integers to count duplicates in.

        Returns:
            Dict[int, List[int]]: A dictionary where the keys are the elements from the array,
                                  and the values are lists of those elements in their original order.
        """
        count_dict = defaultdict(list)  # Initialize a defaultdict with list as default factory

        for element in arr:
            # Append the element itself to the corresponding key's list in the count_dict
            count_dict[element].append(element)  # Append the element to preserve order

        return dict(count_dict)

    @staticmethod
    def append_duplicates(duplicates_dict: Dict[int, List[int]], to_append: int, sorted_arr: List[int]) -> None:
        """
        Appends duplicates of a given value to a sorted array.

        Args:
            duplicates_dict (Dict[int, List[int]]): A dictionary containing the elements as keys and a list of duplicates as values.
            to_append (int): The element to extend the aray with.
            sorted_arr (List[int]): The list to which duplicates will be appended.

        Returns:
            None
        """
        to_extend = duplicates_dict.get(to_append)

        # Extend the sorted_arr list with the duplicates of the element
        sorted_arr.extend(to_extend)

    @staticmethod
    def find_min_and_max(arr: List[int]) -> Tuple[int, int]:

        """
        Finds the minimum and maximum values in an array.

        Args:
            arr (List[int]): The array of integers to find the minimum and maximum from.

        Returns:
            Tuple[int, int]: A tuple containing the minimum and maximum values in the array.
        """
        # Initialize min and max with the first element
        minimum, maximum = arr[0], arr[0]

        for num in arr[1:]:
            # Update minimum and maximum values as needed
            if num < minimum:
                minimum = num
            elif num > maximum:
                maximum = num

        return minimum, maximum