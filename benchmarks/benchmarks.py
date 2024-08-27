from modulo_sort import ModuloSort
from quick_sort import QuickSort
from tabulate import tabulate
from merge_sort import MergeSort
from bucket_sort import BucketSort, QuickBucketSort
from radix_sort import RadixSort
import numpy as np
import pandas as pd
import random
from typing import Callable, List, Dict, Any
import logging
import time



logging.basicConfig(filename='script.log', level=logging.INFO)


class SortingEvaluator:
    def __init__(self, sorting_algorithms: Dict[str, Callable[[List[Any]], List[Any]]]):
        """
        Initializes the SortingEvaluator with a dictionary of sorting algorithms.

        :param sorting_algorithms: A dictionary where keys are algorithm names and values are functions implementing the sorting algorithm.
        """
        self.sorting_algorithms = sorting_algorithms
        self.algorithm_names = list(sorting_algorithms.keys())
        self.results = []
        self.results_df = pd.DataFrame()
        self.metrics_df = pd.DataFrame()
        self.distribution_metrics_df = pd.DataFrame()
        self.size_metrics_df = pd.DataFrame()
        self.range_metrics_df = pd.DataFrame()



    def generate_large_random_array(self, size: int, distribution: str, integer: bool, range_min: int, range_max: int,
                                    percentage_sorted: float = 0.9, duplicate_percentage: float = 0.5) -> List[int]:
        """
        Generates a large random array based on the specified distribution and range.

        :param size: Size of the array.
        :param distribution: Type of distribution ('uniform', 'shuffle', 'normal', 'exponential', 'poisson', 'almost_sorted', 'high_duplicates').
        :param integer: Whether to generate integer values.
        :param range_min: Minimum value for the range.
        :param range_max: Maximum value for the range.
        :param percentage_sorted: Percentage of the array that should be sorted (used for 'almost_sorted' distribution).
        :param duplicate_percentage: Percentage of duplicates in the array (used for 'high_duplicates' distribution).
        :return: Generated array.
        """
        if distribution == 'uniform':
            if integer:
                return np.random.randint(range_min, range_max, size).tolist()
            else:
                return np.random.uniform(range_min, range_max, size).tolist()

        elif distribution == 'shuffle':
            arr = list(range(size))
            random.shuffle(arr)
            return arr

        elif distribution == 'normal':
            mean = (range_max + range_min) / 2
            std_dev = (range_max - range_min) / 4
            array = np.random.normal(mean, std_dev, size).astype(int)
            array = np.clip(array, range_min, range_max)
            return array.tolist()

        elif distribution == 'exponential':
            scale = (range_max + range_min) / 2
            array = np.random.exponential(scale, size).astype(int)
            array = np.clip(array, range_min, range_max)
            return array.tolist()


        elif distribution == 'almost_sorted':
            # Start with a sorted array
            array = np.arange(size)

            # Determine the number of elements to shuffle
            num_elements_to_shuffle = int(size * (1 - percentage_sorted))
            indices_to_shuffle = np.random.choice(size, num_elements_to_shuffle, replace=False)

            # Shuffle the selected indices
            np.random.shuffle(array[indices_to_shuffle])
            return array.tolist()

        elif distribution == 'high_duplicates':
            # Start with an empty array
            array = []

            # Determine the number of unique elements
            num_unique = int(size * (1 - duplicate_percentage))

            # Generate unique values
            unique_values = np.random.randint(range_min, range_max, num_unique)
            array.extend(unique_values)

            # Fill the rest of the array with random choices from the unique values
            while len(array) < size:
                array.append(np.random.choice(unique_values))

            # Shuffle the array to avoid any ordering
            random.shuffle(array)
            return array

        else:
            raise ValueError("Unknown distribution type")



    def is_sorted(self, arr: List[int]) -> bool:
        """
        Checks if the given array is sorted.

        :param arr: Array to check.
        :return: True if sorted, False otherwise.
        """
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

    def run_single_evaluation(self, arr: List[int], size: int, distribution: str, range_min: int, range_max: int, integer: bool, run_counter: int) -> Dict[str, Any]:
        """
        Runs a single evaluation of all sorting algorithms on a given array.

        :param arr: The original array to be sorted (a copy will be used for each algorithm).
        :param size: Size of the array.
        :param distribution: Distribution type of the array.
        :param range_min: Minimum value for the range.
        :param range_max: Maximum value for the range.
        :param integer: Whether the array contains integer values.
        :return: Dictionary with evaluation results.
        """
        row_result = {
            'size': size,
            'distribution': distribution,
            'range_min': range_min,
            'range_max': range_max,
            'integer': integer
        }
        expected_sorted = sorted(arr.copy())

        for name, algorithm in self.sorting_algorithms.items():
            print(f"Run number {str(run_counter)}: Processing {name} with size {size}, distribution {distribution}, range ({range_min}, {range_max})")
            logging.info(f"Run number {str(run_counter)}: Processing {name} with size {size}, distribution {distribution}, range ({range_min}, {range_max})")
            try:
                arr_copy = arr.copy()
                start_time = time.perf_counter()
                sorted_arr = algorithm(arr_copy)
                end_time = time.perf_counter()
                elapsed_time = end_time - start_time
                assert expected_sorted == sorted_arr, f"{name} did not sort array correctly"
                row_result[f'{name}_is_sorted'] = True
                row_result[f'{name}_error'] = None
                row_result[f'{name}_time'] = elapsed_time
            except Exception as e:
                print(f"Error in {name}: {e}")
                logging.error(f"Error in {name}: {e}")
                row_result[f'{name}_is_sorted'] = False
                row_result[f'{name}_error'] = str(e)
                row_result[f'{name}_time'] = None

        return row_result

    def calculate_metrics(self):
        """
        Calculates various metrics (mean, std deviation, min, max, median) for each sorting algorithm.

        Populates the following attributes:
        - self.metrics_df: DataFrame containing overall metrics for each algorithm.
        - self.distribution_metrics_df: DataFrame containing average time by distribution.
        - self.size_metrics_df: DataFrame containing average time by array size.
        - self.range_metrics_df: DataFrame containing average time by range.
        """
        metrics = {}
        distribution_metrics_df = None
        size_metrics_df = None
        range_metrics_df = None

        for name in self.algorithm_names:
            distribution_metrics = self.results_df.groupby('distribution')[f'{name}_time'].mean().reset_index()
            distribution_metrics.rename(columns={f'{name}_time': f'{name}_avg_time'}, inplace=True)
            if distribution_metrics_df is None:
                distribution_metrics_df = distribution_metrics
            else:
                distribution_metrics_df = pd.merge(distribution_metrics_df, distribution_metrics, on='distribution', how='outer')

            size_metrics = self.results_df.groupby('size')[f'{name}_time'].mean().reset_index()
            size_metrics.rename(columns={f'{name}_time': f'{name}_avg_time'}, inplace=True)
            if size_metrics_df is None:
                size_metrics_df = size_metrics
            else:
                size_metrics_df = pd.merge(size_metrics_df, size_metrics, on='size', how='outer')

            range_metrics = self.results_df.groupby(['range_min', 'range_max'])[f'{name}_time'].mean().reset_index()
            range_metrics.rename(columns={f'{name}_time': f'{name}_avg_time'}, inplace=True)
            if range_metrics_df is None:
                range_metrics_df = range_metrics
            else:
                range_metrics_df = pd.merge(range_metrics_df, range_metrics, on=['range_min', 'range_max'], how='outer')

            valid_times = self.results_df[self.results_df[f'{name}_time'].notna()][f'{name}_time']
            metrics[name] = {
                'average_time': valid_times.mean(),
                'std_deviation': valid_times.std(),
                'min_time': valid_times.min(),
                'max_time': valid_times.max(),
                'median_time': valid_times.median()
            }

        self.metrics_df = pd.DataFrame(metrics).T
        self.metrics_df.reset_index(inplace=True)
        self.metrics_df.rename(columns={'index': 'algorithm'}, inplace=True)
        self.distribution_metrics_df = distribution_metrics_df
        self.size_metrics_df = size_metrics_df
        self.range_metrics_df = range_metrics_df

    def evaluate(self, sizes: List[int] = None, distributions: List[str] = None, integer: bool = False, runs: int = 10):
        """
        Evaluates the sorting algorithms on arrays of varying sizes, distributions, and ranges.

        :param sizes: List of sizes for the arrays.
        :param distributions: List of distribution types.
        :param integer: Whether to generate integer values.
        :param runs: Number of times to run each algorithm for each configuration.
        """
        if sizes is None:
            sizes = [1000, 10000, 100000, 1000000, 10000000]
        if distributions is None:
            distributions = ['uniform', 'shuffle', 'normal', 'exponential', 'almost_sorted', 'high_duplicates']

        ranges = [(10, 10 ** (i + 1)) for i in range(1, 8)]

        for run in range(runs):
            for size in sizes:
                for dist in distributions:
                    for range_min, range_max in ranges:
                            arr = self.generate_large_random_array(size, dist, integer, range_min, range_max)
                            row_result = self.run_single_evaluation(arr, size, dist, range_min, range_max, integer, run + 1)
                            self.results.append(row_result)

        self.results_df = pd.DataFrame(self.results)
        self.calculate_metrics()


sorting_algorithms = {
    'modulo_sort': ModuloSort.sorter,
    'radix_sort' : RadixSort.sorter,
    'radix_bucket_sort': BucketSort.sorter,
#    'quick_bucket_sort' : QuickBucketSort.sorter,
    'merge_sort': MergeSort.sorter,
#    'quick_sort': QuickSort.sorter,

}

evaluator = SortingEvaluator(sorting_algorithms)
evaluator.evaluate(integer=True, runs=5)
print(tabulate(evaluator.metrics_df, headers='keys', tablefmt='psql', showindex=False))
print(tabulate(evaluator.distribution_metrics_df, headers='keys', tablefmt='psql', showindex=False))
print(tabulate(evaluator.size_metrics_df, headers='keys', tablefmt='psql', showindex=False))
print(tabulate(evaluator.range_metrics_df, headers='keys', tablefmt='psql', showindex=False))
evaluator.metrics_df.to_pickle('results/metrics_df.pkl')
evaluator.distribution_metrics_df.to_pickle('results/distribution_metrics_df.pkl')
evaluator.size_metrics_df.to_pickle('results/size_metrics_df.pkl')
evaluator.range_metrics_df.to_pickle('results/range_metrics_df.pkl')


