numbers = [5, 10, 15, 20, 25] 
min_val = min(numbers) 
max_val = max(numbers) 
normalized = list(map(lambda x: (x - min_val) / (max_val - min_val), 
numbers)) 
print(normalized)
