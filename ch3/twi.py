 def apply_twice(func, value):
     return func(func(value))
 print(apply_twice(lambda x: x + 1, 5))
