import datetime
print("Привет! Это твой личный календарь-органайзер")
x = datetime.datetime.now()
print("Сейчас", x.strftime("%X"))
print("Пожалуйста, выбери функцию:")
print("1. Создать новую заметку")
print("2. Просмотреть все заметки")
print("3. Завершить")
print("Пожалуйста, введи число от 1 до 3")
while True:
    message_of_user = input()
    if message_of_user == "1":
        new_note = input("Введи новую заметку: ")
        new_date = input("Не забудь указать дату: ")
        calendar = open("calendar.txt", "a")
        calendar.write("\n" + new_date + " - " + new_note)
        calendar.close()
        print("Поздравляю! Ты создал новую заметку. Хочешь продолжить работу?")
        new_message_of_user = input("Введи: Да или Нет \n")
        if new_message_of_user == "Да":
            print("Супер! Тогда введи, пожалуйста, число от 1 до 3")
        else:
            print("Спасибо за работу;) Пока!")
            break
    if message_of_user == "2":
        print("Вот список заметок:")
        calendar = open("calendar.txt", "r")
        print(calendar.read())
        print("\nПродолжаем работать?")
        new_message_of_user = input("Введи: Да или Нет \n")
        if new_message_of_user == "Да":
            print("Супер! Тогда введи, пожалуйста, число от 1 до 3")
        else:
            print("Спасибо за работу;) Пока!")
            break
    if message_of_user == "3":
        print("Спасибо за работу;) Пока!")
        break
