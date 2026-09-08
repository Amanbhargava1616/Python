user_data: dict = {
    "fname": "aman",
    "lname": "bhargava",
    "age": 25,
    "fathername": "ashish",
}


print(user_data.get("fname"))
print(user_data.get("mothername", "sonia"))

# Adding a new key, value
user_data.update({"mothername": "sonia"})
print(user_data)

# updating an old value using key
user_data.update({"fname": "Aman"})
print(user_data)


print(user_data.pop("age"))
print(user_data)

print(user_data.popitem())
print(user_data)
