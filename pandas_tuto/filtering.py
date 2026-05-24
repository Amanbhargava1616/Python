import pandas as pd


people = pd.read_csv(
    r"C:\Users\amaab\OneDrive\Desktop\Python\pandas_tuto\MOCK_DATA.csv"
)

males = people[people["gender"] == "Male"]

print(males[["first_name", "last_name"]])
