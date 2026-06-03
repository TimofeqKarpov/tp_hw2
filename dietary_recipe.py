from recipe import Recipe


class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients=[]):
        super().__init__(title)
        self.diet_type = diet_type
        for ingredient in ingredients:
            self.add_ingredient(ingredient)

    def scale(self, ratio):
        scale_recipe = super().scale(ratio)
        new_recipe = DietaryRecipe(self.title, self.diet_type)
        new_recipe.ingredients = scale_recipe.ingredients
        return new_recipe

    def __str__(self):
        return f"{self.diet_type} {super().__str__()}"