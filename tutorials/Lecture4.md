# Lecture 4

## Lecture 4 Concepts

- [Pedestrian_Button Class](#pedestrian_button-class)
    - [Create Files](#create-files)
    - [Imports and Constructor](#imports-and-constructor)
    - [Implement an Interrupt](#implement-an-interrupt)
    - [Getter and Setter](#getter-and-setter)
    - [Create a Callback Method for the Interrupt Trigger](#create-a-callback-method-for-the-interrupt-trigger)

## Pedestrian_Button Class

The Pedestrian_Button class extends the Pin class to provide a debounced button interface specifically designed for pedestrian crossing systems. It uses interrupt-based detection and software debouncing to reliably capture button presses. It also provides optional debug output.

### Create Files

1. Create a Python file in `project\lib` called `pedestrian_button.py`
2. Create a Python file in `project\py_scripts` called `v05.py`

### Imports and Constructor

In your `pedestrian_button.py` include your imports, define the class and configure the initialiser with the parameters pin and debug. Add the required parameters to store time and hold state if the button has been pressed.

```python
from machine import Pin
import time


class Pedestrian_Button(Pin):
    # Sub Class inherits the Super 'Pin' 

    def __init__(self, pin, debug):
        super().__init__(pin, Pin.IN, Pin.PULL_DOWN)
        self.__debug = debug
        self.__pin = pin
        self.__last_pressed = 0  # Track the last time the button was pressed
        self.__pedestrian_waiting = False
        self.irq(
            trigger=Pin.IRQ_RISING, handler=self.callback
        )  # Set up interrupt on rising edge
```

### Implement an Interrupt

An interrupt is a signal to the processor that an event needs immediate attention. Instead of constantly checking (polling) if something has happened, interrupts allow the system to be notified immediately when an event occurs.

1. self.irq() is inherited from the Pin Class and stands for Interrupt Request.
2. `trigger=Pin.IRQ_RISING` The interrupt will be triggered when the pin state changes from LOW (0) to HIGH (1).
3. `handler=self.callback` The `self.callback` method will be executed whenever the button is pressed.

```python
class Pedestrian_Button(Pin):
    # Sub Class inherits the Super 'Pin' 

    def __init__(self, pin, debug):
        super().__init__(pin, Pin.IN, Pin.PULL_DOWN)
        self.irq(
            trigger=Pin.IRQ_RISING, handler=self.callback
        )  # Set up interrupt on rising edge
```

### Getter and Setter

Our system has a design requirement that the button state is stored until the walk lights have been displayed. So, because we are not setting or getting the current state of the button as we did with the LED_Light Class, we will use an ad hoc method that updates the `__pedestrian_waiting` attribute.

- If `button_state()` is called with no arguments, it returns the current state (getter).
- If `button_state(bool)` is called with a boolean argument, it sets the state (setter).

```python
    def button_state(self, value=None):
        if value is None:
            # Getter
            if self.__debug:
                print(
                    f"Button connected to Pin {self.__pin} is {'WAITING' if self.__pedestrian_waiting else 'NOT WAITING'}"
                )
            return self.__pedestrian_waiting
        else:
            self.__pedestrian_waiting = bool(
                value
            )  # Convert to boolean to ensure proper type
            if self.__debug:
                print(
                    f"Button state on Pin {self.__pin} set to {self.__pedestrian_waiting}"
                )
```

### Create a Callback Method for the Interrupt Trigger

This `callback()` was configured in the attributes and will be executed in response to an interrupt call.

```python
    def callback(self, pin):
        current_time = time.ticks_ms()  # Get the current time in milliseconds
        if (
            time.ticks_diff(current_time, self.__last_pressed) > 200
        ):  # 200ms debounce delay
            self.__last_pressed = current_time
            self.__pedestrian_waiting = True
            if self.__debug:
                print(f"Button pressed on Pin {self.__pin} at {current_time}ms")
```
