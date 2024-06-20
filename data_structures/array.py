"""
"""

from typing import Any

class Array():

  def __init__(self, size:int) -> None:
    self.array = [None for _ in range(size)]
    self.length = 0
    self.size = size

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
    self.array[i] = value
    if self.array[i] is None:
      self.length += 1
    if value is None:
      self.length -= 1

  def __getitem__(self, i:int) -> Any:
    return self.array[i]
  
  def __str__(self) -> str:
    return str(self.array[:self.length])
  
if __name__ == "__main__":

  array:Array = Array(3)
  print(array, len(array))
  array[0] = 1
  array[1] = 3
  array[2] = 2
  print(array, len(array))