from book import Book
from recipe import Recipe

if __name__ == "__main__" :
    book = Book("recetario")
    tourte = Recipe("tourte", 3, 23, ["tpr", "ter"], "postre")
    pasta = Recipe("macarrones", 1, 10, ["macarrones", "tomate"], "comida")
    carne = Recipe("solomillo", 4, 25, ["solomillo", "sal", "pimienta"], "comida")
  
    book.add_recipe(tourte)
    book.add_recipe(pasta)
    book.add_recipe(carne)

    str_recipes = []
    for recipe in book.get_recipes_by_types("comida") :
        print(str(recipe) + "\n-------\n")



