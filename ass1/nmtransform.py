marks = [[47, 84, 74], [95, 63, 105], [92, 80, 97]] 
print(list(map(lambda row: list(map(lambda x: round(x * 1.05), row)), 
marks)
