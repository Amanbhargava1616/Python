import pandas as pd

user_df = pd.DataFrame(
    data={
        "Name": ["Aman", "Ashu", "Ashwin"],
        "Age": [24, 23, 23],
        "City": ["Jaipur", "Jaipur", "Chumela"],
    },
    index=["Student 1", "Student 2", "Student 3"],
)

# Add a new Column (Series)
user_df["Job"] = ["BE", "FE", "QA"]

# Add a new Single Row
new_user_1 = pd.DataFrame(
    data={
        "Name": "Akshat",
        "Age": 22,
        "City": "Kota",
        "Job": "DevOps",
    },
    index=["Student 4"],
)

# Add new Rows
new_user_2 = pd.DataFrame(
    data=[
        {
            "Name": "Harsh",
            "Age": 23,
            "City": "Jaipur",
            "Job": "BE",
        },
        {
            "Name": "Kunal",
            "Age": 21,
            "City": "Jaipur",
            "Job": "BE",
        },
    ],
    index=["Student 5", "Student 6"],
)

print(user_df)
print(new_user_1)
print(new_user_2)

combined_df = pd.concat([user_df, new_user_1, new_user_2])
print(combined_df)
