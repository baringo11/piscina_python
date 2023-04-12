import sys
import string
import re

def filter(text, n) :
    
    words = []
    punct_chars = f"[{re.escape(string.punctuation)}]"
    for word in text.split() :
        i = 0
        for char in word :
            if char not in string.punctuation :
                i += 1
        word = re.sub(punct_chars, "", word)
        if (i > n) :
            words.append(word)

    print(words)

if __name__ == "__main__" :
    if (len(sys.argv) != 3 or not(not sys.argv[1].isdigit() and (sys.argv[2].isdigit()))) :
        print("Error, bad arguments")
    else :
        filter(sys.argv[1], int(sys.argv[2]))
