from datetime import datetime
from recipe import Recipe

class Book :
    def __init__(self, name) :
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

        if not isinstance(self.name, str) or not bool(name):
            raise ValueError("name should be a not empty string")

    def get_recipe_by_name(self, name) :
        """Imprime la receta con el nombre {name} y devuelve la instancia"""
        if not isinstance(name, str) :
            print("name should be a string")
            return
        for i in ["starter", "lunch", "dessert"] :
            for recipe in self.recipes_list[i] :
                if recipe.name == name :
                    print(recipe)
                    return recipe
        print(f"Recipe {name} not found")
        return None

    def get_recipes_by_types(self, recipe_type) :
        """Devuelve todas las recetas dado un recipe_type """
        recipes = []
        if not isinstance(recipe_type, str) or recipe_type not in ["starter", "lunch", "dessert"]:
            print("recipe_type should be a string that is either 'starter', 'lunch', or 'dessert'")
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
        self.last_update = datetime.now()
        
        