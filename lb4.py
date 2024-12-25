def write_matrix_to_file(file_name, matrix):
    try:
        with open(file_name, 'w') as file:
            for row in matrix:
                file.write(" ".join(map(str, row)) + "\n")
        print(f"Матрица успешно записана в файл '{file_name}'.")
    except Exception as e:
        print(f"Ошибка при записи матрицы: {e}")


if __name__ == "__main__":
    matrix_A = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
    ]
    write_matrix_to_file("matrix_A.txt", matrix_A)

def read_matrix_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            matrix = [list(map(int, line.split())) for line in file]
        return matrix
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None


def swap_columns(matrix, col1, col5):
    if not matrix or col1 >= len(matrix[0]) or col5 >= len(matrix[0]):
        print("Некорректные индексы столбцов или пустая матрица.")
        return matrix

    for row in matrix:
        row[col1], row[col5] = row[col5], row[col1]
    return matrix


def write_result_to_file(file_name, matrix):
    try:
        with open(file_name, 'w') as file:
            for row in matrix:
                file.write(" ".join(map(str, row)) + "\n")
        print(f"Результат успешно записан в файл '{file_name}'.")
    except Exception as e:
        print(f"Ошибка при записи результата: {e}")


if __name__ == "__main__":
    input_file = "matrix_A.txt"
    output_file = "matrix_result.txt"

    # Считывание матрицы из файла
    matrix = read_matrix_from_file(input_file)
    if matrix:
        print("Исходная матрица:")
        for row in matrix:
            print(row)

        # Замена 1-го и 5-го столбцов
        result_matrix = swap_columns(matrix, 0, 4)

        print("\nОбработанная матрица:")
        for row in result_matrix:
            print(row)

        # Запись результата в файл
        write_result_to_file(output_file, result_matrix)
