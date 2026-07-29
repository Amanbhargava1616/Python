import time


def add_salt(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Salt Added")
        result = func(*args, **kwargs)
        print(f"Time to prepare Dish: {time.time()-start_time}")
        return result

    return wrapper


@add_salt
def prepare_baati(salt: int = 10, ghee: int = 1):
    qty: int = salt * ghee
    time.sleep(5)
    return qty


if __name__ == "__main__":
    print(f"Dish: {prepare_baati()}")
