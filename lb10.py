class Tool:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def use(self):
        return f"Используется инструмент: {self.name}"

class Hammer(Tool):
    def __init__(self, name, material, weight):
        super().__init__(name, material)
        self.weight = weight

    def use(self):
        return f"Используется молоток {self.name}, вес: {self.weight} кг."

class Guitar(Tool):
    def __init__(self, name, material, type_):
        super().__init__(name, material)
        self.type = type_

    def use(self):
        return f"Используется гитара {self.name}, тип: {self.type}"

    def play_sound(self):
        return f"Звук из гитары {self.name}: 'ппииии'"

class Sound:
    def __init__(self, type_, volume):
        self.type = type_
        self.volume = volume

    def generate(self):
        return f"Звук {self.type} с громкостью {self.volume}"

# Пример использования:

# Создаем молоток
hammer = Hammer("Молоток", "Металл", 1.5)
print(hammer.use())  # Используется молоток, вес: 1.5 кг.

# Создаем гитару
guitar = Guitar("Гитара", "Дерево", "Акустическая")
print(guitar.use())  # Используется гитара, тип: Акустическая
print(guitar.play_sound())  # Звук из гитары: 'ппииии'

# Создаем звук
sound = Sound("Удар", "Средняя")
print(sound.generate())  # Звук Удар с громкостью Средняя
