import datetime
x = datetime.datetime.now()
print(x.strftime("%X"))
i = int(x.strftime("%H"))
m = int(x.strftime("%M"))
s = int(x.strftime("%S"))
print(i * 60 + m, "хвилин")
print(i * 3600 + m * 60 + s, "секунд")
