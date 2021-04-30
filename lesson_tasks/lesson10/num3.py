def mult_num():
    a = int(input("Введите число: "))
    for b in range(0, 10):
        c = a * b
        b += 1
        print(c)


print(mult_num())
