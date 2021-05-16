class GameHero:
    def __init__(self, name, health_points, attack_points):
        self.name = name
        self.health_points = health_points
        self.attack_points = attack_points

    def say_hello(self):
        print("Our hero", self.name, "said hello")

    def compare_damage_health(self):
        result = self.health_points - self.attack_points
        print("Різниця = ", result)


Mario = GameHero("Mario", 100, 15)
Mario.say_hello()
Mario.compare_damage_health()
Mushroom = GameHero("Mushroom", 20, 5)
Mushroom.say_hello()
Mushroom.compare_damage_health()
Turtle = GameHero("Turtle", 50, 20)
Turtle.say_hello()
Turtle.compare_damage_health()
