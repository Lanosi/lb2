class Recipe:
    def __init__(self, recipe_type, name, ingredients, instructions):
        self.recipe_type = recipe_type
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        ingredients_str = ", ".join(self.ingredients) if self.ingredients else "Нет ингредиентов"
        return (f"Название рецепта: {self.name}\n"
                f"Тип: {self.recipe_type}\n"
                f"Ингредиенты: {ingredients_str}\n"
                f"Инструкция: {self.instructions}")

    def add_ingredient(self, ingredient):
        if ingredient not in self.ingredients:
            self.ingredients.append(ingredient)
            print(f"Вы добавили '{ingredient}'!")
        else:
            print(f"Этот '{ingredient}' уже есть в рецепте.")

    def delete_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
            print(f"Ингредиент '{ingredient}' удален.")
        else:
            print(f"'{ingredient}' отсутсвует в рецепте.")


recipe = Recipe("Горячее", "Пюре с биточками", ["картошка", "молоко","вода", "мясо"], "Приготовить сначала пюре потом биточки :)")

print(recipe)
recipe.add_ingredient("яйца")
recipe.delete_ingredient("молоко")

