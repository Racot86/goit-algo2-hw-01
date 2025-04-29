# Algorithm Implementation Project

This project implements two efficient algorithms for array processing:

1. Min-Max Search - Finding minimum and maximum values in an array using divide and conquer
2. K-th Minimum Search - Finding the k-th smallest element in an array using quickselect

## Task 1: Min-Max Search

The `min_max_search` function finds both the minimum and maximum values in an array using a divide-and-conquer approach.

### How it works:

1. The array is recursively divided into two halves until we reach subarrays of size 1 or 2
2. For subarrays of size 1, the single element is both the minimum and maximum
3. For subarrays of size 2, we compare the two elements to find the minimum and maximum
4. As we merge results back up, we compare the minimum and maximum from each half to find the overall minimum and maximum

### Time Complexity:

- O(n) time complexity, where n is the length of the array
- This approach requires approximately 3n/2 comparisons, which is more efficient than the naive approach (2n comparisons)

### Example Usage:

```python
from src.arrays.sample_array import sample_array
from src.functions.min_max_search import min_max_search

# Find minimum and maximum values in the array
min_val, max_val = min_max_search(sample_array)
print(f"Minimum value: {min_val}, Maximum value: {max_val}")
```

## Task 2: K-th Minimum Search

The `k_min_search` function finds the k-th smallest element in an array using the quickselect algorithm.

### How it works:

1. The function uses the quickselect algorithm, which is based on the partition scheme from quicksort
2. In each step, it selects a pivot element and partitions the array around it
3. After partitioning, if the pivot is at position k, we've found our answer
4. If k is less than the pivot's position, we search in the left subarray
5. If k is greater than the pivot's position, we search in the right subarray

### Time Complexity:

- Average case: O(n) time complexity
- Worst case: O(n²) time complexity (rare)
- This is more efficient than sorting the entire array (O(n log n)) when we only need to find a single element

### Example Usage:

```python
from src.arrays.sample_array import sample_array
from src.functions.k_min_search import k_min_search

# Find the 10th smallest element in the array
tenth_min = k_min_search(sample_array, 10)
print(f"10th minimum element: {tenth_min}")

# Find the minimum element (0th smallest)
min_element = k_min_search(sample_array, 0)
print(f"Minimum element: {min_element}")
```

## Key Differences Between the Algorithms

1. **Purpose**:
   - `min_max_search` finds both the minimum and maximum values
   - `k_min_search` finds a specific element (the k-th smallest)

2. **Approach**:
   - `min_max_search` uses pure divide-and-conquer
   - `k_min_search` uses quickselect, which is more selective about which parts of the array to process

3. **Efficiency**:
   - Both have O(n) average time complexity
   - `min_max_search` always processes the entire array
   - `k_min_search` often processes only a portion of the array, making it more efficient for its specific task