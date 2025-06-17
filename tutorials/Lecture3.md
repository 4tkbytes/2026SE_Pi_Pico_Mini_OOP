# Lecture 3

## Lecture 3 Concepts
- [Abstraction](#abstraction)
  - [Benefits of Abstraction](#benefits-of-abstraction)
  - [VSCode Instructions](#vscode-instructions)
  - [Wokwi Instructions](#wokwi-instructions)
- [Implement a Non-Blocking Flash Method](#implement-a-non-blocking-flash-method)

## Abstraction

Abstraction in Object-Oriented Programming (OOP) is a principle that focuses on exposing only the essential features of an object while hiding the unnecessary details. The primary goal is to offer a simplified, high-level interface for interacting with complex systems, thereby making your code easier to use and understand.

### Benefits of Abstraction

- What vs. How: Abstraction tells you what an object does, not how it does it.
- Simplification: It reduces complexity by hiding implementation details.
- Interface: Abstraction is often achieved by hiding the complex implementation and providing only the interface methods or attributes.

### VSCode Instructions

1. Create a Python file in `project\lib` called `led_light.py`
2. Copy the Class only to `project\lib\led_light.py`

### Wokwi Instructions

1. Click the small down arrow in the folder tabs.
2. Choose **+ New File**
3. Name the file `led_light.py`
4. Copy the Class only to `project\lib\led_light.py`

![Create a new file on Wokwi](/images/wokwi_new_file.png)

```Python
from led_light import Led_Light
from time import sleep

red_light = Led_Light(3, True, True)

while True:
    print(red_light.led_light_state)
    red_light.led_light_state = 1
    sleep(0.25)
    print(red_light.led_light_state)
    red_light.led_light_state = 0
    sleep(0.25)
```

## Implement a Non-Blocking Flash Method

> [!Important]
> Make sure you edit the  in the `project\lib\led_light.py`, not your main.py implementation.

Import time and add a new attribute to store a time value when the LED last toggled.

```python
from time import sleep, time

    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        self.__last_toggle_time = time()
```
Implement a non-blocking flash. This method should be called repeatedly in the main loop. The LED will toggle only if flashing is enabled and 0.5 seconds have elapsed since the last toggle.

```python
    def flash(self):
        now = time()
        if self.__flashing and now - self.__last_toggle_time >= 0.5:
            self.toggle()
            self.__last_toggle_time = now
```

