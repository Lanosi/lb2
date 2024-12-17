class Main:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.data)

    def __add__(self, other):
        """Перегрузка оператора + для сложения с другой матрицей или числом."""
        if isinstance(other, Main):
            # Сложение двух матриц одинакового размера
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("Матрицы должны быть одного размера для сложения.")
            result = [
                [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
                for i in range(self.rows)
            ]
            return Main(result)
        elif isinstance(other, (int, float)):
            # Сложение матрицы с числом
            result = [
                [self.data[i][j] + other for j in range(self.cols)]
                for i in range(self.rows)
            ]
            return Main(result)
        else:
            raise TypeError("Неподдерживаемый тип для сложения с матрицей.")

    def __eq__(self, other):
        """Перегрузка оператора == для сравнения двух матриц."""
        if not isinstance(other, Main):
            return False
        return self.data == other.data

# Пример использования
if __name__ == "__main__":
    # Создание двух матриц
    matrix1 = Main([[1, 2, 3], [4, 5, 6]])
    matrix2 = Main([[6, 5, 4], [3, 2, 1]])

    # Сложение двух матриц
    print("Сложение матриц:")
    print(matrix1 + matrix2)

    # Сложение матрицы с числом
    print("\nСложение матрицы с числом 10:")
    print(matrix1 + 10)

    # Сравнение матриц
    matrix3 = Main([[1, 2, 3], [4, 5, 6]])
    print("\nСравнение matrix1 и matrix3:")
    print(matrix1 == matrix3)

    print("\nСравнение matrix1 и matrix2:")
    print(matrix1 == matrix2)

