"""
Hi! This file defines bubble sort for arrays, a stable sorting algorithm that works by traversing an array from the start, to the end where it iteratively accumulates the greatest values. Here's an example:

  >>  array = [3, 1, 2, 9, 4, 7, 6, 5, 8, 0]

  - To find the greatest value, bubble sort compares immediately adjacent values, shifting the greater of the pair towards the end. 

  for i in (0...n):
    if array[i] > array[i+1]:
      swap array[i] with array[i+1]

  - See what happens when the current value is greater than the next value.

  >>  array = [3, 1, 2, 9, 4, 7, 6, 5, 8, 0]
  
  array[0] > array[1] == True (3 > 1 == True)
  swap array[0] with array[1]

  >>  array = [1, 3, 2, 9, 4, 7, 6, 5, 8, 0]

  - See what happens when the current value is smaller than the next value.

  >>  array = [1, 2, 3, 9, 4, 7, 6, 5, 8, 0]

  array[2] > array[3] == False (3 > 5 == False)
  do nothing

  >>  array = [1, 2, 3, 9, 4, 7, 6, 5, 8, 0]

  - This repeats all the way until the end of the list is reached. 

  >>  array = [1, 2, 3, 4, 7, 6, 5, 8, 0, 9]

  - Notice that the array as a whole is not sorted, but the greatest unsorted value is in its sorted position (i.e. if the array were sorted, the value would have the same position). 
  - In fact, this is an invariant; at the end of each loop, the greatest unsorted value will always be moved to its sorted position. 
  - And since the values are sorted in descending order, the array is partitioned in two -- the lower half contains unsorted values, the upper half contains sorted values. Each loop moves the greatest value from its unsorted position in the lower half, to its sorted position in the upper half.
  - However, because the upper half will always be made of values greater than all values in the lower half, the sorted position of the lower half's greatest value is always immediately adjacent to the start of the upper half (because this position is less than all the sorted values in the upper half, and greater than all the unsorted values in the lower half), meaning the sorted partition increases grows by one value each loop, until it includes the whole array.
"""
def bubble_sort(array:list) -> None:
  
  for n in range(len(array), 1, -1):

    swapped:bool = False

    for i in range(n-1):

      if array[i] > array[i+1]:
        # print(f"{array}, n: {n}, i: {i}")
        swap(array, i, i+1)
        swapped = True

    if not swapped:
      break

def swap(array:list, i:int, j:int) -> None:

  item = array[i]
  array[i] = array[j]
  array[j] = item


if __name__=="__main__":

  array = [3, 1, 2, 9, 4, 7, 6, 5, 8, 0]
  print(array)
  bubble_sort(array)
  print(array)