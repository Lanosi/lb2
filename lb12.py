import tkinter as tk
from math import cos

class FunctionCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Вычисление функции f(a)")

        # Метка для ввода значения a
        self.label_a = tk.Label(root, text="Введите значение a:")
        self.label_a.pack()

        # Поле для ввода значения a
        self.entry_a = tk.Entry(root)
        self.entry_a.pack()

        # Кнопка для вычисления
        self.calculate_button = tk.Button(root, text="Вычислить", command=self.calculate)
        self.calculate_button.pack()

        # Поле для вывода результата
        self.result_label = tk.Label(root, text="Результат:")
        self.result_label.pack()
        self.result_entry = tk.Entry(root, state="readonly", justify="center")
        self.result_entry.pack()

    def calculate(self):
        try:
            # Получение значения a
            a = float(self.entry_a.get())

            # Вычисление функции f(a)
            if a > 2:
                result = a**4 - 13
            elif 0 < a <= 2:
                result = cos(a)
            else:
                result = a - 18

            # Вывод результата
            self.result_entry.config(state="normal")
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, f"{result:.5f}")
            self.result_entry.config(state="readonly")

        except ValueError:
            self.result_entry.config(state="normal")
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, "Некорректный ввод")
            self.result_entry.config(state="readonly")


if __name__ == "__main__":
    root = tk.Tk()
    app = FunctionCalculator(root)
    root.mainloop()
