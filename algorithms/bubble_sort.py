"""
Hi! This file defines bubble sort for arrays, a stable sorting algorithm that works by traversing an array from the end, to the start where it iteratively accumulates the minimum values in their sorted positions.

  - Here's an example:

    >>  array = [3, 0, 2, 9, 4, 7, 6, 5, 8, 1]

    - To find the minimum unsorted value, bubble sort compares immediately adjacent values, shifting the smaller value towards the start.

    for i in range(n):
    
      for j in range(n-1...i):
      
          if array[j-1] > array[j]:
          
            swap(array, j-1, j)

    - See what happens when the current value is smaller than the next value.

    >>  array = [3, 0, 2, 9, 4, 7, 6, 5, 8, 1]
    
    i = 0, j = 9
    array[j-1] > array[j] == True (i.e. array[8] > array[9] == 8 > 1 == True)
    swap array[j-1] with array[j] (i.e. swap array[8] with array[9])

    >>  array = [3, 0, 2, 9, 4, 7, 6, 5, 1, 8]

    - See what happens when the current value is greater than or equal to the next value.

    >>  array = [3, 0, 1, 2, 9, 4, 7, 6, 5, 8]

    i = 0, j = 2
    array[j-1] > array[j] == False (i.e. array[1] > array[2] == 0 > 1 == False)
    do nothing

    >>  array = [3, 0, 1, 2, 9, 4, 7, 6, 5, 8]

    - This repeats all the way until the end of the list is reached. 

    >>  array = [0, 3, 1, 2, 9, 4, 7, 6, 5, 8]

    - Notice that the array as a whole is not sorted, but the minimum unsorted value is in its sorted position (i.e. if the array were sorted, the value would have the same position). 

    - In fact, this is an invariant; at the end of each loop, the minimum unsorted value will always be moved to its sorted position. 

    - And since the values are sorted in ascending order, the array is partitioned in two -- the lower part contains sorted values, the upper part contains unsorted values. Each loop moves the minimum value from its unsorted position in the upper part, to its sorted position in the lower part, extending the sorted partition until it includes the whole array.

The best-case time complexity is O(n):

  - Recall the invariant -- at the end of each loop, the minimum unsorted value will always be moved to its sorted position. But what if at the end of the loop, no values have been moved? 

  - Recall that bubble sort compares pairs of immediately adjacent values and swaps them if they're in descending order, but if no values have been moved, than each pair of immediately adjacent values must be in ascending order, and thus the whole array must be in ascending order, and thus is sorted. 

  - This provides the algorithm with an early exit; if no values have been swapped, the array is sorted and the algorithm terminates. But even if the input array was sorted, the algorithm can only determine it by iterating over the whole array once, and thus the best-case time complexity is O(n).

The average/worst-case time complexity is O(n^2):

  - Note that because the lower part will always be made of values smaller than all values in the upper part, the sorted position of the upper part's minimum value is always immediately adjacent to the lower part (because this position is greater than all the sorted values in the lower part, and smaller than all the unsorted values in the upper part).
  
  - This means we never need to iterate over the sorted values; we only iterate over the unsorted values, which decreases by one each loop. Defining 'n' as the number of values for a given array (i.e. the length of the array):

  (n-1) + (n-2) + ... + 2 + 1 + c

  - This is similar to a known mathematical series, where n + (n-1) + ... + 2 + 1 = n(n+1) / 2

  (n(n+1) / 2) - n + c

  ((n^2+n) / 2) - n + c

  (1/2)n^2 + (1/2)n - n + c

  (1/2)n^2 + (-1/2)n + c

  c * n^2 + c * n + c

  - The greatest term is n^2, and thus the average/worst-case time complexity is O(n^2).

The best/average/worst-case space complexity is O(1). Here's an explanation:

  - Bubble sort is in-place, meaning it directly modifies the array without replicating it. Thus, any auxiliary space used is constant:

  c

  - The greatest term is a constant value, and thus the space complexity is O(1).
"""

def bubble_sort(array:list) -> None:
  """
  A stable sorting algorithm that works by traversing an array from the end, to the start where it iteratively accumulates the minimum values in their sorted positions.

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
  n:int = len(array)
  
  for i in range(n):

    swapped:bool = False

    for j in range(n-1, i, -1):
      
      if array[j-1] > array[j]:

        swap(array, j-1, j)
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
  
  array = [3, 0, 2, 9, 4, 7, 6, 5, 8, 1]
  print(array)
  bubble_sort(array)
  print(array)