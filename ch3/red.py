 def my_reduce(func, iterable, initializer=None):
     iterator = iter(iterable)
     if initializer is None:
         try:
             value = next(iterator)
         except StopIteration:
             raise TypeError("Empty sequence with no initial value")
     else:
         value = initializer    
     for element in iterator:
        value = func(value, element)    
    return value
