"""
"""

from typing import Any

class Queue():

  def __init__(self, size:int) -> None:
    self.array = [None for _ in range(size)]
    self.front = 0
    self.back = 0
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
  
  def append(self, value:Any) -> None:
    if self.is_full():
      raise Exception("Queue is full")
    self.array[self.back] = value
    self.back = (self.back + 1) % self.size
    self.length += 1

  def peek(self) -> Any:
    if self.is_empty():
      raise Exception("Queue is empty")
    return self.array[self.front]
  
  def pop(self) -> Any:
    if self.is_empty():
      raise Exception("Queue is empty")
    value = self.array[self.front]
    self.front = (self.front + 1) % self.size
    self.length -= 1
    return value

  def __str__(self) -> str:
    values:list = []
    i = self.front
    for _ in range(len(self)):
      values.append(self.array[i])
      i = (i + 1) % self.size
    return str(values)
  
if __name__ == "__main__":

  queue:Queue = Queue(3)
  print(queue)
  queue.append(1)
  queue.append(3)
  queue.append(2)
  print(queue)
  print(queue.peek())
  print(queue)
  print(queue.pop())
  print(queue)
  queue.pop()
  print(queue)
  queue.pop()
  print(queue)