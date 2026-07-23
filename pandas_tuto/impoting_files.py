import pandas as pd

csv_data = pd.read_csv(r"C:\Users\amaab\OneDrive\Desktop\Python\pandas_tuto\MOCK_DATA.csv", index_col="id")

print(csv_data.to_string())

print(csv_data[["first_name", "email"]])

print(csv_data.loc[[4], ["first_name", "last_name"]])
print(csv_data.loc[4:9, ["first_name", "last_name"]])


first_name = input("Enter user first name: ")
try:
    print(csv_data[csv_data["first_name"] == first_name])
except KeyError:
    raise Exception("Error in reading file data")
