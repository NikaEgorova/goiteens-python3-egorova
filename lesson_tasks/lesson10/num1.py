import datetime


def my_date():
    x = datetime.datetime.now()
    return x.strftime("%x")


print(my_date())
