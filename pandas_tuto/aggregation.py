import pandas as pd

user_data = pd.read_csv(r"C:\Users\amaab\OneDrive\Desktop\Python\pandas_tuto\MOCK_DATA.csv")


print(user_data.mean(numeric_only=True))
print(user_data.max(numeric_only=True))
print(user_data.min(numeric_only=True))
print(user_data.sum(numeric_only=True))
print(user_data.count())

print(user_data["car_model"].mean(numeric_only=True))
print(user_data["car_model"].max(numeric_only=True))
print(user_data["car_model"].min(numeric_only=True))
print(user_data["car_model"].sum(numeric_only=True))
print(user_data["car_model"].count())

user_data_group_car_model = user_data.groupby("car_model")

print(user_data_group_car_model.describe())
