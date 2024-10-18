text = "text2.1.txt"

try:
    with open(text, 'r', encoding='utf8') as file:
        symbols = file.read().lower()
        digits_cnt = 0
        letters_cnt = 0

        for symbol in symbols:
            if symbol.isdigit():
                digits_cnt += 1
            elif 'a' <= symbol <= 'z':
                letters_cnt += 1
        print(f"цифр - {digits_cnt}, букв - {letters_cnt}")

except FileNotFoundError:
    print(f"файла нету '{text}'")
except PermissionError:
    print(f"нет прав '{text}'")
except Exception as e:
    print(f"случайная ошибка {e}")