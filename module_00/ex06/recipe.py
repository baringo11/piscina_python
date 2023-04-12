import readline

Ireceta = {
    "ingredients": [],
    "meal": "",
    "prep_time": 0
}

receta_1 = Ireceta.copy()
receta_1["ingredients"] = ["jamón", "pan", "queso", "tomate"]
receta_1["meal"] = "Almuerzo"
receta_1["prep_time"] = 10

receta_2 = Ireceta.copy()
receta_2["ingredients"] = ["harina", "azúcar", "huevos"]
receta_2["meal"] = "Postre"
receta_2["prep_time"] = 60

receta_3 = Ireceta.copy()
receta_3["ingredients"] = ["aguacate", "rúcula", "tomates", "espinacas"]
receta_3["meal"] = "Almuerzo"
receta_3["prep_time"] = 15

cookbook = {
    "Bocadillo": receta_1,
    "Tarta": receta_2,
    "Ensalada": receta_3
}

def print_recipe_names(cookbook):
    """ Imprime los nombres de todas las recetas en el cookbook. """

    print("Recetas disponibles:")
    for recipe_name in cookbook:
        print("- " + recipe_name)

def print_recipe_details(cookbook, recipe_name):
    """ Imprime los detalles de una receta específica en el cookbook. """
    if recipe_name in cookbook:
        print(f"\nDetalles de la receta '{recipe_name}':")
        recipe = cookbook[recipe_name]
        print("Ingredientes: ", ", ".join(recipe["ingredients"]))
        print("Tipo de comida: ", recipe["meal"])
        print("Tiempo de preparación: ", recipe["prep_time"], "minutos")
    else:
        print(f"No se encontró la receta '{recipe_name}' en el cookbook.")

def print_all_recipes(cookbook) :
    for i in cookbook :
        print_recipe_details(cookbook, i)

def delete_recipe(cookbook, recipe_name):
    """ Borra una receta específica del cookbook. """
    if recipe_name in cookbook:
        del cookbook[recipe_name]
        print(f"La receta '{recipe_name}' ha sido borrada del cookbook.")
    else:
        print(f"No se encontró la receta '{recipe_name}' en el cookbook.")

def add_recipe(cookbook):
    """ Añade una nueva receta al cookbook a partir de la entrada del usuario. """
    print("Nombre de la receta:")
    recipe_name = input()

    print("Lista de ingredientes: ")
    ingredients = []
    while True:
        linea = input()
        if linea:
            ingredients.append(linea)
        else:
            print()
            break

    print("Tipo de comida:")
    meal = input()

    print("Tiempo de preparación (en minutos):")
    try:
        prep_time = int(input())
    except:
        prep_time = 0
    recipe = {"ingredients": [ingredient for ingredient in ingredients],
              "meal": meal,
              "prep_time": prep_time}
    cookbook[recipe_name] = recipe
    print(f"La receta '{recipe_name}' ha sido añadida al cookbook.")


if __name__ == "__main__" :
    print("Welcome to the Python Cookbook !")
    
    functs = {
        1: add_recipe,
        2: delete_recipe,
        3: print_recipe_details,
        4: print_all_recipes,
    }

    print("List of available option:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n")
    while True :
        print("Please select an option:")
        option = input()
        if option.isdigit() and int(option) in functs :
            if len(cookbook) == 0 and int(option) != 1:
                print("Cookbook vacío, ingresa una receta")
            elif (int(option) == 2 or int(option) == 3) :
                print("Please enter a recipe name:")
                recipe = input()
                functs[int(option)](cookbook, recipe)
            else :
                functs[int(option)](cookbook)
        elif option.isdigit() and int(option) == 5 :
            print("Cookbook closed. Goodbye !")
            exit(0)
        else :
            print("Sorry, this option does not exist.")
            print("List of available option:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n")
        print("\n******************\n")
        
            

