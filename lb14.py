import sqlite3

def create_database():
    """Создание базы данных и таблиц."""
    conn = sqlite3.connect("cinema.db")
    cursor = conn.cursor()

    # Создаем таблицу жанров
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Жанры (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            название TEXT NOT NULL
        );
    """)

    # Создаем таблицу фильмов
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Фильмы (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            название TEXT NOT NULL,
            жанр_id INTEGER NOT NULL,
            FOREIGN KEY (жанр_id) REFERENCES Жанры (id)
        );
    """)

    # Создаем таблицу билетов
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Билеты (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            фильм_id INTEGER NOT NULL,
            цена REAL NOT NULL,
            FOREIGN KEY (фильм_id) REFERENCES Фильмы (id)
        );
    """)

    conn.commit()
    conn.close()


def insert_data():
    """Вставка тестовых данных в таблицы."""
    conn = sqlite3.connect("cinema.db")
    cursor = conn.cursor()

    # Добавляем жанры
    genres = [("Ужасы",), ("Боевик",), ("Комедия",), ("Драма",)]
    cursor.executemany("INSERT INTO Жанры (название) VALUES (?);", genres)

    # Добавляем фильмы
    films = [
        ("Оно", 1),  # Ужасы
        ("Дедпул", 2),  # Боевик
        ("Один дома", 3),  # Комедия
        ("Еретик", 4)  # Драма
    ]
    cursor.executemany("INSERT INTO Фильмы (название, жанр_id) VALUES (?, ?);", films)

    # Добавляем билеты
    tickets = [
        (1, 500), (1, 600),  # Билеты на "Оно"
        (2, 400), (2, 450),  # Билеты на "Дедпул"
        (3, 800),            # Билет на "Один дома"
        (4, 300), (4, 350)   # Билеты на "Еретик"
    ]
    cursor.executemany("INSERT INTO Билеты (фильм_id, цена) VALUES (?, ?);", tickets)

    conn.commit()
    conn.close()


def query_movies_with_genres():
    """Получить список фильмов с их жанрами."""
    conn = sqlite3.connect("cinema.db")
    cursor = conn.cursor()

    query = """
        SELECT Фильмы.название, Жанры.название
        FROM Фильмы
        JOIN Жанры ON Фильмы.жанр_id = Жанры.id;
    """
    cursor.execute(query)
    results = cursor.fetchall()

    print("Список фильмов с их жанрами:")
    for row in results:
        print(f"Фильм: {row[0]}, Жанр: {row[1]}")

    conn.close()


def query_tickets_by_genre(genre_name):
    """Найти билеты на фильмы определенного жанра."""
    conn = sqlite3.connect("cinema.db")
    cursor = conn.cursor()

    query = """
        SELECT Билеты.id, Билеты.цена
        FROM Билеты
        JOIN Фильмы ON Билеты.фильм_id = Фильмы.id
        JOIN Жанры ON Фильмы.жанр_id = Жанры.id
        WHERE Жанры.название = ?;
    """
    cursor.execute(query, (genre_name,))
    results = cursor.fetchall()

    print(f"Билеты на фильмы жанра '{genre_name}':")
    for row in results:
        print(f"Билет ID: {row[0]}, Цена: {row[1]}")

    conn.close()


def query_average_ticket_price():
    """Вывести среднюю цену билетов для каждого фильма."""
    conn = sqlite3.connect("cinema.db")
    cursor = conn.cursor()

    query = """
        SELECT Фильмы.название, AVG(Билеты.цена)
        FROM Билеты
        JOIN Фильмы ON Билеты.фильм_id = Фильмы.id
        GROUP BY Фильмы.id;
    """
    cursor.execute(query)
    results = cursor.fetchall()

    print("Средняя цена билетов для каждого фильма:")
    for row in results:
        print(f"Фильм: {row[0]}, Средняя цена: {row[1]:.2f}")

    conn.close()


if __name__ == "__main__":
    create_database()
    insert_data()

    print("\nЗапрос 1:")
    query_movies_with_genres()

    print("\nЗапрос 2:")
    query_tickets_by_genre("Ужасы")

    print("\nЗапрос 3:")
    query_average_ticket_price()
