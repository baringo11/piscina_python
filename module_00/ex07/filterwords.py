import sys
import string
import re

def filter(text, n) :
    
    words = []
    for word in text.split() :
        i = 0
        for char in word :
            if char not in string.punctuation :
                i += 1
        word = re.sub(f"[{re.escape(string.punctuation)}]", "", word)
        if (i > n) :
            words.append(word)

    print(words)

if __name__ == "__main__" :
    if (len(sys.argv) != 3 or not (sys.argv[2].isdigit())) :
        print("Error, bad arguments")
    else :
        filter(sys.argv[1], int(sys.argv[2]))
