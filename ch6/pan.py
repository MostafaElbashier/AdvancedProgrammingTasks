import pandas as pd 
data = { 
"ID": [1, 2, 3], 
"Name": ["Mostafa", "Yasser", "Salah"], 
"Salary": [5000, 6200, 4800] 
} 
df = pd.DataFrame(data) 
df.to_excel("employees.xlsx", index=False) 
loaded_df = pd.read_excel("employees.xlsx") 
print(loaded_df[["Name", "Salary"]])
