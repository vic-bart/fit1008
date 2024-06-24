"""
Hi! This file defines insertion sort for arrays, a stable sorting algorithm that works by partitioning an array in two -- the lower sorted part iteratively accumulates unsorted values from the upper unsorted part, in their sorted positions, relative to the sorted partition.

  - Recall selection sort, which attempted to improve upon bubble sort by drastically minimising swaps, resulting in an unstable algorithm with reduced best-case time complexity. Insertion sort is an alternative approach to the same problem; it attempts to maintain the O(n) best-case time complexity and stability of bubble sort, while minimising swaps for improved efficiency.

  - Here's an example:

              >> array = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]
      sorted partition = [3]
    unsorted partition =    [2, 1, 9, 4, 7, 6, 5, 8, 0]

    - The sorted partition is initialised to include the first unsorted value -- when the sorted partition includes only one value, that value will be in its sorted position (relative to the sorted partition), because there are no other values to compare it against.

    - For subsequent iterations, the sorted partition swaps the next unsorted value immediately adjacent to the sorted partition, towards its sorted position (relative to the sorted partition).

    for i in (1...n):
    
      j = i - 1

      while (j >= 0) and (array[j + 1] < array[j]):
      
        swap(array, j + 1, j)
        j = j - 1
    
    - See what happens when the next value to be sorted, is less than the sorted partition's max value.

              >> array = [2, 3, 1, 9, 4, 7, 6, 5, 8, 0]
      sorted partition = [2, 3]
    unsorted partition =       [1, 9, 4, 7, 6, 5, 8, 0]

    i = 2, j = 1
       (j >= 0) and (array[j + 1] < array[j])
    == (1 >= 0) and (array[2] < array[1])
    == (1 >= 0) and (1 < 3)
    == True
    swap array[j + 1] and array[j] (i.e. swap array[2] and array[1])
    j = j - 1

              >> array = [2, 1, 3, 9, 4, 7, 6, 5, 8, 0]
      sorted partition = [2, 1, 3]
    unsorted partition =          [9, 4, 7, 6, 5, 8, 0]

    i = 2, j = 0
       (j >= 0) and (array[j + 1] < array[j])
    == (0 >= 0) and (array[1] < array[0])
    == (0 >= 0) and (1 < 2)
    == True
    swap array[j + 1] and array[j] (i.e. swap array[1] and array[0])
    j = j - 1

              >> array = [1, 2, 3, 9, 4, 7, 6, 5, 8, 0]
      sorted partition = [1, 2, 3]
    unsorted partition =          [9, 4, 7, 6, 5, 8, 0]

       (j >= 0)
    == (-1 >= 0)
    == False
    do nothing

              >> array = [1, 2, 3, 9, 4, 7, 6, 5, 8, 0]
      sorted partition = [1, 2, 3]
    unsorted partition =          [9, 4, 7, 6, 5, 8, 0]

    - See what happens when the next value to be sorted, is greater than the sorted partition's max value.

              >> array = [1, 2, 3, 9, 4, 7, 6, 5, 8, 0]
      sorted partition = [1, 2, 3]
    unsorted partition =          [9, 4, 7, 6, 5, 8, 0]

    i = 3, j = 2
       (array[j + 1] < array[j])
    == (array[3] < array[2])
    == (9 < 3)
    == False
    do nothing

              >> array = [1, 2, 3, 9, 4, 7, 6, 5, 8, 0]
      sorted partition = [1, 2, 3, 9]
    unsorted partition =             [4, 7, 6, 5, 8, 0]

    - Notice that when the sorted partition is extended, the next unsorted value is incrementally swapped towards a position that maintains the sorted partition's ascending order.

    - In fact, this is an invariant; at the end of each loop, the sorted partition must be in ascending order; must always be sorted.

    - This also means that once the sorted partition is extended to include the whole array, the whole array must be in ascending order, and thus be sorted.

  - Note that the use of incremental swapping maintains the algorithm's stability:

    - The next unsorted value is incrementally swapped through the sorted partition until either A) values less than or equal to next unsorted value are found, or B) the start of the array is reached -- the "equal" condition prevents the next unsorted value from swapping with equivalent sorted values, thus preserving the order of equivalent values in the unsorted array.

    - Here's an example (consider 6a and 6b as being equivalent to 6; the letters just make it easier to differentiate them):

               >>  array = [1, 2, 3, 6a, 7, 6b, 5, 4]
        sorted partition = [1, 2, 3]
      unsorted partition =          [6a, 7, 6b, 5, 4]

      - The next unsorted value is 6a, and its sorted position is immediately adjacent to the sorted partition.

               >>  array = [1, 2, 3, 6a, 7, 6b, 5, 4]
        sorted partition = [1, 2, 3, 6a]
      unsorted partition =              [7, 6b, 5, 4]

      - The next unsorted value is 7, and its sorted position is immediately adjacent to the sorted partition.

               >>  array = [1, 2, 3, 6a, 7, 6b, 5, 4]
        sorted partition = [1, 2, 3, 6a, 7]
      unsorted partition =                 [6b, 5, 4]

      - The next unsorted value is 6b, and its sorted position is between 6a and 7.

               >>  array = [1, 2, 3, 6a, 7, 6b, 5, 4]
        sorted partition = [1, 2, 3, 6a, 6b, 7]
      unsorted partition =                     [5, 4]

      - The order of values relative to other values within the sorted partition is constant, ensuring the stability persists.

               >>  array = [1, 2, 3, 4, 5 6a, 6b, 7]
        sorted partition = [1, 2, 3, 4, 5 6a, 6b, 7]
      unsorted partition = []

The best-case time complexity is O(n):

  - Recall that when the sorted partition is extended, the next unsorted value is incrementally swapped towards a position that maintains the sorted partition's ascending order. However, if the input array is sorted, then the position of the next unsorted value doesn't violate the sorted partition's ascending order, and thus requires no additional swaps.

  - This will hold true for all subsequent unsorted values, meaning the only work performed by selection sort is iterating over the unsorted partition, which takes O(n) time. 

The average/worst-case time complexity is O(n^2):

  - Recall that when the sorted partition is extended, the next unsorted value is incrementally swapped towards a position that maintains the sorted partition's ascending order. 
  
  - Finding this position could require iterating over all values in the sorted partition, which initially includes one value, and increases by another value each loop. Defining 'n' as the number of values for a given array (i.e. the length of the array):

  c + 1 + 2 + ... + (n-2) + (n-1)

  - This is similar to a known mathematical series, where 1 + 2 + ... + (n-1) + n = n(n+1) / 2

  (n(n+1) / 2) - n + c

  ((n^2+n) / 2) - n + c

  (1/2)n^2 + (1/2)n - n + c

  (1/2)n^2 + (-1/2)n + c

  c * n^2 + c * n + c

  - The greatest term is n^2, and thus the average/worst-case time complexity is O(n^2).

The best/average/worst-case space complexity is O(1). Here's an explanation:

  - Insertion sort is in-place, meaning it directly modifies the array without replicating it. Thus, any auxiliary space used is constant:

  c

  - The greatest term is a constant value, and thus the space complexity is O(1).
"""

def insertion_sort(array:list) -> None:
  """
  A stable sorting algorithm that works by partitioning an array in two -- the lower sorted part iteratively accumulates unsorted values from the upper unsorted part, in their sorted positions, relative to the sorted partition.

  Input:
    - array (list)
      A list of values.
  Output:
    - array (list)
      A list of sorted values.
  Time Complexity:
    - Best-case
      O(n)
    - Average-case
      O(n^2)
    - Worst-case
      O(n^2)
  Space Complexity:
    - Best-case
      O(1)
    - Average-case
      O(1)
    - Worst-case
      O(1)
  """
  for i in range(1, len(array)):

    j:int = i - 1

    while (j >= 0) and (array[j + 1] < array[j]):
      
      swap(array, j + 1, j)
      j = j - 1

def swap(array:list, i:int, j:int) -> None:
  """
  Swaps the value at index i with the value at index j for a given array.

  Input:
    - array (list)
      A list of values.
  Output:
    - array (list)
      A list of sorted values.
  Time Complexity:
    - Best-case
      O(1)
    - Average-case
      O(1)
    - Worst-case
      O(1)
  Space Complexity:
    - Best-case
      O(1)
    - Average-case
      O(1)
    - Worst-case
      O(1)
  """
  item = array[i]
  array[i] = array[j]
  array[j] = item


if __name__ == "__main__":
  
  array = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]
  print(array)
  insertion_sort(array)
  print(array)