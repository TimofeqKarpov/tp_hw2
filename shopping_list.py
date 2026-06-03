from recipe import Recipe
from ingredient import Ingredient

class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe, portions):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным.")
        recipe_with_ratio = recipe.scale(portions)
        for ingredient in recipe_with_ratio.ingredients:
            self._items.append((ingredient, recipe_with_ratio.title))

    def remove_recipe(self, title):
        new_items = []
        for ingredient, recipe_title in self._items:
            if recipe_title != title:
                new_items.append((ingredient, recipe_title))
        self._items = new_items
    
    def get_list(self):
        totals = {}
        for ingredient, recipe_title in self._items:
            key = (ingredient.name, ingredient.unit)
            if key in totals:
                totals[key] += ingredient.quantity
            else:
                totals[key] = ingredient.quantity
        result = [Ingredient(name, quantity, unit) for (name, unit), quantity in totals.items()]
        return sorted(result, key=lambda i: i.name)
    
    def __add__(self, other):
        new_list = ShoppingList()
        for item in self._items:
            new_list._items.append(item)
        for item in other._items:
            new_list._items.append(item)
        return new_list