import random

# 1. Generating Numbers
print(random.random())  # Float between 0.0 and 1.0 (exclusive)
print(random.uniform(1.5, 5.5))  # Float between 1.5 and 5.5 (inclusive)
print(random.randint(1, 10))  # Integer from 1 to 10 (inclusive)
print(random.randrange(1, 10, 2))  # Odd integer from 1 to 9 (step-based)

# 2. Working with Sequences
items = ["apple", "banana", "cherry"]
print(random.choice(items))  # Pick a single random item
print(random.choices(items, k=2))  # Pick multiple items (allows duplicates)
print(random.sample(items, k=2))  # Pi ck multiple unique items (no duplicates)

# 3. Mutating Sequences
random.shuffle(items)  # Reorder the list in-place
print(items)
