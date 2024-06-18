"""
"""

from typing import Any, TypeVar
Node = TypeVar("Node")

class Node():

  def __init__(self, value:Any) -> None:
    self.value = value
    self.link = None

  def __str__(self) -> str:
    return str(self.value)

  def link(self, node:Node) -> None:
    self.link = node

if __name__ == "__main__":
  A:Node = Node(1)
  B:Node = Node(2)
  A.link(B)
  print(A)
  print(A.link)
  print(B)
  print(B.link)