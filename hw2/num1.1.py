num_of_years = int(input("Введіть кількість років президенства: "))
term = 4
result = num_of_years / term
if result < 1:
    print("Цей президент займає посаду менше 1 терміну")
elif result > 2:
    print("Президент не може займати посаду більше 2 термінів")
else:
    print("Президент займає посаду вже другий термін")