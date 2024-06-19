"""
"""

from typing import Any, TypeVar
Node = TypeVar("Node")

class Node():

  def __init__(self) -> None:
    self.link = None
    self.value = None

  def __str__(self) -> str:
    return str(self.value)

  def set_link(self, node:Node) -> None:
    self.link = node

  def get_link(self) -> Node:
    return self.link
  
  def set_value(self, value:Any) -> None:
    self.value = value

  def get_value(self) -> Any:
    return self.value

if __name__ == "__main__":
  
  A:Node = Node(1)
  B:Node = Node(2)
  A.set_link(B)
  print(A)
  print(A.link)
  print(B)
  print(B.link)