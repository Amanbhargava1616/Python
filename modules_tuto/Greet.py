def Greet(name: str):
    print(f"Hello from {name}, this is Greet function from module1")


if __name__ == "__main__":
    user_name = input("Enter User name: ")
    Greet(user_name)
