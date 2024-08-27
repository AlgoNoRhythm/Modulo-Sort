from typing import List
from radix_sort import RadixSort
from sorting_utilities import SortingUtils


class ModuloSort:

    """
    Implementation of Modulo Sort for positive integer arrays.
    """


    @staticmethod
    def sorter(arr: List[int]) -> List[int]:
        """
        Applies modulo sort on an array of integers.

        Args:
            arr (List[int]): The array of integers to be sorted.

        Returns:
            arr (List[int]): The array of integers, sorted in ascending order.
        """

        # Return if the lenght of the array is 0
        if len(arr) == 0:
            return arr

        sorted_arr = []
        buckets = {}


        # Determine the range of the input array
        min_value, max_value = SortingUtils.find_min_and_max(arr)
        modulo_range = int(round((max_value - min_value)/len(arr) + 1, 0))

        # Find duplicates to be appended after sorting
        duplicates_dict = SortingUtils.count_duplicates(arr)

        # Distribute input array values into buckets by floor division, keeping the modulo for the sub-buckets
        for num in arr:
            index = int((num - min_value) // modulo_range)
            modulo_val = int((num - min_value) % modulo_range)

            # Ensure the index is within the correct range
            index = min(index, len(arr) - 1)

            # If the index already exists, we assign the num to the corresponding modulo value
            if index in buckets:
                buckets[index][modulo_val] = num

            # Otherwise, we create a new bucket and initialize it as above
            else:
                buckets[index] = {}
                buckets[index][modulo_val] = num

        # Identify the upper bound for a bucket index
        maximum_bucket = int((max_value - min_value) // modulo_range)

        for index in range(0, maximum_bucket + 1):

            # Select the bucket to process
            current_bucket = buckets.get(index)

            if not current_bucket:
                continue

            # Get the lenght of the current bucket to sort according to size
            relative_lenght = len(current_bucket)

            if relative_lenght == 1:

                # We get the original values associated with the modulo
                original_values = list(current_bucket.values())

                # We simply append the only value
                to_append = original_values[0]
                SortingUtils.append_duplicates(duplicates_dict=duplicates_dict, to_append=to_append, sorted_arr=sorted_arr)

            elif relative_lenght == 2:

                # We get the original values associated with the modulo
                original_values = list(current_bucket.values())

                # We sort the small array before taking care of the duplicates
                sorted_small = SortingUtils.sort_small_array(original_values, length=2)

                for to_append in sorted_small:
                    SortingUtils.append_duplicates(duplicates_dict=duplicates_dict, to_append=to_append,
                                                   sorted_arr=sorted_arr)

            elif relative_lenght == 3:

                # We get the original values associated with the modulo
                original_values = list(current_bucket.values())

                # We sort the small array before taking care of the duplicates
                sorted_small = SortingUtils.sort_small_array(original_values, length=3)

                for to_append in sorted_small:
                    SortingUtils.append_duplicates(duplicates_dict=duplicates_dict, to_append=to_append,
                                                   sorted_arr=sorted_arr)


            elif relative_lenght > 3:

                # We get the modulo values, which are expected to be easier to sort with Radix sort
                modulo_values = list(current_bucket.keys())

                # We apply Radix sort on the modulo values and append the sorted elements to sorted_arr
                new_arr = RadixSort.sorter(modulo_values)
                for j in new_arr:
                    to_append = current_bucket[j]
                    SortingUtils.append_duplicates(duplicates_dict=duplicates_dict, to_append=to_append,
                                                   sorted_arr=sorted_arr)

        return sorted_arr






