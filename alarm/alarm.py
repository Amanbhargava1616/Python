from datetime import datetime
from time import sleep


def alarm():
    alarm_time = input("Enter the time for alarm (HH:MM): ")

    now = datetime.now()

    try:
        alarm_datetime: datetime = datetime.strptime(f"{now:%Y-%m-%d} {alarm_time}", "%Y-%m-%d %H:%M")
    except ValueError:
        raise ValueError("Time must be in HH:MM format (24-hour).")

    while True:
        curr_time = datetime.now()
        if curr_time >= alarm_datetime:
            print(f"Alram ringed")
            # Play a native system file path
            break
        else:
            print(curr_time)
            sleep(1)


if __name__ == "__main__":
    alarm()
