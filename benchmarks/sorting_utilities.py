from typing import Dict, List, Tuple, Union
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
    def count_duplicates(arr: List[int]) -> Dict[int, Union[int, List[int]]]:
        """
        Tracks occurrences of elements in the array. On the first occurrence of an element, its index is stored.
        On subsequent occurrences, the element is moved to a defaultdict that maps elements to lists of their duplicates.

        Args:
            arr (List[int]): The array of integers to process.

        Returns:
            Dict[int, List[int]]: A dictionary where keys are the elements that have duplicates and values
                                   are lists of those elements, effectively storing duplicates after the first occurrence.
        """
        count_dict = {}
        duplicates_dict = defaultdict(list)

        for k, element in enumerate(arr):
            original_index = count_dict.get(element)

            if type(original_index) == int:
                duplicates_dict[element].append(arr[original_index])

                duplicates_dict[element].append(element)

                count_dict[element] = ""

            elif original_index == "":
                duplicates_dict[element].append(element)
            else:
                # Track the first occurrence with a simple index
                count_dict[element] = k

        return duplicates_dict

    @staticmethod
    def append_duplicates(duplicates_dict: Dict[int, List[int]], to_append: int, sorted_arr: List[int]) -> None:
        """
        Appends duplicates of a given element to a sorted array, if available. Otherwise simply appends the element

        Args:
            duplicates_dict (Dict[int, List[int]]): A dictionary containing elements as keys and a list of duplicates as values.
            to_append (int): The element to append duplicates for.
            sorted_arr (List[int]): The list to which duplicates will be appended.

        Returns:
            None
        """
        # Check if the element has duplicates to append
        if to_append in duplicates_dict:
            sorted_arr.extend(duplicates_dict[to_append])
        else:
            sorted_arr.append(to_append)


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