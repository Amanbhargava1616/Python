import pandas as pd

# Below is a data frame
user_data = pd.DataFrame(
    data={
        "Name": ["Aman", "Aditi", "Ashu"],
        "Age": [24, 23, 23],
        "City": ["Udaipur", "Jaipur", "Jaipur"],
    },
    index=["a", "b", "c"],
)

print(user_data)
print(f"Max from age series: {user_data['Age'].max()}")
print(user_data.describe())
print(f"User Data at loc a is: {user_data.loc('a')}")

print("-------------------------------------------------------------")

# Below is a series
is_smart = pd.Series(
    data=[True, False, False],
    index=["a", "b", "c"],
    name="Is Smart",
)

print(is_smart)
print(is_smart.count())
print(is_smart.iloc[1])

print("-------------------------------------------------------------")

# Below is series using a dict
day_count_dict = {
    "Jan": 20,
    "Dec": 22,
    "Feb": 20,
}
day_count = pd.Series(data=day_count_dict)
print(day_count)


# Filtering
print(day_count[day_count == 20])
