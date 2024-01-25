# Определение класса "Gamer"
# Необходимо добавить поля nickaname и email
# Допиши код
class Gamer:
    def __init__(self, name, age, nickaname, email):
        self.name = name
        self.age = age

        self.games = []

    def add_game(self, game):
        self.games.append(game)

# Вызов данной функции выводит сообщение "Привет, меня зовут Иван, мне 14 лет."
# А должен вывести сообщение "Привет, меня зовут Иван, мне 14 лет. Всегда на связи по john@gmail.com. Ищи меня в игре по нику John"
# Допиши код, чтобы выводилось правильное сообщение
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет.")

# Создание экземпляра класса "Gamer"
gamer1 = Gamer("Иван", 14, "John", "john@gmail.com")

# Добавление игр
gamer1.add_game("Minecraft")
gamer1.add_game("Dota 2")

# Минипрезентация геймера
gamer1.introduce()

# Вывод любимых игр
print(f"{gamer1.name} любит игры: {', '.join(gamer1.games)}")
