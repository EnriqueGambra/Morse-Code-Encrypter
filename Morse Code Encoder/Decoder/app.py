from morse_code_decoder import *


def run():

    while True:
        option = int(input("To quit anytime, type in 0. Choose if you'd like to: " +
                   "\n1. Translate from morse code to English." +
                   "\n2. Translate from English to morse code. "))
        if option == 0:
            break
        elif option == 1:
            word_in_morse = input("Enter the morse code you'd like to translate.")
            if word_in_morse.isalnum():
                print("You did not enter in morse code.")
                break
            print(morse_code_to_english(word_in_morse))
        elif option == 2:
            word_in_english = input("Enter the word in English that you'd like to translate.")
            print(english_to_morse_code(word_in_english))


if __name__ == '__main__':
    run()
