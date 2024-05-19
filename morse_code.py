from morse_letter import MorseCodeWord

class MorseCode:
    """
    Takes in any text input and turns it into morse code
    """
    def __init__(self, sentence):
        self.plain_text_list = sentence.split(" ")
        self.morse_code = self.convert_to_morse(self.plain_text_list)

    def __str__(self):
        string = ""
        for morse_letter in self.morse_code:
            string += morse_letter.get_morse()
        return string

    def convert_to_morse(self, plain_text_list):
        return [MorseCodeWord(text) for text in plain_text_list]

    def play_morse_code(self):
        for morse_letter in self.morse_code:
            morse_letter.play()
