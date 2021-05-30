class Human:
    default_name = "Боб"
    default_age = 30

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 20000
        self.__house = None

    def info(self):
        print(f'Имя: {self.name}')
        print(f'Возраст: {self.age}')
        print(f'Количество денег: {self.__money}')
        print(f'Наличие дома: {self.__house}')

    def default_info():
        print(f'Имя по умолчанию: {Human.default_name}')
        print(f'Возраст по умолчанию: {Human.default_age}')

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, amount):
        self.__money += amount
        print(f'Заработал {amount} грн! Текущий баланс: {self.__money} грн')

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print("Недостаточно денег")


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'Цена со скидкой: {final_price}')
        return final_price


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


man = Human()
man.info()
Human.default_info()
man.earn_money(20000)
small_house = SmallHouse(8500)
man.buy_house(small_house, 3)
man.info()
