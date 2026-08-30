import pandas as pd
#create a simple dataset
# data = {
#     "hour" : [1,2,3,4,5,6,7,8],
#     "price" : [32.10,41.50,55.80,78.20,91.00,85.50,62.30,45.00],
#     "location": ["ERCOT", "ERCOT", "ERCOT", "ERCOT", "ERCOT", "ERCOT", "ERCOT", "ERCOT"]
# }

# df = pd.DataFrame(data)
# print(df)
# print(df.shape) # rows and columns
# print(df.describe())
# print(df["price"].mean())
# print(df["price"].max())

# high = df[df["price"] > 70]
# print(high)

# # Add a new column
# df["high_price"] = df["price"] > 70
# print(df)

# # Sort by price descending
# df_sorted = df.sort_values("price", ascending=False)
# print(df_sorted)

# Load from CSV
df2 = pd.read_csv("prices.csv")
print(df2)

# Group by location
grouped = df2.groupby("location")["price"].mean()
print(grouped)