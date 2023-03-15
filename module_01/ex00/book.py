import datetime
from recipe import Recipe

class Book :
    def __init__(self, name) :
        self.name = name
        self.last_update = datetime
        self.creation_date = datetime
        self.recipes_list = {"entrante": [], "comida": [], "postre": []}

        if not isinstance(self.name, str):
            raise ValueError("name should be a string")
    
    def get_recipe_by_name(self, name) :
        """Imprime la receta con el nombre {name} y devuelve la instancia"""
        if not isinstance(name, str) :
            print("name should be a string")
            return
        for i in ["entrante", "comida", "postre"] :
            for recipe in self.recipes_list[i] :
                if recipe.name == name :
                    return recipe

    def get_recipes_by_types(self, recipe_type) :
        """Devuelve todas las recetas dado un recipe_type """
        recipes = []
        if not isinstance(recipe_type, str) or recipe_type not in ["entrante", "comida", "postre"]:
            print("recipe_type should be a string that is either 'entrante', 'comida', or 'postre'")
            return
        for recipe in self.recipes_list[recipe_type] :
            recipes.append(recipe)
        return recipes
    
    def add_recipe(self, recipe):
        """Añade una receta al libro y actualiza last_update"""
        if not isinstance(recipe, Recipe):
           print("recipe should be a Recipe instance")
           return 1
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime
        
        