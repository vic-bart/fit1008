"""
Hi! This file defines selection sort for arrays, an unstable sorting algorithm that works by partitioning an array in two, where the lower sorted part iteratively accumulates the minimum values of the upper unsorted part. 

  - Recall bubble sort, which sorts an array by swapping the minimum unsorted values into their sorted positions. Selection sort works on the same principle, but attempts to sort more efficiently by minimising the number of swaps as much as possible; rather than incrementally swapping the minimum unsorted value towards its sorted position, selection sort iterates over all unsorted values, finds the minimum unsorted value, and swaps it directly into its sorted position.

  - Here's an example:

             >>  array = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]
      sorted partition = []
    unsorted partition = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]

    - To find the minimum unsorted value, selection sort compares the current minimum unsorted value -- which is initialised to the unsorted value immediately adjacent to the sorted partition -- with every other unsorted value. If a lower value is found, it replaces the current minimum unsorted value. After all unsorted values have been compared, the current minimum unsorted value is guaranteed to be the minimum unsorted value, and is swapped with the unsorted value immediately adjacent to the sorted partition.

    for i in (0...n):

      min = i

      for j in (i+1...n):
      
        if array[j] < array[min]:
        
          min = j
          
      swap(array, i, min)

    - See what happens when an unsorted value is less than the current minimum unsorted value.

             >>  array = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]
      sorted partition = []
    unsorted partition = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]

    min = 0, j = 1
    array[j] < array[min] == True (i.e. array[1] < array[0] == 2 < 3 == True)
    min = 1

             >>  array = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]
      sorted partition = []
    unsorted partition = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]

    - Note that no values have been swapped. 

    - See what happens when an unsorted value is greater than the current minimum unsorted value.

             >>  array = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]
      sorted partition = []
    unsorted partition = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]

    min = 2, j = 3
    array[j] < array[min] == False (i.e. array[3] < array[2] == 9 < 1 == False)
    do nothing

             >>  array = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]
      sorted partition = []
    unsorted partition = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]
    
    - See what happens when the final unsorted value is compared.

             >>  array = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]
      sorted partition = []
    unsorted partition = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]

    i = 0, min = 2, j = 9
    array[j] < array[min] == True (i.e. array[9] < array[2] == 0 < 1 == True)
    min = 9

    i = 0, min = 9, j = 10
    j == n
    exit loop
    swap array[i] with array[min] (i.e. swap array[0] with array[9])

             >>  array = [0, 2, 1, 9, 4, 7, 6, 5, 8, 3]
      sorted partition = [0]
    unsorted partition =    [2, 1, 9, 4, 7, 6, 5, 8, 3]

    - Notice that the array as a whole is not sorted, but the minimum unsorted value is in its sorted position (i.e. if the array were sorted, the value would have the same position). 

    - In fact, this is an invariant; at the end of each loop, the minimum unsorted value will always be moved to its sorted position. 

    - And since the values are sorted in ascending order, the array is partitioned in two -- the lower part contains sorted values, the upper part contains unsorted values. Each loop moves the minimum value from its unsorted position in the upper part, to its sorted position in the lower part, extending the sorted partition until it includes the whole array.

  - Recall that selection sort attempts to improve upon bubble sort by minimising swaps. But does it succeed? Yes, selection sort is generally more efficient because of fewer swaps being performed, but the time complexity (found below) has not improved. In fact, the best-case time complexity has worsened to O(n^2) (previously O(n)):

    - In bubble sort, the swapping of immediately adjacent values revealed information about the whole array -- if swaps were performed, there existed a pair of immediately adjacent values that were not in ascending order, and thus the array could not be in ascending order (i.e. not sorted); if no swaps were performed, each pair must be in ascending order, and thus the whole array must be in ascending order (i.e. sorted).

    - In selection sort, no information is revealed about the array as a whole -- the algorithm only identifies the minimum unsorted value, and swaps it into its sorted position, which is already known without incremental swapping (this position is immediately adjacent to the sorted partition, where it is greater than all the sorted values in the lower part, and smaller than all the unsorted values in the upper part).

    - Thus, selection sort cannot identify when the whole array has been sorted, and must always iterate over the whole unsorted partition.

  - Additionally, the removal of incremental swapping also makes the algorithm unstable:

    - When the minimum unsorted value is swapped into its sorted position, the original value which existed there prior, is moved into the minimum unsorted value's vacated position.

    - If other values equal to this original value, were previously positioned after the original value, and are now positioned before it, their sorted positions may come before the original value's sorted position, making the algorithm unstable.

    - Here's an example (consider 7a and 7b as being equivalent to 7; the letters just make it easier to differentiate them):

               >>  array = [1, 2, 3, 7a, 7b, 6, 5, 4]
        sorted partition = [1, 2, 3]
      unsorted partition =          [7a, 7b, 6, 5, 4]

      - The minimum unsorted value is 4, and it's sorted position is immediately adjacent to the sorted partition.

               >>  array = [1, 2, 3, 4, 7b, 6, 5, 7a]
        sorted partition = [1, 2, 3, 4]
      unsorted partition =             [7b, 6, 5, 7a]

      - This is the moment where the sorted order of equivalent values is violated; 7a must come before 7b in the sorted array, as it was in the unsorted array. However, this violation will persist.

               >>  array = [1, 2, 3, 4, 5, 6, 7b, 7a] ([7b, 7a] = unstable, [7a, 7b] = stable)
        sorted partition = [1, 2, 3, 4, 5, 6, 7b, 7a]
      unsorted partition = []

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
  An unstable sorting algorithm that works by partitioning an array in two, where the lower sorted part iteratively accumulates the minimum values of the upper unsorted part.

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


if __name__ == "__main__":
  
  array = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]
  print(array)
  selection_sort(array)
  print(array)