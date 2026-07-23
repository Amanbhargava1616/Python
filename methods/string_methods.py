dummy_str: str = "Aman Bhargava"

print(f"{len(dummy_str)}")
print(f"{dummy_str.find("a")}")
print(f"{dummy_str.find("A")}")
print(f"{dummy_str.find("C")}")
print(f"{dummy_str.rfind("a")}")
print(f"{dummy_str.capitalize()}")
print(f"{dummy_str.upper()}")
print(f"{dummy_str.lower()}")
print(f"{dummy_str.isalpha()}")  # returns true only if string contains alphabets and if string have space returns false
print(f"{dummy_str.isdigit()}")
print(f"{dummy_str.count("a")}")
print(f"{dummy_str.replace("a","A")}")
print(help(str))
