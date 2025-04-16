import pandas as pd
data = { "Name": ["Lily","Henry","Rose","Will","Elizabeth"],
         "Age": [ 30,25,18,35,40],
         "City": ["London","Chicago","Edinburgh","Paris","Paris"] }
df = pd.DataFrame(data)
filtered_df = df[(df["Age"] < 30) |
 (df["City"] == "Paris")]
print(filtered_df)
                 