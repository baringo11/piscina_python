class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = ""):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

        if not isinstance(self.name, str):
            raise ValueError("name should be a string")
        
        if not isinstance(self.cooking_lvl, int) or self.cooking_lvl not in range(1, 6):
            raise ValueError("cooking_lvl should be an integer between 1 and 5")
        
        if not isinstance(self.cooking_time, int) or self.cooking_time < 0:
            raise ValueError("cooking_time should be a positive integer")
        
        if not isinstance(self.ingredients, list) or not all(isinstance(ingredient, str) for ingredient in self.ingredients):
            raise ValueError("ingredients should be a list of strings")
        
        if not isinstance(self.description, str):
            raise ValueError("description should be a string")
        
        if not isinstance(self.recipe_type, str) or self.recipe_type not in ["entrante", "comida", "postre"]:
            raise ValueError("recipe_type should be a string that is either 'entrante', 'comida', or 'postre'")

    
    def __str__(self):
        """Return the string to print with the recipe info"""
        return f"Receta: {self.name}\nNivel de Cocina: {self.cooking_lvl}\nTiempo de Cocina: {self.cooking_time}\nIngredientes: {', '.join(self.ingredients)}\nDescripción: {self.description}\nTipo de Receta: {self.recipe_type}"
