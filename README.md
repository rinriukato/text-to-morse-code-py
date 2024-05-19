# Text To Morse Code Module
A python module that takes any string input, such as indivdual words or a sentence, and converts it into American Morse Code.

![American Morse Code Chart](https://m.media-amazon.com/images/I/61fSbU2U1NL._AC_UF894,1000_QL80_.jpg)

## How to use:
Create a MorseCode object by calling its constructor and providing it a string of any length

```
some_text = "Hello World!"
morse_code = MorseCode(some_text)
```

### Printing
You can print the Morse code by passing it into a print statement and the object will return a string like so:
```
print(morse_code)
```

### .play_morse_code()
You can then play the Morse code by calling the 'play_morse_code" method. Note, that this module uses winsounds, so you may need to have your system sounds volume up to be able to hear it!
```
morse_code.play_morse_code()
```
