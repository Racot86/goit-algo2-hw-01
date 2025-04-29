from src.arrays.sample_array import sample_array
from src.functions.min_max_search import min_max_search

from src.functions.k_min_search import k_min_search

if __name__ == '__main__':
   print("task 1: ")
   print("  sample array:")
   print("  ", sample_array)
   print("  min max search:\n", min_max_search(sample_array))

   print("\ntask 2: ")
   print("  sorted sample array:")
   print("  ", sorted(sample_array))

   print("  k_min_search:")
   print("  10th minimum element:", k_min_search(sample_array, 10))

