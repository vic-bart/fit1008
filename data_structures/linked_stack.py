"""
"""

from typing import Any
from node import Node

class LinkedStack():

  def __init__(self) -> None:
    self.top = Node()
    self.length = 0

  def __len__(self) -> int:
    return self.length
  
  def is_empty(self) -> bool:
    if len(self) == 0:
      return True
    return False
  
  def push(self, value:Any) -> None:
    self.top.set_value(value)
    node = Node()
    node.set_link(self.top)
    self.top = node
    self.length += 1

  def peek(self) -> Any:
    if self.is_empty():
      raise Exception("Stack is empty")
    node = self.top.get_link()
    return node.get_value()
  
  def pop(self) -> Any:
    if self.is_empty():
      raise Exception("Stack is empty")
    node = self.top.get_link()
    value = node.get_value()
    self.top = node
    self.length -= 1
    return value

  def __str__(self) -> str:
    values:list = []
    node = self.top
    while node.get_link() is not None:
      node = node.get_link()
      values.append(node.get_value())
    return str(values)
  
if __name__ == "__main__":

  linked_stack:LinkedStack = LinkedStack()
  print(linked_stack, len(linked_stack))
  linked_stack.push(1)
  linked_stack.push(3)
  linked_stack.push(2)
  print(linked_stack, len(linked_stack))
  print(linked_stack.peek())
  print(linked_stack, len(linked_stack))
  print(linked_stack.pop())
  print(linked_stack, len(linked_stack))
  linked_stack.pop()
  print(linked_stack, len(linked_stack))
  linked_stack.pop()
  print(linked_stack, len(linked_stack))