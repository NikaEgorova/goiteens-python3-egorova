# 4 завдання
prices = [100, 50, 50, 100, 200]
money = 500
if sum(prices) < money:
    print("У нього залишиться", money - sum(prices), "грн")
else:
    print("У нього не залишиться грошей")
