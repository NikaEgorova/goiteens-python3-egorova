def sum_of_num(a, b):
    c = a + b
    return c


def diff_of_num(a, b):
    c = a - b
    return c


def div_of_num(a, b):
    c = a / b
    return c


def multip_of_num(a, b):
    c = a * b
    return c


while True:
    first_num = int(input("Введите первое число: "))
    second_num = int(input("Введите второе число: "))
    action = input(
        "Какое действие совершить?\n1. Сложение\n2. Вычитание\n3. Деление\n4. Умножение\nВведите цифру от 1 до 4: ")
    if action == "1":
        result = sum_of_num(first_num, second_num)
        print(first_num, "+", second_num, "=", result)
    elif action == "2":
        result = diff_of_num(first_num, second_num)
        print(first_num, "-", second_num, "=", result)
    elif action == "3":
        result = div_of_num(first_num, second_num)
        print(first_num, "/", second_num, "=", result)
    else:
        result = multip_of_num(first_num, second_num)
        print(first_num, "*", second_num, "=", result)

    print("Хотите продолжить?")
    decision = input("Введите: Да или Нет\n")
    if decision == "Да":
        continue
    else:
        break
