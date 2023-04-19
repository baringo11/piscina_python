class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

        if not isinstance(name, str) or not bool(name):
            raise ValueError("name should be a not empty string")

        if not isinstance(cooking_lvl, int) or cooking_lvl not in range(1, 6):
            raise ValueError("cooking_lvl should be an integer between 1 and 5")

        if not isinstance(cooking_time, int) or cooking_time < 0:
            raise ValueError("cooking_time should be a positive integer")

        if not isinstance(ingredients, list) or not bool(ingredients) or not all(isinstance(ingredient, str) and bool(ingredient) for ingredient in ingredients):
            raise ValueError("ingredients should be a list of not empty strings")

        if not isinstance(description, str):
            raise ValueError("description should be a string(may be empty)")

        if not isinstance(recipe_type, str) or recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("recipe_type should be a string that is either 'starter', 'lunch', or 'dessert'")

    def __str__(self):
        """Return the string to print with the recipe info"""
        return f"Receta: {self.name}\nNivel de Cocina: {self.cooking_lvl}\nTiempo de Cocina: {self.cooking_time}\nIngredientes: {', '.join(self.ingredients)}\nDescripción: {self.description}\nTipo de Receta: {self.recipe_type}"
