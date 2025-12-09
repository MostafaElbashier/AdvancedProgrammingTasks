solution
import pandas as pd
data={
    "Name": ["Ahmed", "Mostafa", "Omar", "Ziad"],
    "Age": [20, 22, 21, 23],
    "Score": [83, 20, 67, 90]
}
df=pd.DataFrame(data)
result=df[df["Score"] > 80]
print(result)
