import csv
import random

# Функция для генерации данных и записи в файл
def generate_data(filename, num_records):
    doctors = ["Иванов Иван Иванович", "Петров Петр Петрович", "Сидоров Сидор Сидорович"]
    specialties = ["Терапевт", "Хирург", "Стоматолог"]
    patients = ["Смирнов", "Кузнецов", "Попов", "Соколов", "Михайлов"]
    names = ["Алексей", "Максим", "Иван", "Евгений", "Дмитрий"]
    patronymics = ["Иванович", "Петрович", "Сергеевич", "Александрович", "Михайлович"]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["ФИО врача", "Специальность", "Фамилия пациента", "Имя пациента",
                         "Отчество пациента", "Дата рождения пациента", "Дата приема", "Стоимость приема"])
        for _ in range(num_records):
            doctor = random.choice(doctors)
            specialty = random.choice(specialties)
            patient = random.choice(patients)
            name = random.choice(names)
            patronymic = random.choice(patronymics)
            birth_date = f"{random.randint(1950, 2010)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
            appointment_date = f"{random.randint(2020, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
            cost = random.randint(500, 5000)
            writer.writerow([doctor, specialty, patient, name, patronymic, birth_date, appointment_date, cost])

# Функция для чтения данных и анализа расходов пациентов
def analyze_data(input_file, output_file, year):
    patient_expenses = {}

    with open(input_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            appointment_date = row["Дата приема"]
            appointment_year = int(appointment_date.split("-")[0])
            if appointment_year == year:
                patient_fullname = f"{row['Фамилия пациента']} {row['Имя пациента']} {row['Отчество пациента']}"
                cost = int(row["Стоимость приема"])
                if patient_fullname in patient_expenses:
                    patient_expenses[patient_fullname] += cost
                else:
                    patient_expenses[patient_fullname] = cost

    # Записываем результат в новый файл
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ФИО пациента", "Общая сумма расходов"])
        for patient, total_cost in patient_expenses.items():
            writer.writerow([patient, total_cost])

    # Выводим результат на экран
    print(f"Расходы пациентов за {year} год:")
    for patient, total_cost in patient_expenses.items():
        print(f"{patient}: {total_cost} руб.")

# Основная программа
if __name__ == "__main__":
    input_filename = "clinic_data.csv"
    output_filename = "patient_expenses.csv"
    num_records = 10000
    year_to_analyze = 2023

    # Генерация данных
    generate_data(input_filename, num_records)

    # Анализ данных
    analyze_data(input_filename, output_filename, year_to_analyze)
