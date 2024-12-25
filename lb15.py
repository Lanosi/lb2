def process_csv(input_file):
    # Чтение CSV-файла
    with open(input_file, "r") as file:
        for line in file:
            # Преобразуем строку в список чисел
            numbers = list(map(int, line.strip().split(";")))

            # Условие 1: В строке есть два числа, каждое из которых повторяется дважды
            unique_counts = {num: numbers.count(num) for num in set(numbers)}
            double_repeats = [k for k, v in unique_counts.items() if v == 2]

            # Условие 2: Максимальное число строки не повторяется
            max_num = max(numbers)
            max_condition = numbers.count(max_num) == 1

            # Если оба условия выполнены, выводим строку и её сумму
            if len(double_repeats) == 2 and max_condition:
                print(f"Строка: {numbers}")
                print(f"Сумма чисел: {sum(numbers)}")
                break  # Выходим после обработки первой подходящей строки

# Входной CSV-файл
input_csv = "24.csv"  # путь к CSV-файлу

process_csv(input_csv)
