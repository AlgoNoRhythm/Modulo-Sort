# Modulo Sort: A Fast Sorting Algorithm for Positive Integers

## Summary

Modulo Sort is a sorting algorithm designed specifically for positive integers. The expected time complexity of Modulo Sort is **O(n * d)**, where **n** is the number of elements in the input array, and **d** is the number of digits of the maximum remainder (modulo value) within the sub-arrays created during the sorting process. The maximum remainder value is determined by the `modulo_range`, which influences the depth of sorting operations needed for efficient performance.

## Algorithm Overview

### Intuition

Modulo Sort is inspired by the way we commonly represent time. When looking at a clock, we usually think in terms of hours and minutes past the hour, rather than the total minutes from the start of the day. This approach allows us to evaluate hours and minutes independently, leading to more efficient processing.

Similarly, any positive integer can be represented by its quotient (floor division) and remainder (modulo) when divided by an arbitrary number. For instance, if we choose **10** as the divisor, the number **53** can be uniquely identified by the tuple **(53 // 10, 53 % 10)** or **(5, 3)**. Modulo Sort leverages this concept to sort numbers more efficiently by breaking them down into these components.

### Process

The core idea of Modulo Sort is to distribute the input numbers into "buckets" based on their ranges, using both the quotient (floor division) and the remainder (modulo) to sort the numbers within each bucket.

#### Steps:

1. **Calculate Modulo Range**: 
   The `modulo_range` determines the size of each bucket to ensure an even distribution of numbers across all buckets:
   ```modulo_range = floor((max_value - min_value) / len(arr)) + 1```
   
2. **Distribute Values into Buckets**:
   Each number is placed into a dictionary with two levels of keys:
   - **First key**: The result of the floor division of the number minus the minimum value by `modulo_range`.
   - **Second key**: The result of the modulo operation between the number minus the minimum value and `modulo_range`.
   
   For a given number **num**:
   ```index = floor((num - min_value) / modulo_range) modulo_val = (num - min_value) % modulo_range```
   
   The value is stored in `buckets[index][modulo_val]`.

3. **Determine Maximum Bucket Index**:
   ```maximum_bucket = floor((max_value - min_value) / modulo_range)```

4. **Sort Buckets**:
   Iterate through all the available buckets from **0** to **maximum_bucket**:
   - For small arrays (up to three elements), simple swap operations are sufficient, as these operations can be considered **O(1)**.
   - For larger sub-buckets, use Radix Sort to ensure efficient sorting.

   The sub-buckets have a limited range (from 1 to `modulo_range`), and the maximum remainder value determines the depth of the sorting. This makes Radix Sort particularly suitable for sorting within these ranges.

5. **Compile the Sorted Array**:
   After sorting, append all elements from `buckets[index][modulo_val]` into a new array in the order of their indices and sorted modulo values.

### Time Complexity

Modulo Sort involves several steps, each contributing to the overall time complexity:

1. **Preparatory Operations**: **O(n)**
   - Creating buckets by processing every value.
   - Identifying duplicates to maintain the order in the original array.
   - Building sortable sub-arrays based on modulo values.

2. **Sorting Operations for Each Bucket**:
   - For small arrays, sorting is **O(1)**.
   - For larger sub-buckets using Radix Sort: **O(z + d)**, where **z** is the number of elements and **d** is the number of digits of the maximum remainder (equal to `modulo_range`).

The total complexity can be expressed as:
```O(n) + O(s) + l * O(z * d)```
Where:
- **s**: Number of small arrays.
- **l**: Number of sub-arrays with more than three elements.

On average, the complexity simplifies to:
```
O(s) + l * O(z * d)
```

### Best and Worst Case Scenarios

- **Best Case**: All elements are distributed into small arrays, resulting in **O(n)** time complexity.
- **Worst Case**: Most values are concentrated in a few large buckets. If **l \cdot z = n**, the time complexity approximates **O(n \cdot d)**. In this scenario, **d** represents the number of digits of the maximum remainder within sub-arrays, and it is proportional to `modulo_range`. Thus, while similar to Radix Sort, Modulo Sort can perform better due to potentially fewer digits being sorted.


## Benchmarks

The algorithm was benchmarked across a range of input sizes and value ranges, using various distributions ('uniform', 'shuffle', 'normal', 'exponential', 'almost_sorted', 'high_duplicates'). The benchmarks compare Modulo Sort against Radix Sort, Merge Sort, and a variant of Bucket Sort with Radix Sort as a subroutine. The results demonstrate a notable performance improvement, with Modulo Sort achieving almost 2X speedup over the closest competing algorithm, Radix Sort.

For detailed benchmarking results, please refer to the `benchmarks/results/results_df.pkl` file. Additional benchmark scripts are available in the `benchmarks` folder for further experimentation.

---


