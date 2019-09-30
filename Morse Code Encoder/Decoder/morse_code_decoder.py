morse_translated_to_english = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "...---...": "SOS",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0",
    ".-.-.-": ".",
    "--..--": ",",
    "..--..": "?",
    ".----.": "'",
    "-.-.--": "!",
    "-..-.": "/",
    "-.--.": "(",
    "-.--.-": ")",
    ".-...": "&",
    "---...": ":",
    "-.-.-.": ";",
    "-...-": "=",
    ".-.-.": "+",
    "-....-": "-",
    "..--.-": "_",
    ".-..-.": '"',
    "...-..-": "$",
    ".--.-.": "@",
}

english_translated_to_morse = dict()

for key, value in morse_translated_to_english.items():
    english_translated_to_morse[value] = key


def morse_code_to_english(incoming_morse_code):
    output = ""
    word = ""
    morse_code_list = incoming_morse_code.split(" ")
    i = 0

    for code in morse_code_list:
        i += 1
        if code != "" and len(morse_code_list) != i:
            word = word + morse_translated_to_english.get(code, code)
        elif len(morse_code_list) == i:
            word = word + morse_translated_to_english.get(code, code)
            output = output + " " + word
        else:
            output = f'{output} {word}'
            word = ""
        output = output.strip()
        output = output.replace("  ", " ")
    return output


def english_to_morse_code(incoming_english):
    output = ""
    letter = ""
    english_list = list(incoming_english.upper())
    i = 0
    for letters in english_list:
        i += 1
        if letters != "" and len(english_list) != i:
            letter = letter + " " + english_translated_to_morse.get(letters, letters)
        elif len(english_list) == i:
            letter = letter + " " + english_translated_to_morse.get(letters, letters)
            output = output + "  " + letter
        else:
            output = f'{output}  {letter}'
        output = output.strip()
        output = output.replace("   ", "  ")
    return output

