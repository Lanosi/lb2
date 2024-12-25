class Instrument:
    def __init__(self, name):
        self.name = name

    def use(self):
        raise NotImplementedError("Метод должен быть переопределен в подклассе.")


class Hammer(Instrument):
    def use(self):
        return f"{self.name}: Забиваю гвозди."


class Guitar(Instrument):
    def use(self):
        return f"{self.name}: Играю мелодию."


# Пример использования полиморфизма
if __name__ == "__main__":
    instruments = [
        Hammer("Молоток"),
        Guitar("Гитара"),
    ]

    for instrument in instruments:
        print(instrument.use())
