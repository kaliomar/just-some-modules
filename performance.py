from time import time


def performance(function):
  def wrapper(*args, **kwargs):
    t1 = time()
    result = function(*args, **kwargs)
    t2 = time()
    print(f'time to execute = {t2-t1}')
    return result
  return wrapper
