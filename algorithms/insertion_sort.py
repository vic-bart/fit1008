"""
Hi! This file defines insertion sort for arrays, a stable sorting algorithm that works by iteratively shifting values from an upper unsorted partition into a lower sorted partition.
Here's an example:

            >> array = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]
    sorted partition = [3]
  unsorted partition =    [2, 1, 9, 4, 7, 6, 5, 8, 0]

  - The sorted partition is initialised to include the first unsorted value, because when the sorted partition only includes one value, that value must be in its sorted position (within the partition), because there are no other values to compare it against.

  - For subsequent iterations, the sorted partition shifts the next unsorted value (i.e. the one immediately adjacent to the sorted partition) down until it reaches its sorted position (within the partition). 

  for i in (1...n):
  
    j = i - 1

    while (j >= 0) and (array[j] > array[j + 1]):
    
      swap(array, j + 1, j)
      j = j - 1
  
  - See what happens when the next value to be sorted, is less than the sorted partition's max value.

            >> array = [2, 3, 1, 9, 4, 7, 6, 5, 8, 0]
    sorted partition = [2, 3]
  unsorted partition =       [1, 9, 4, 7, 6, 5, 8, 0]

  i = 2, j = 1
  (j >= 0) and (array[j] > array[j + 1]) == True; (1 >= 0) and (3 > 1) == True
  swap array[j + 1] and array[j]
  j = j - 1

  i = 2, j = 0
  (j >= 0) and (array[j] > array[j + 1]) == True; (0 >= 0) and (2 > 1) == True
  swap array[j + 1] and array[j]
  j = j - 1

  (j >= 0) == False; (-1 >= 0) == False

            >> array = [1, 2, 3, 9, 4, 7, 6, 5, 8, 0]
    sorted partition = [1, 2, 3]
  unsorted partition =          [9, 4, 7, 6, 5, 8, 0]

  - See what happens when the next value to be sorted, is greater than the sorted partition's max value.

            >> array = [1, 2, 3, 9, 4, 7, 6, 5, 8, 0]
    sorted partition = [1, 2, 3]
  unsorted partition =          [9, 4, 7, 6, 5, 8, 0]

  i = 3, j = 2
  (array[j] > array[j + 1]) == False; (3 > 9) == False
  do nothing

            >> array = [1, 2, 3, 9, 4, 7, 6, 5, 8, 0]
    sorted partition = [1, 2, 3, 9]
  unsorted partition =             [4, 7, 6, 5, 8, 0]

The best-case time complexity is O(n):

  - If the input list is already sorted, each value will be iterated over once, and no swaps will be performed.

  n + c

  

The average/worst-case time complexity is O(n^2):

  - 

The best/average/worst-case space complexity is O(1). Here's an explanation:

  - Insertion sort is in-place, meaning it directly modifies the array without replicating it. Thus, any auxiliary space used is constant:

  c

  - The greatest term is a constant value, and thus the time complexity is O(1).
"""

def insertion_sort(array:list) -> None:
  """
  """
  for i in range(1, len(array)):

    j:int = i - 1

    while (j >= 0) and (array[j] > array[j + 1]):
      
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