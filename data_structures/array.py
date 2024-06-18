"""
"""

from typing import Any

class Array():

  def __init__(self, size:int) -> None:
    self.array = [None for _ in range(size)]
    self.size = size

  def __len__(self) -> int:
    return len(self.array)
  
  def __setitem__(self, i:int, value:Any) -> None:
    self.array[i] = value

  def __getitem__(self, i:int) -> Any:
    return self.array[i]
  
  def __str__(self) -> str:
    return(str(self.array))