from time import sleep
try :
    from gpiozero import LED, Button, Buzzer
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

def set_lights(state):
    print(f"{state=}")
    light_states= states[state]

    for (name,led) in lights.items():
        if name in light_states:
            led.on()
        else:
            led.off()

sequence = ["slow","stop", "prepare", "go", ]
btn = Button(2)
buzz = Buzzer(3)
set_lights("go")
while True:
    btn.wait_for_press()
    buzz.on()
    for i in range (5):
        buzz.on()
        sleep(0.2)
        buzz.off()
        sleep(0.2)
    for state in sequence :
        set_lights(state)
        sleep(1)
        buzz.off()
    print(f"{btn.is_pressed=}")
