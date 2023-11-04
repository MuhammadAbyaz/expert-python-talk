# top-level syntax, function -> underscore methods
from time import sleep


# generator implementation
class Compute:

  def __iter__(self):
    self.last = 0
    return self

  def __next__(self):
    rv = self.last
    self.last += 1
    if self.last > 10:
      raise StopIteration()
    sleep(0.5)
    return rv


# generator


def compute():
  for i in range(10):
    sleep(0.5)
    yield i


for val in Compute():
  print(val)

# sub-routine has one starting point it starts and finishes and gives the final result
# where as in co-routine it starts and gives user the result one by one
# with generators you can write code that can interleave with other code
# generators forces a sequence on us 
