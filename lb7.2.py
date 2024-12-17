class ThreeNumbers:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __del__(self):
        print(f"Вы уничтожили объект (•‿•) {self}")

    def geometric_mean(self):
        if self.x >= 0 and self.y >= 0 and self.z >= 0:
            result = (self.x * self.y * self.z) ** (1 / 3)
            return result
        else:
            return "Присутствуют отрицательные числа"

    def how_numbers(self):
        sum_x_y_z = self.x + self.y + self.z
        return len(str(int(sum_x_y_z)))

    def __str__(self):
        return (f"x = {self.x}, y = {self.y}, z = {self.z}\n"
                f"Среднее геометрическое: {self.geometric_mean()}\n"
                f"Количество цифр в сумме: {self.how_numbers()}")

if __name__ == "__main__":
    numbers = ThreeNumbers(4.5, 2, 8.0)
    del numbers
