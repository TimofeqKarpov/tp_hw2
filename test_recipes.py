import pytest

from ingredient import Ingredient
from recipe import Recipe
from dietary_recipe import DietaryRecipe
from shopping_list import ShoppingList

def test_ingredient_init():
    ing = Ingredient("Мука", 500, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit == "г"

def test_ingredient_str():
    ing = Ingredient("Мука", 500, "г")
    assert str(ing) == "Мука: 500.0 г"

def test_ingredient_eq_same():
    ing1 = Ingredient("Мука", 100, "г")
    ing2 = Ingredient("Мука", 500, "г")
    assert ing1 == ing2

def test_ingredient_eq_diff_name():
    ing1 = Ingredient("Мука", 500, "г")
    ing2 = Ingredient("Сахар", 500, "г")
    assert ing1 != ing2

def test_ingredient_eq_diff_unit():
    ing1 = Ingredient("Мука", 500, "г")
    ing2 = Ingredient("Мука", 500, "кг")
    assert ing1 != ing2




def test_recipe_init():
    recipe = Recipe("Пицца")
    assert recipe.title == "Пицца"
    assert recipe.ingredients == []

def test_recipe_add_new_ingredient():
    recipe = Recipe("Пицца")
    ingridient = Ingredient("Мука", 500, "г")
    recipe.add_ingredient(ingridient)
    assert len(recipe) == 1

def test_recipe_add_duplicate_ingredient():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    recipe.add_ingredient(Ingredient("Мука", 200, "г"))
    assert len(recipe) == 1
    assert recipe.ingredients[0].quantity == 700.0

def test_recipe_scale_returns_new():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    scaled = recipe.scale(2)
    assert scaled is not recipe

def test_recipe_scale_quantity():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    scaled = recipe.scale(2)
    assert scaled.ingredients[0].quantity == 1000.0

def test_recipe_scale_invalid():
    recipe = Recipe("Пицца")
    with pytest.raises(ValueError):
        recipe.scale(-1)

def test_recipe_len():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    recipe.add_ingredient(Ingredient("Мука", 200, "г"))
    recipe.add_ingredient(Ingredient("Соль", 10, "г"))
    assert len(recipe) == 2







def test_shopping_add_recipe():
    sl = ShoppingList()
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    sl.add_recipe(recipe, 2)
    assert len(sl._items) == 1

def test_shopping_add_recipe_invalid_portions():
    sl = ShoppingList()
    recipe = Recipe("Пицца")
    with pytest.raises(ValueError):
        sl.add_recipe(recipe, 0)

def test_shopping_remove_recipe():
    sl = ShoppingList()
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    sl.add_recipe(recipe, 1)
    sl.remove_recipe("Пицца")
    sl.remove_recipe("Пеперонни")  # Два в одном
    assert sl._items == []

def test_shopping_get_list_sums():
    sl = ShoppingList()
    r1 = Recipe("Пицца")
    r1.add_ingredient(Ingredient("Мука", 500, "г"))
    r2 = Recipe("Хлеб")
    r2.add_ingredient(Ingredient("Мука", 300, "г"))
    sl.add_recipe(r1, 1)
    sl.add_recipe(r2, 1)
    result = sl.get_list()
    assert result[0].quantity == 800.0

def test_shopping_get_list_sorted():
    sl = ShoppingList()
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Соль", 10, "г"))
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    sl.add_recipe(recipe, 1)
    result = sl.get_list()
    assert result[0].name == "Мука"
    assert result[1].name == "Соль"

def test_shopping_add_two_lists():
    sl1 = ShoppingList()
    sl2 = ShoppingList()
    r1 = Recipe("Пицца")
    r1.add_ingredient(Ingredient("Мука", 500, "г"))
    r2 = Recipe("Хлеб")
    r2.add_ingredient(Ingredient("Соль", 10, "г"))
    sl1.add_recipe(r1, 1)
    sl2.add_recipe(r2, 1)
    sl3 = sl1 + sl2
    assert len(sl3._items) == 2
    assert len(sl1._items) == 1
    assert len(sl2._items) == 1              #Еще одно два в одном