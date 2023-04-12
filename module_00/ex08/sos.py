import sys

MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}

def encode_morse(text):
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE:
            morse_code.append(MORSE_CODE[char])
    return ' '.join(morse_code)


if __name__ == "__main__" :
    argv = []
    if len(sys.argv) < 2 :
        exit(0)
    for argument in sys.argv[1:] :
        argument = argument.split()
        for a in argument :
            argv.append(a)
    for a in argv :
        if a not in MORSE_CODE:
            print("Error, only alphanumeric chars")
            exit(1)
    print(encode_morse(' '.join(argv)))

   