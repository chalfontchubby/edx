from time import sleep

dot_time = 0.2
dash_time = 0.7
error_time = 2
gap_time = 0.3
letter_gap_time = 0.5

#dictionary of letters to strings of dots and dashes in morse code
codes = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".-",
    "x": ".--.",
    "z": "--..",
    "*": "*", # Error tone
    " ": ""
}

class Led:
    def __init__(self):
        return

    def on(self):
        print("LED ON")

    def off(self):
        print("LED OFF")

    def dot(self):
        print("LED DOT")
        self.on()
        sleep(dot_time)
        self.off()
        sleep(gap_time)

    def dash(self):
        print("LED DASH")
        self.on()
        sleep(dash_time)
        self.off()
        sleep(gap_time)

    def error(self):
        print("Error")
        self.on()
        sleep(error_time)
        self.off()
        sleep(gap_time)


    def end_letter(self):
        print("end letter")
        sleep(letter_gap_time)

    def play_letter(self, l):
        players = {
            ".": self.dot,
            "-": self.dash,
            ",": self.end_letter,
            "*": self.error
        }

        code = codes.get(l.lower(), "*") + ","

        print(f"{l=} {code=}")
        for beep in code:
            players[beep]()

    def play_word(self, word):
        for letter in word:
            self.play_letter(letter)


led = Led()

led.play_word("Hello World")