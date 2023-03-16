import random

def generator(text, sep=" ", option=None):
    """Divide el texto de acuerdo al valor de sep y producirá las sub-strings. option especifica si una acción se realizará sobre las sub-strings antes de ser producidas."""
    if not isinstance(text, str) :
        print("ERROR")
        return 1
    if option != None :
        if not isinstance(option, str) or option not in ["shuffle", "unique", "ordered"] :
            print("ERROR")
            return 1

    words = text.split(sep)
    if option == "shuffle":
        n = len(words)
        for i in range(n-1, 0, -1):
            j = random.randint(0, i)
            words[i], words[j] = words[j], words[i]
    elif option == "unique":
        words = list(set(words))
    elif option == "ordered":
        words.sort()
    for word in words:
        yield word

if __name__ == "__main__" :
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, sep=" "):
        print(word)
    print("\n--------------\n")
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    print("\n--------------\n")
    for word in generator(text, sep=" ", option="ordered"):
        print(word)
    print("\n--------------\n")
    for word in generator("Lorem Ipsum Lorem Ipsum", sep=" ", option="unique"):
        print(word)
    print("\n--------------\n")
    for word in generator(4, sep=" ", option="unique"):
        print(word)