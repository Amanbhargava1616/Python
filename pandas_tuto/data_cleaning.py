import pandas as pd

user_data = pd.read_csv(
    filepath_or_buffer=r"C:\Users\amaab\OneDrive\Desktop\Python\pandas_tuto\MOCK_DATA.csv",
    index_col="id",
)

# 1. Drop a column
user_data_no_ip_address_column = user_data.drop(columns=["ip_address"])

# 2. Drop a row
user_data_no_3_index = user_data.drop(index=(3))

# 3. Drop a row and column
user_data_no_4_index_and_ip_address_column = user_data.drop(
    index=(4), columns=["ip_address"]
)

# print(user_data_no_ip_address_column)
# print(user_data_no_3_index)
# print(user_data_no_4_index_and_ip_address_column)


# 4. Handle missing data

# dropna => drop not available
drop_row_with_no_last_name = user_data.dropna(subset=["last_name"])
print(drop_row_with_no_last_name)

# fillna => fill not available
fill_last_name_with_a_value = user_data.fillna(value={"last_name": "bhargava"})
print(fill_last_name_with_a_value)

# 5. Inconsistent data
fill_last_name_with_a_value["last_name"] = fill_last_name_with_a_value[
    "last_name"
].replace({"bhargava": "Bhargava"})
print(fill_last_name_with_a_value)


# 6. Standardize text
user_data["last_name"] = user_data["last_name"].str.lower()
print(user_data)

# 7. Drop duplicates
fill_last_name_with_a_value = fill_last_name_with_a_value.drop_duplicates()
print(fill_last_name_with_a_value)
