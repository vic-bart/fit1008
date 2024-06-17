"""
Hi! This file defines selection sort for arrays, an unstable sorting algorithm that works by partitioning an array in two, where the lower sorted half iteratively accumulates the minimum values of the upper unsorted half. 
Note that this is very similar to bubble sort, the main difference being we only swap the desired value after iterating over all other unsorted values (bubble sort swaps the desired value while iterating over all other unsorted values). 
Here's an example:

  >>  array = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]

  - To find the minimum unsorted value, selection sort compares the current minimum unsorted value -- which is initialised to the unsorted value immediately adjacent to the sorted partition -- with every other unsorted value. If a lower value is found, it replaces the current minimum unsorted value. After all unsorted values have been compared, the current minimum unsorted value is guaranteed to be the minimum unsorted value, and is swapped with the unsorted value immediately adjacent to the sorted partition.

  min = i
  for j in (i+1...n):
    if array[j] < array[min]:
      min = j
  swap(array, i, min)

  - See what happens when an unsorted value is less than the first unsorted value.

  >>  array = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]

  j = 1, min = 0
  array[j] < array[min] == True (2 < 3 == True)
  min = 1

  >>  array = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]

  - Note that no values have been swapped. See what happens when the last unsorted value is compared (Note that at this point, the sorted partition is empty, and the unsorted partition includes the whole array).

  >>  array = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]

  j = n-1, min = 2, i = 0
  array[j] < array[min] == True (0 < 1 == True)
  min = n-1
  j += 1, j == n (exit loop)
  swap array[i] with array[min]

  >>  array = [0, 2, 1, 9, 4, 7, 6, 5, 8, 3]

  - Notice that the array as a whole is not sorted, but the minimum unsorted value is in its sorted position (i.e. if the array were sorted, the value would have the same position). 
  - In fact, this is an invariant; at the end of each loop, the minimum unsorted value will always be moved to its sorted position. 
  - And since the values are sorted in ascending order, the array is partitioned in two -- the lower half contains sorted values, the upper half contains unsorted values. Each loop moves the minimum value from its unsorted position in the upper half, to its sorted position in the lower half, extending the sorted partition until it includes the whole array.

The best/average/worst-case time complexity is O(n^2):

  - We always only iterate over the unsorted values, which decreases by one value each loop. Defining 'n' as the number of values for a given array (i.e. the length of the array):

  (n-1) + (n-2) + ... + 2 + 1 + c

  - This is similar to a known mathematical series, where n + (n-1) + ... + 2 + 1 = n(n+1) / 2

  (n(n+1) / 2) - n + c

  ((n^2+n) / 2) - n + c

  (1/2)n^2 + (-1/2)n + c

  c * n^2 + c * n + c

  - The greatest term is n^2, and thus the best/average/worst-case time complexity is O(n^2).

The best/average/worst-case space complexity is O(1). Here's an explanation:

  - Selection sort is in-place, meaning it directly modifies the array without replicating it. Thus, any auxiliary space used is constant:

  c

  - The greatest term is a constant value, and thus the time complexity is O(1).
"""

def selection_sort(array:list) -> None:
  """
  An unstable sorting algorithm that works by partitioning an array in two, where the lower sorted half iteratively accumulates the minimum values of the upper unsorted half. 

  Input:
    - array (list)
      A list of values.
  Output:
    - array (list)
      A list of sorted values.
  Time Complexity:
    - Best-case
      O(n^2)
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
  for i in range(len(array)):

    min_value:int = i

    for j in range(i+1, len(array)):
      
      if array[j] < array[min_value]:

        min_value = j

    swap(array, i, min_value)

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


if __name__=="__main__":
  
  array = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]
  print(array)
  selection_sort(array)
  print(array)