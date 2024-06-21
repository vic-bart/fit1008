"""
Hi! This file defines a static array, a data structure that supports random-access of a known number of stored values.
Here's an example:

  >> array = StaticArray(3)

  - Values are stored in memory, which is allocated to the array when initialised.

  - But what if the number of values we want to store is unknown? This would require a dynamic array, which 
"""

from typing import Any

class StaticArray():

  def __init__(self, size:int) -> None:
    self.array:list = [None for _ in range(size)]
    self.length:int = 0
    self.size:int = size

  def __len__(self) -> int:
    return self.length
  
  def is_full(self) -> bool:
    if len(self) == self.size:
      return True
    return False
  
  def is_empty(self) -> bool:
    if len(self) == 0:
      return True
    return False
  
  def __setitem__(self, i:int, value:Any) -> None:
    if (i < 0) or (i >= len(self)):
      raise IndexError
    self.array[i] = value

  def __getitem__(self, i:int) -> Any:
    return self.array[i]
  
  def append(self, value:Any) -> None:
    self.length += 1
    self[len(self)-1] = value

  def find(self, value:Any) -> int:
    for i in range(len(self)):
      if self[i] == value:
        return i
    raise ValueError
    
  def __delitem__(self, i:int) -> None:
    if (i < 0) or (i >= len(self)):
      raise IndexError
    self.length -= 1
    for i in range(i, len(self)):
      self[i] = self[i + 1]
  
  def __str__(self) -> str:
    return str(self.array[:self.length])
  
if __name__ == "__main__":

  static_array:StaticArray = StaticArray(3)

  print(static_array, len(static_array))
  static_array.append(1)
  static_array.append(3)
  static_array.append(2)
  print(static_array, len(static_array))

  print(static_array[0], static_array[1], static_array[2])
  static_array[0] = 4
  static_array[1] = 6
  static_array[2] = 5

  print(static_array, len(static_array))
  i = static_array.find(6)
  del static_array[i]
  print(static_array, len(static_array))

  static_array.append(7)
  print(static_array, len(static_array))
