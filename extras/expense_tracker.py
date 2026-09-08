from typing import DefaultDict

total_amt: float = float(input("Enter the total amount (example $10.32): "))

person_dict: dict[str, float] = {}
i: int = 1
while True:
    person: str = input(f"Enter Person {i} name or 'ENTER' if that's all: ")
    i += 1
    if person.strip() == "":
        break
    person_dict.update({person: 0.0})

print("=" * 60)
print(f"Current Amount: {total_amt}")
for person in person_dict.keys():
    print("=" * 60)
    amt: float = float(input(f"Enter {person} split (example $10.32): "))
    person_dict[person] = amt
    print(f"Total Remaining Amount: {total_amt - sum(person_dict.values())}")
    print(f"Current Split: {person_dict}")
