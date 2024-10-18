text = "text2.2.txt"

try:
    with open(text, 'r', encoding='utf8') as file:
        symbols = file.read().lower()
        ab_cnt = symbols.count('ab')
        abcdefgh_cnt = symbols.count('abcdefgh')

        letters_to_cnt = ['a', 'b', 'c', 'd', 'e', 'f']
        letter_cnt = {letter: symbols.count(letter) for letter in letters_to_cnt}


        print(f"Количество 'ab': {ab_cnt}")

        if abcdefgh_cnt >= 1:
            print("Сочетание 'abcdefgh' найдено в файле.")
        else:
            print("Сочетание 'abcdefgh' не найдено в файле.")

        print("Число букв a, b, c, d, e, f:")
        for letter in letters_to_cnt:
            print(f"{letter} - {letter_cnt[letter]}")

except FileNotFoundError:
    print(f"файла нету '{text}'")
except PermissionError:
    print(f"нет прав '{text}'")
except Exception as e:
    print(f"случайная ошибка {e}")