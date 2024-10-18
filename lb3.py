text = "text3.txt"
output_file = 'new_data.txt'
try:
    with open(text, 'r', encoding='utf8') as file:
        data = file.readlines()

        oldest_bodyguard = None
        oldest_date = [10000, 13, 32]

    for line in data:
        parts = line.split(';')
        birth_date = list(map(int, parts[2].split(',')))
        birth_year, birth_month, birth_day = birth_date

        if (birth_year < oldest_date[0]) or \
                (birth_year == oldest_date[0] and birth_month < oldest_date[1]) or \
                (birth_year == oldest_date[0] and birth_month == oldest_date[1] and birth_day < oldest_date[2]):
            oldest_date = [birth_year, birth_month, birth_day]
            oldest_bodyguard = line.strip()
    if oldest_bodyguard:
        print(f"Старший телохранитель: {oldest_bodyguard}")

        try:
            with open(output_file, 'w', encoding='utf-8') as out_file:
                out_file.write(oldest_bodyguard)
            print(f"Результаты сохранены '{output_file}'")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        else:
            print("Данные некорректны.")


except FileNotFoundError:
    print(f"файла нету '{text}'")
except PermissionError:
    print(f"нет прав '{text}'")
except Exception as e:
    print(f"случайная ошибка {e}")


