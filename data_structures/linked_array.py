"""
"""

from typing import Any
from node import Node

class LinkedArray():

  def __init__(self) -> None:
    self.front = Node()
    self.length = 0

  def __len__(self) -> int:
    return self.length
  
  def is_empty(self) -> bool:
    if len(self) == 0:
      return True
    return False
  
  def __setitem__(self, i:int, value:Any) -> None:
    if (i < 0) or (i >= len(self)):
      raise IndexError
    node = self.front
    for _ in range(i):
      node = node.get_link()
    if node.get_value() is None:
      self.length += 1
    if value is None:
      self.length -= 1
    node.set_value(value)

  def __getitem__(self, i:int) -> Any:
    if (i < 0) or (i >= len(self)):
      raise IndexError
    node = self.front
    for _ in range(i):
      node = node.get_link()
    return node.get_value()
  
  def append(self, value:Any) -> None:
    node = self.front
    for _ in range(len(self)):
      node = node.get_link()
    node.set_value(value)
    node.set_link(Node())
    self.length += 1
  
  def find(self, value:Any) -> int:
    node = self.front
    for i in range(len(self)):
      if node.get_value() == value:
        return i
      node = node.get_link()
    raise ValueError
    
  def __delitem__(self, i:int) -> None:
    if (i < 0) or (i >= len(self)):
      raise IndexError
    
    self.length -= 1
    
    if i == 0:
      self.front = self.front.get_link()
    else:
      node:Node = self.front
      for _ in range(i-1):
        node = node.get_link()
      deleted_node:Node = node.get_link()
      node.set_link(deleted_node.get_link())
  
  def __str__(self) -> str:
    values:list = []
    node = self.front
    while node.get_link() is not None:
      values.append(node.get_value())
      node = node.get_link()
    return str(values)
  
  
if __name__ == "__main__":

  linked_array:LinkedArray = LinkedArray()

  print(linked_array, len(linked_array))
  linked_array.append(1)
  linked_array.append(3)
  linked_array.append(2)
  print(linked_array, len(linked_array))

  print(linked_array[0], linked_array[1], linked_array[2])
  linked_array[0] = 4
  linked_array[1] = 6
  linked_array[2] = 5

  print(linked_array, len(linked_array))
  i = linked_array.find(6)
  del linked_array[i]
  print(linked_array, len(linked_array))

  linked_array.append(7)
  print(linked_array, len(linked_array))