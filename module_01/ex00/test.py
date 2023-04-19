from book import Book
from recipe import Recipe

if __name__ == "__main__" :
    book = Book("recetario")
    tourte = Recipe("tourte", 3, 23, ["tpr", "ter"], "", "dessert")
    pasta = Recipe("macarrones", 1, 10, ["macarrones", "tomate"], "", "lunch")
    carne = Recipe("solomillo", 4, 25, ["solomillo", "sal", "pimienta"], "", "lunch")

    book.add_recipe(tourte)
    book.add_recipe(pasta)
    book.add_recipe(carne)

    str_recipes = []
    print(book.creation_date)
    for recipe in book.get_recipes_by_types("lunch") :
        print(str(recipe) + "\n-------")



