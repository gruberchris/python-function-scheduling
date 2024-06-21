import schedule
from datetime import datetime


def print_current_date_and_time_task():
    print("Current date and time: ", datetime.now())


def print_my_name(name: str):
    print("My name is: ", name)


def print_quarter(quarter: str):
    print(next(quarter) + " quarter")


def make_quarter_message():
    while True:
        for i in ["first", "second", "third", "fourth"]:
            yield i


def print_give_quarter():
    print("Give quarter!")


def print_never_again():
    print("This will never be printed again!")
    return schedule.CancelJob


def print_make_way_message():
    print("Make way!")


if __name__ == "__main__":
    schedule.every(30).seconds.do(print_current_date_and_time_task)
    schedule.every().minute.at(":15").do(print_my_name, "John Doe")
    schedule.every(1).minutes.do(print_give_quarter)
    schedule.every(15).seconds.do(print_quarter, make_quarter_message())
    schedule.every().second.do(print_never_again)
    schedule.every(1).to(15).seconds.do(print_make_way_message)

    while True:
        schedule.run_pending()
