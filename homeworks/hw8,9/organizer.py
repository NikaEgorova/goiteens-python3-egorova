import datetime
print("Привет! Это твой личный календарь-органайзер")
x = datetime.datetime.now()
print("Сейчас", x.strftime("%X"))
print("Пожалуйста, выбери функцию:")
print("1. Создать новую заметку")
print("2. Добавить заметку на сегодня")
print("3. Просмотреть все заметки")
print("4. Завершить")
print("Пожалуйста, введи цифру от 1 до 4")
while True:
    message_of_user = input()
    if message_of_user == "1":
        from datetime import datetime
        while True:
            new_date = input("Укажи дату в формате гггг/мм/дд: ")
            try:
                year, month, day = map(int, new_date.split('/'))
                date = datetime(year, month, day)
                break
            except ValueError:
                print("Неверный формат даты. Попробуй еще раз!")
        new_note = input("Введи новую заметку: ")
        while True:
            new_priority = int(
                input("Установи приоритет заметки от 1 до 5, где 5 - наибольший приоритет: "))
            if new_priority > 5:
                print("Неправильное значение. Попробуй еще раз!")
            else:
                break
        new_priority1 = str(new_priority)
        calendar = open("calendar.txt", "a")
        calendar.write("\n" + new_date + " - " + new_note +
                       ". Приоритет: " + new_priority1)
        calendar.close()
        print("Поздравляю! Ты создал новую заметку. Хочешь продолжить работу?")
    if message_of_user == "2":
        print("Ты хочешь добавить заметку на текущий день. Напоминаю сегодня: ",
              x.strftime("%x"))
        new_note = input("Введи новую заметку: ")
        while True:
            new_priority = int(
                input("Установи приоритет заметки от 1 до 5, где 5 - наибольший приоритет: "))
            if new_priority > 5:
                print("Неправильное значение. Попробуй еще раз!")
            else:
                break
        new_priority1 = str(new_priority)
        calendar = open("calendar.txt", "a")
        calendar.write("\n" + x.strftime("%x") + " - " + new_note +
                       ". Приоритет: " + new_priority1)
        calendar.close()
        print(
            "Поздравляю! Ты добавил заметку на сегодняшний день. Хочешь продолжить работу?")
    if message_of_user == "3":
        print("Вот список заметок:")
        calendar = open("calendar.txt", "r")
        print(calendar.read())
        print("\nПродолжаем работать?")
    if message_of_user == "4":
        print("Спасибо за работу;) Пока!")
        break
    new_message_of_user = input("Введи: Да или Нет \n")
    if new_message_of_user == "Да":
        print("Супер! Тогда введи, пожалуйста, число от 1 до 4")
    else:
        print("Спасибо за работу;) Пока!")
        break
