from morse_code import MorseCode

text_from_user = input("Please input text here to be converted into morse code: ").upper()
word = MorseCode(text_from_user)
print(word)
word.play_morse_code()