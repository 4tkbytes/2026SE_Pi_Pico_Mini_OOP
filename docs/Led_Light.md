## Led_Light Class

The `Led_Light`  extends the `machine.Pin`  to provide advanced control of an LED, including toggling, non-blocking flashing, and optional debug output.

## Constructor

```python
Led_Light(pin, flashing=False, debug=False)
```
- `pin`: The GPIO pin number the LED is connected to.
- `flashing`: Set to `True` to enable the flash method.
- `debug`: Set to `True` to enable debug print statements.

## Example Usage

```python
from led_light import Led_Light
from time import sleep

# Create a Led_Light on GPIO pin 3, with flashing and debug enabled
led = Led_Light(3, flashing=True, debug=True)

# Turn the LED on
led.on()

# Turn the LED off
led.off()

# Toggle the LED state
led.toggle()

# Set the LED state using the property (0 = ON, 1 = OFF)
led.led_light_state = 0  # Turns LED ON
led.led_light_state = 1  # Turns LED OFF

# Non-blocking flash: call repeatedly in your main loop
while True:
    led.flash()  # Will toggle every 0.5s if flashing is enabled
    sleep(0.1)
```

## Methods and Properties

- **on()**  
  Turns the LED on and prints debug info if enabled.

- **off()**  
  Turns the LED off and prints debug info if enabled.

- **toggle()**  
  Switches the LED between on and off states.

- **led_light_state** (property)  
  Gets or sets the LED state (0 = ON, 1 = OFF).

- **flash()**  
  Non-blocking: toggles the LED every 0.5 seconds if `flashing=True`. Call this method repeatedly in your main loop.

---

**Note:**  
- The LED should be wired with an appropriate resistor to the specified GPIO pin.
- The  uses the internal features of the `machine.Pin`  for output control.

## Class Unit Test

```python
from time import sleep
from led_light import Led_Light

# Replace 3 with a valid GPIO pin number for your board
led = Led_Light(3, flashing=True, debug=True)

print("Testing on()")
led.on()
sleep(0.1)
if led.value() == 1:
    print(".on() method passed")
else:
    print(".on() method failed")

print("Testing off()")
led.off()
sleep(0.1)
if led.value() == 0:
    print(".off() method passed")
else:
    print(".off() method failed")


print("Testing toggle()")
led.toggle()
sleep(0.1)
if led.value() == 1:
    print(".toggle() .on() method passed")
else:
    print(".toggle() .on() method failed")

led.toggle()
sleep(0.1)
if led.value() == 0:
    print(".toggle() .off() method passed")
else:
    print(".toggle() .off() method failed")


print("Testing led_light_state property (getter)")
state = led.led_light_state
sleep(0.1)
if state == led.value():
    print(".led_light_state passed")
else:
    print(".led_light_state getter failed")

print("Testing led_light_state property (setter) to 1 (should turn on)")
set1 = led.led_light_state = 1
set0 = led.led_light_state = 0
if set1 == 1 and set0 == 0 :
    print(".led_light_state setter passed")
else:
    print(".led_light_state setter failed")

```


## Class Implementation

```python
from machine import Pin
from time import sleep, time


class Led_Light(Pin):
    """LED Light Class that extends machine.Pin to provide higher-level LED control.

    This class provides methods to control an LED including on, off, toggle, and non-blocking flashing.
    It extends the machine.Pin class functionality, overriding and adding methods specific to LED control.

    Args:
        pin (int): The GPIO pin number the LED is connected to.
        flashing (bool, optional): Whether to enable flashing capability. Defaults to False.
        debug (bool, optional): Whether to print debug statements. Defaults to False.
    """

    def __init__(self, pin, flashing=False, debug=False):
        """Initialize the Led_Light object.

        Args:
            pin (int): The GPIO pin number the LED is connected to.
            flashing (bool, optional): Whether to enable flashing capability. Defaults to False.
            debug (bool, optional): Whether to print debug statements. Defaults to False.
        """
        super().__init__(pin, Pin.OUT)
        self.led_light_state
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing
        self.__last_toggle_time = time()

    def on(self):
        """Turn the LED on.

        Overrides the Pin.on() method to provide additional debug output.
        """
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is {self.led_light_state}")

    def off(self):
        """Turn the LED off.

        Overrides the Pin.off() method to provide additional debug output.
        """
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is {self.led_light_state}")

    def toggle(self):
        """Toggle the LED between on and off states.

        If the LED is off, turns it on. If the LED is on, turns it off.
        """
        if self.value() == 0:
            self.on()
        elif self.value() == 1:
            self.off()

    @property
    def led_light_state(self):
        """Get the current state of the LED.

        Returns:
            int: 0 if the LED is off, 1 if the LED is on.
        """
        return self.value()

    @led_light_state.setter
    def led_light_state(self, value):
        """Set the state of the LED.

        Args:
            value (int): 0 turns the LED on, 1 turns the LED off.
        """
        if value == 1:
            self.off()
        elif value == 0:
            self.on()

    def flash(self):
        """Non-blocking flash: toggles LED every 0.5 seconds.

        This method should be called repeatedly in the main loop.
        The LED will toggle only if flashing is enabled and 0.5 seconds
        have elapsed since the last toggle.
        """
        now = time()
        if self.__flashing and now - self.__last_toggle_time >= 0.5:
            self.toggle()
            self.__last_toggle_time = now
```
