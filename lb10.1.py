class Instrument:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def use(self):
        raise NotImplementedError("Метод должен быть переопределен в подклассе.")


class Hammer(Instrument):
    def __init__(self, name, weight):
        super().__init__(name, "строительный")
        self.weight = weight

    def use(self):
        return f"Использую {self.name} весом {self.weight} кг для забивания гвоздей."


class Guitar(Instrument):
    def __init__(self, name, strings):
        super().__init__(name, "музыкальный")
        self.strings = strings

    def use(self):
        return f"Играю на инструменте {self.name} с {self.strings} струнами."


class Sound:
    def __init__(self, instrument_name, description):
        self.instrument_name = instrument_name
        self.description = description

    def play_sound(self):
        return f"Звук инструмента {self.instrument_name}: {self.description}"


# Пример использования
if __name__ == "__main__":
    hammer = Hammer("Молоток", 2)
    guitar = Guitar("Гитара", 6)

    print(hammer.use())
    print(guitar.use())

    hammer_sound = Sound(hammer.name, "громкий металлический звук")
    guitar_sound = Sound(guitar.name, "мелодичный аккорд")

    print(hammer_sound.play_sound())
    print(guitar_sound.play_sound())
