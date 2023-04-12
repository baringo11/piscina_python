# Put this at the top of your kata00.py file
kata = (19,42,21)

if kata :
    cadena = "{}" + ", {}" * (len(kata) - 1)
    print("the {} numbers are: ".format(len(kata)) + cadena.format(*kata))
