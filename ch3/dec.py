 def log_call(func):
     def nestedFunc(*args, **kwargs):
         print(f"--- Calling function: {func.__name__} ---")
         result = func(*args, **kwargs)
         print(f"--- Finished function: {func.__name__} ---")
         return result
     return nestedFunc
