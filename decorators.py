from time import time


def timer(func):

  def function(*args, **kwargs):
    before = time()
    rv = func(*args, **kwargs)
    after = time()
    print("time elapsed", after - before)
    return rv

  return function


@timer
def add(x, y):
  return x + y


@timer
def sub(x, y=10):
  return x - y


print("add(10)", add(10, 10))
print("add(20, 30)", add(20, 30))
print("add('a','b')", add("a", "b"))


# ntimes decorators

def ntime(n):
  def inner(f):
    def wrapper(*args, **kwargs):
      for _ in range(n):
       rv = f(**args, **kwargs)
      return rv
    return wrapper
  return inner