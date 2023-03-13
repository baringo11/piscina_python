import sys
import string

def text_analyzer(text = None) :
    """This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
    if (text == None) :
        print('What is the text to analyze?')
        text = input()
    if (type(text) == str) :
        upper, lower, puntMarks, spaces = 0,0,0,0
        for char in text :
            if (char.isalpha() and char.isupper()) :
                upper += 1
            if (char.isalpha() and char.islower()) :
                lower += 1
            if (char in string.punctuation) :
                puntMarks += 1
            if (char in [' ', '\t', '\r', '\n', '\v', '\f']) :
                spaces += 1
        print('The text contains ' + str(len(text)) + ' character(s):')
        print ('- ' + str(upper) + ' upper letter(s)')
        print ('- ' + str(lower) + ' lower letter(s)')
        print ('- ' + str(puntMarks) + ' punctuation mark(s)')
        print ('- ' + str(spaces) + ' space(s)')
    else :
        print('AssertionError: argument is not a string')

if __name__ == "__main__" :
    if (len(sys.argv) > 2) :
        print('AssertionError: more than one argument are provided')
    elif (len(sys.argv) == 2):
        text_analyzer(sys.argv[1])
    else :
        text_analyzer()