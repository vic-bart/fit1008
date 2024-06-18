"""
Hi! This file defines insertion sort for arrays, an unstable sorting algorithm that works by partitioning an array in two, where the lower sorted half iteratively accumulates the minimum values of the upper unsorted 
half. 

"""

def insertion_sort(array:list) -> None:
  """
  """
  for i in range(1, len(array)):

    value:int = array[i]
    j:int = i - 1

    while (j >= 0) and (array[j] > value):
      
      array[j+1] = array[j]
      j = j - 1
      
    array[j + 1] = value


if __name__ == "__main__":
  
  array = [3, 2, 1, 9, 4, 7, 6, 5, 8, 0]
  print(array)
  insertion_sort(array)
  print(array)