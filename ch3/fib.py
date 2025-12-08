 import functools
 import time
 @functools.lru_cache(maxsize=None)
 def fibonacci(n):
     if n < 2:
         return n
     return fibonacci(n-1) + fibonacci(n-2)
start_time = time.time()
print(f"Fibonacci(35) = {fibonacci(35)}")
end_time = time.time()
print(f"Time taken: {end_time - start_time:.5f} seconds")
