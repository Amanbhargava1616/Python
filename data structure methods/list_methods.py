lst: list = ["Aman", 23, "Jaipur", 900000.00, "Aman"]


print(lst.index("Aman"))
lst.append("Bhargava")
print(lst)
lst2 = lst.copy()
print(lst2)
lst2.clear()
print(lst2)
print(lst)
print(lst.count("Aman"))
lst.insert(4, "Ashish")
print(lst)
lst.reverse()
print(lst)
