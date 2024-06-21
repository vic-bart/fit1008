"""
Hi! This file defines a dynamic array, a data structure that supports random-access of an unknown number of stored values.
Here's an example:

  >> array = DynamicArray(3)
"""

from typing import Any
from static_array import StaticArray

class DynamicArray():

  def __init__(self) -> None:
    self.array:StaticArray = StaticArray(1)
    self.resize_factor:int = 2

  def __len__(self) -> int:
    return len(self.array)
  
  def is_empty(self) -> bool:
    if len(self) == 0:
      return True
    return False
  
  def __setitem__(self, i:int, value:Any) -> None:
    self.array[i] = value

  def __getitem__(self, i:int) -> Any:
    return self.array[i]
  
  def append(self, value:Any) -> None:
    if self.array.is_full():
      self._resize()
    self.array.append(value)

  def find(self, value:Any) -> int:
    return self.array.find(value)
    
  def __delitem__(self, i:int) -> None:
    del self.array[i]

  def _resize(self) -> None:
    resized_array:StaticArray = StaticArray(len(self) * self.resize_factor)
    for value in self.array:
      resized_array.append(value)
    self.array = resized_array
  
  def __str__(self) -> str:
    return str(self.array)
  
if __name__ == "__main__":

  dynamic_array:DynamicArray = DynamicArray()

  print(dynamic_array, len(dynamic_array))
  dynamic_array.append(1)
  dynamic_array.append(3)
  dynamic_array.append(2)
  print(dynamic_array, len(dynamic_array))

  print(dynamic_array[0], dynamic_array[1], dynamic_array[2])
  dynamic_array[0] = 4
  dynamic_array[1] = 6
  dynamic_array[2] = 5

  print(dynamic_array, len(dynamic_array))
  i = dynamic_array.find(6)
  del dynamic_array[i]
  print(dynamic_array, len(dynamic_array))

  dynamic_array.append(7)
  print(dynamic_array, len(dynamic_array))