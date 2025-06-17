from machine import Pin
from time import sleep, time


class Led_Light(Pin):
    # child class inherits the parent 'Pin' class
    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        self.led_light_state
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing
        self._last_toggle_time = time()

    def on(self):
        # method overiding polymorphism of the parent class
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is {self.led_light_state}")

    def off(self):
        # method overiding polymorphism of the parent class
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is {self.led_light_state}")

    def toggle(self):
        # method overiding polymorphism of the parent class
        if self.value() == 0:
            self.on()
        elif self.value() == 1:
            self.off()

    @property
    def led_light_state(self):
        # method overloading polymorphism in this class
        return self.value()

    @led_light_state.setter
    def led_light_state(self, value):
        # method overloading polymorphism in this class
        if value == 1:
            self.off()
        elif value == 0:
            self.on()

    def flash(self):
        # Non-blocking flash: toggles LED every 0.5s for the given duration
        now = time()
        if self.__flashing and now - self._last_toggle_time >= 0.5:
            self.toggle()
            self._last_toggle_time = now
