from ingredient import Ingredient


class Recipe:
    def __init__(self, title):
        self.title = title
        self.ingredients = []

    def add_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients[self.ingredients.index(ingredient)].quantity += ingredient.quantity
        else:
            self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0

    def scale(self, ratio):
        if not Recipe.is_valid_ratio(ratio):
            raise ValueError("Количество рационов должно быть положительным.")
        
        new_recipe = Recipe(self.title)
        
        for ingredient in self.ingredients:
            new_recipe.add_ingredient(Ingredient(ingredient.name, ingredient.quantity * ratio, ingredient.unit))
        return new_recipe

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        ingredients_str = "\n".join(str(i) for i in self.ingredients)
        return f"Название: {self.title}\nИнгредиенты:\n{ingredients_str}"
