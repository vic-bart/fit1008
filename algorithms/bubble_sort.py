"""
Hi! This file defines bubble sort for arrays, a stable sorting algorithm that works by traversing an array from the start, to the end where it iteratively accumulates the greatest values. 
Here's an example:

  >>  array = [3, 1, 2, 9, 4, 7, 6, 5, 8, 0]

  - To find the greatest value, bubble sort compares immediately adjacent values, shifting the greater value towards the end.

  for i in (0...n):
    if array[i] > array[i+1]:
      swap array[i] with array[i+1]

  - See what happens when the current value is greater than the next value.

  >>  array = [3, 1, 2, 9, 4, 7, 6, 5, 8, 0]
  
  i = 0
  array[i] > array[i+1] == True (3 > 1 == True)
  swap array[i] with array[i+1]

  >>  array = [1, 3, 2, 9, 4, 7, 6, 5, 8, 0]

  - See what happens when the current value is smaller than the next value.

  >>  array = [1, 2, 3, 9, 4, 7, 6, 5, 8, 0]

  i = 2
  array[i] > array[i+1] == False (3 > 9 == False)
  do nothing

  >>  array = [1, 2, 3, 9, 4, 7, 6, 5, 8, 0]

  - This repeats all the way until the end of the list is reached. 

  >>  array = [1, 2, 3, 4, 7, 6, 5, 8, 0, 9]

  - Notice that the array as a whole is not sorted, but the greatest unsorted value is in its sorted position (i.e. if the array were sorted, the value would have the same position). 
  - In fact, this is an invariant; at the end of each loop, the greatest unsorted value will always be moved to its sorted position. 
  - And since the values are sorted in descending order, the array is partitioned in two -- the lower half contains unsorted values, the upper half contains sorted values. Each loop moves the greatest value from its 
  unsorted position in the lower half, to its sorted position in the upper half, extending the sorted partition until it includes the whole array.

The best-case time complexity is O(n):

  - Recall the invariant -- at the end of each loop, the greatest unsorted value will always be moved to its sorted position. But what if at the end of the loop, no values have been moved? 
  - Recall that bubble sort compares immediately adjacent values and swaps them if they're in descending order, but if no values have been moved, than each pair of immediately adjacent values must be in ascending 
  order, and thus the array is already sorted. 
  - This provides the algorithm with an early exit; if no values have been swapped, the array is sorted and the algorithm terminates. But even if the input array was sorted, the algorithm can only determine it by 
  iterating over the whole array once, and thus the best-case time complexity is O(n).

The average/worst-case time complexity is O(n^2):

  - Note that because the upper half will always be made of values greater than all values in the lower half, the sorted position of the lower half's greatest value is always immediately adjacent to the start of the 
  upper half (because this position is less than all the sorted values in the upper half, and greater than all the unsorted values in the lower half).
  - This means we never need to iterate over the sorted values; we only iterate over the unsorted values, which decreases by one value each loop. Defining 'n' as the number of values for a given array (i.e. the 
  length of the array):

  (n-1) + (n-2) + ... + 2 + 1 + c

  - This is similar to a known mathematical series, where n + (n-1) + ... + 2 + 1 = n(n+1) / 2

  (n(n+1) / 2) - n + c

  ((n^2+n) / 2) - n + c

  (1/2)n^2 + (-1/2)n + c

  c * n^2 + c * n + c

  - The greatest term is n^2, and thus the average/worst-case time complexity is O(n^2).

The best/average/worst-case space complexity is O(1). Here's an explanation:

  - Bubble sort is in-place, meaning it directly modifies the array without replicating it. Thus, any auxiliary space used is constant:

  c

  - The greatest term is a constant value, and thus the time complexity is O(1).
"""

def bubble_sort(array:list) -> None:
  """
  A stable sorting algorithm that works by traversing an array from the start, to the end where it iteratively accumulates the greatest values.

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
  for n in range(len(array), 1, -1):

    swapped:bool = False

    for i in range(n-1):
      
      if array[i] > array[i+1]:

        swap(array, i, i+1)
        swapped = True

    if not swapped:
      break

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
  
  array = [3, 1, 2, 9, 4, 7, 6, 5, 8, 0]
  print(array)
  bubble_sort(array)
  print(array)