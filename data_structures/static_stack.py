"""
"""

from typing import Any

class Stack():

  def __init__(self, size:int) -> None:
    self.array = [None for _ in range(size)]
    self.top = 0
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
  
  def push(self, value:Any) -> None:
    if self.is_full():
      raise Exception("Stack is full")
    self.array[self.top] = value
    self.top += 1
    self.length += 1

  def peek(self) -> Any:
    if self.is_empty():
      raise Exception("Stack is empty")
    return self.array[self.top-1]
  
  def pop(self) -> Any:
    if self.is_empty():
      raise Exception("Stack is empty")
    self.top -= 1
    self.length -= 1
    return self.array[self.top]

  def __str__(self) -> str:
    values = self.array[:self.top]
    values.reverse()
    return str(values)
  
if __name__ == "__main__":

  stack:Stack = Stack(3)
  print(stack, len(stack))
  stack.push(1)
  stack.push(3)
  stack.push(2)
  print(stack, len(stack))
  print(stack.peek())
  print(stack, len(stack))
  print(stack.pop())
  print(stack, len(stack))
  stack.pop()
  print(stack, len(stack))
  stack.pop()
  print(stack, len(stack))