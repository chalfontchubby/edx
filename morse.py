from time import sleep
try :
    from gpiozero import LED
except ImportError:
    # Dummy LED class to allow testing on non-raspberry pi
    class LED:
        def __init__(self, pin):
            print(f"Create led on {pin=}")

        def on(self):
            print(f"LED on")

        def off(self):
            print(f"LED off")

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

class OutputDevice:
    def __init__(self, pin):
        self.led =  LED(pin)
        return

    def dot(self):
        print("LED DOT")
        self.led.on()
        sleep(dot_time)
        self.led.off()
        sleep(gap_time)

    def dash(self):
        print("LED DASH")
        self.led.on()
        sleep(dash_time)
        self.led.off()
        sleep(gap_time)

    def error(self):
        print("Error")
        self.led.on()
        sleep(error_time)
        self.led.off()
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


led = OutputDevice(10)

led.play_word("Hello World")