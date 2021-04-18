def div_by_two(a, b):
    c = a % b
    return c


num_of_prod = int(input("Введіть кількість продуктів у кошику: "))
result = div_by_two(num_of_prod, 2)
if result == 0:
    print("Акція діє!")
else:
    print("Акція не діє.")
