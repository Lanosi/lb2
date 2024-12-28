import tkinter as tk
from tkinter import messagebox

class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)

    def __str__(self):
        return (f"Название рецепта: {self.name}\n"
                f"Ингредиенты: {', '.join(self.ingredients)}\n"
                f"Инструкция: {self.instructions}")

class RecipeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Управление рецептами")

        self.recipes = []

        # Виджеты
        self.name_label = tk.Label(root, text="Название рецепта:")
        self.name_label.grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.grid(row=0, column=1, pady=5)

        self.ingredients_label = tk.Label(root, text="Ингредиенты (через запятую):")
        self.ingredients_label.grid(row=1, column=0, sticky="w")
        self.ingredients_entry = tk.Entry(root, width=30)
        self.ingredients_entry.grid(row=1, column=1, pady=5)

        self.instructions_label = tk.Label(root, text="Инструкция:")
        self.instructions_label.grid(row=2, column=0, sticky="w")
        self.instructions_entry = tk.Entry(root, width=30)
        self.instructions_entry.grid(row=2, column=1, pady=5)

        self.add_button = tk.Button(root, text="Добавить рецепт", command=self.add_recipe)
        self.add_button.grid(row=3, column=0, pady=10)

        self.view_button = tk.Button(root, text="Просмотреть рецепты", command=self.view_recipes)
        self.view_button.grid(row=3, column=1, pady=10)

        self.delete_button = tk.Button(root, text="Удалить рецепт", command=self.delete_recipe)
        self.delete_button.grid(row=4, column=0, pady=10)

        self.recipe_list_label = tk.Label(root, text="Список рецептов:")
        self.recipe_list_label.grid(row=5, column=0, sticky="nw")

        self.recipe_listbox = tk.Listbox(root, width=50, height=10)
        self.recipe_listbox.grid(row=5, column=1, pady=5)

    def add_recipe(self):
        name = self.name_entry.get().strip()
        ingredients = [ing.strip() for ing in self.ingredients_entry.get().split(',')]
        instructions = self.instructions_entry.get().strip()

        if not name or not ingredients or not instructions:
            messagebox.showerror("Ошибка", "Все поля должны быть заполнены!")
            return

        recipe = Recipe(name, ingredients, instructions)
        self.recipes.append(recipe)
        self.recipe_listbox.insert(tk.END, recipe.name)
        messagebox.showinfo("Успех", "Рецепт добавлен!")
        self.clear_fields()

    def view_recipes(self):
        selected_index = self.recipe_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Ошибка", "Выберите рецепт для просмотра.")
            return

        selected_recipe = self.recipes[selected_index[0]]
        messagebox.showinfo("Рецепт", str(selected_recipe))

    def delete_recipe(self):
        selected_index = self.recipe_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Ошибка", "Выберите рецепт для удаления.")
            return

        self.recipes.pop(selected_index[0])
        self.recipe_listbox.delete(selected_index)
        messagebox.showinfo("Успех", "Рецепт удален!")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.ingredients_entry.delete(0, tk.END)
        self.instructions_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeApp(root)
    root.mainloop()
