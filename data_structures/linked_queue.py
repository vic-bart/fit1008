"""
"""

from typing import Any
from node import Node

class LinkedQueue():

  def __init__(self) -> None:
    node = Node()
    self.front = node
    self.back = node
    self.length = 0

  def __len__(self) -> int:
    return self.length
  
  def is_empty(self) -> bool:
    if len(self) == 0:
      return True
    return False
  
  def append(self, value:Any) -> None:
    self.back.set_value(value)
    node = Node()
    self.back.set_link(node)
    self.back = node
    self.length += 1

  def peek(self) -> Any:
    if self.is_empty():
      raise Exception("Queue is empty")
    return self.front.get_value()
  
  def pop(self) -> Any:
    if self.is_empty():
      raise Exception("Queue is empty")
    value = self.front.get_value()
    self.front = self.front.get_link()
    self.length -= 1
    return value

  def __str__(self) -> str:
    values:list = []
    node = self.front
    while node.get_link() is not None:
      values.append(node.get_value())
      node = node.get_link()
    return str(values)
  

if __name__ == "__main__":

  linked_queue:LinkedQueue = LinkedQueue()
  print(linked_queue, len(linked_queue))
  linked_queue.append(1)
  linked_queue.append(3)
  linked_queue.append(2)
  print(linked_queue, len(linked_queue))
  print(linked_queue.peek())
  print(linked_queue, len(linked_queue))
  print(linked_queue.pop())
  print(linked_queue, len(linked_queue))
  linked_queue.pop()
  print(linked_queue, len(linked_queue))
  linked_queue.pop()
  print(linked_queue, len(linked_queue))