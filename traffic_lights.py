from time import sleep
try :
    from gpiozero import LED
except ImportError:
    # Dummy LED class to allow testing on non-raspberry pi
    class LED:
        def __init__(self, pin):
            print(f"Create led on {pin=}")
            self.pin = pin

        def on(self):
            print(f"LED {self.pin} on")

        def off(self):
            print(f"LED {self.pin} off")


lights = {
    "red": LED(10),
    "amber": LED(9),
    "green": LED(11),
}

states= {"stop": ["red"],
         "prepare": ["red", "amber"],
         "go": ["green"],
         "slow": ["amber"],
}

sequence = ["stop", "prepare", "go", "slow"]

for state in sequence :
    light_states= states[state]
    print(f"{state=}")
    for (name,led) in lights.items():
        if name in light_states:
            led.on()
        else:
            led.off()

