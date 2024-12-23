class QuoteSystem:
    def __init__(self):
        self.quotes = []

    def add_quote(self, source, text, date):
        quote = {
            "source": source,
            "text": text,
            "date": date
        }
        self.quotes.append(quote)
        print("Цитата успешно добавлена!")

    def input_quote(self):
        source = input("Введите источник (книга/автор): ")
        text = input("Введите текст цитаты: ")
        date = input("Введите дату записи (в формате YYYY-MM-DD): ")
        self.add_quote(source, text, date)

    def search_quote(self, keyword):
        results = []
        for quote in self.quotes:
            source_lower = quote["source"].lower()
            text_lower = quote["text"].lower()
            keyword_lower = keyword.lower()

            if keyword_lower in source_lower or keyword_lower in text_lower:
                results.append(quote)

        self.display_search_results(results)

    def display_search_results(self, results):
        if results:
            print(f"Найдено {len(results)} цитат(ы):")
            for i, quote in enumerate(results, 1):
                self.display_quote(quote, i)
        else:
            print("Цитаты по данному запросу не найдены.\n")

    def display_quote(self, quote, index):
        print(f"{index}. \"{quote['text']}\" — {quote['source']} ({quote['date']})\n")

    def display_quotes(self, sort_by_date=False):
        if not self.quotes:
            print("В системе нет цитат.\n")
            return

        sorted_quotes = sorted(self.quotes, key=lambda q: q["date"]) if sort_by_date else self.quotes

        print("Список всех цитат:\n")
        for i, quote in enumerate(sorted_quotes, 1):
            self.display_quote(quote, i)


class Menu:
    def __init__(self, system):
        self.system = system

    def display_menu(self):
        while True:
            print("Меню:")
            print("1) Добавить новую цитату")
            print("2) Найти цитату")
            print("3) Показать все цитаты")
            print("4) Показать все цитаты (сортировка по дате)")
            print("5) Закрыть программу")

            choice = input("Выберите действие (1-5): ")

            if choice == "1":
                self.system.input_quote()
            elif choice == "2":
                keyword = input("Введите ключевое слово для поиска: ")
                self.system.search_quote(keyword)
            elif choice == "3":
                self.system.display_quotes()
            elif choice == "4":
                self.system.display_quotes(sort_by_date=True)
            elif choice == "5":
                print("Удачи! >_<")
                break
            else:
                print("Некорректный ввод. Попробуйте снова.\n")


if __name__ == "__main__":
    quote_system = QuoteSystem()
    menu = Menu(quote_system)
    menu.display_menu()
