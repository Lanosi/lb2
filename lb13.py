import sqlite3
import csv


def create_database_from_csv(csv_file, db_file, table_name):
    # Создание бд из csv
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Получаем заголовки из CSV-файла
        columns = ", ".join([f'"{header}" TEXT' for header in headers])  # SQL-колонки

        # Создаём базу данных и таблицу
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});")

        # Заполняем таблицу данными из CSV
        for row in reader:
            placeholders = ", ".join(["?"] * len(row))
            cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders});", row)

        conn.commit()
        conn.close()
        print(f"Данные из {csv_file} успешно записаны в базу данных {db_file} в таблицу {table_name}.")


def query_and_save_results(db_file, table_name, output_file, year):
    """Выполняет запрос к базе данных и сохраняет результаты в CSV-файл."""
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # SQL-запрос для подсчёта, сколько каждый пациент потратил на приёмы в заданном году
    query = f"""
    SELECT 
        "Фамилия пациента", 
        "Имя пациента", 
        "Отчество пациента", 
        SUM(CAST("Стоимость приема" AS REAL)) AS "Итоговая стоимость"
    FROM {table_name}
    WHERE "Дата приема" LIKE '{year}%'
    GROUP BY "Фамилия пациента", "Имя пациента", "Отчество пациента";
    """

    cursor.execute(query)
    results = cursor.fetchall()

    # Записываем результаты в CSV-файл
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Фамилия пациента", "Имя пациента", "Отчество пациента", "Итоговая стоимость"])
        writer.writerows(results)

    conn.close()
    print(f"Результаты сохранены в файл {output_file}.")


if __name__ == "__main__":
    # Укажите файлы
    input_csv = "clinic_data.csv"  # Исходный CSV-файл из ЛР5
    database_file = "clinic.db"  # SQLite база данных
    table_name = "ClinicData"  # Название таблицы в базе данных
    output_csv = "patient_costs.csv"  # CSV для сохранения результатов
    target_year = "2023"  # Заданный год

    # Выполняем шаги
    create_database_from_csv(input_csv, database_file, table_name)
    query_and_save_results(database_file, table_name, output_csv, target_year)
