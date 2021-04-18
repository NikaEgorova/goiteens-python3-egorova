pharaons = ("Клеопатра", "Рамзес", "Тутанхамон")
pharaons_list = list(pharaons)
for i in pharaons_list:
    num_of_letters = len(i)
    if num_of_letters > 8:
        print(i)
