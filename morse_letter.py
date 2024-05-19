import time
import winsound

frequency = 500 # In Hertz, according to the official morse code frequency
dotLength = 60 # milliseconds or 1 second according to official morse code
dashLength = dotLength * 3 # or 3 seconds according official morse code
pauseWords = dotLength * 7

# Dictionary representing the morse code chart
# Got from GeeksForGeeks
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': ' '}


class MorseCodeWord:
    def __init__(self, word):
        self.plain_text_word = word
        self.morse_word = self.convert_to_morse(word)

    def convert_to_morse(self, word):
        morse_word = ""
        for letter in word:
            try:
                morse_word += MORSE_CODE_DICT[letter]
                morse_word += " "
            except KeyError:
                morse_word += " "

        return morse_word

    def get_word(self):
        return self.plain_text_word

    def get_morse(self):
        return self.morse_word

    # TODO: Convert string to a playable, morse code audio
    def play(self):
        for letter in self.morse_word:
            if letter == '.':
                winsound.Beep(frequency, dotLength)
            elif letter == '-':
                winsound.Beep(frequency, dashLength)
            else:
                time.sleep(1)

        time.sleep(3)