# Lecture 5

## Lecture 5 Concepts

- [Audio_Notification Class](#audio_notification-class)
    - [Create Files](#create-files)
- [What Are Stubs and Drivers?](#what-are-stubs-and-drivers)
  - [Why Use Stubs and Drivers?](#why-use-stubs-and-drivers)
  - [Stub Example](#stub-example)
  - [Driver Example](#driver-example)
- [Implement the Audio_Notification Class](#implement-the-audio_notification-class)
  - [Imports and Constructor](#imports-and-constructor)
  - [Create a Single Beep](#create-a-single-beep)
  - [Implement a Non-Blocking Audio Notification](#implement-a-non-blocking-audio-notification)
  - [Turn Audio Notification Off](#turn-audio-notification-off)

## Audio_Notification Class

The Audio_Notification extends the machine.PWM to provide an interface for controlling a piezo buzzer or speaker, with optional debug output. It supports warning beeps and custom tones.

### Create Files

1. Create a Python file in `project\lib` called `audio_notification.py`
2. Create a Python file in `project\py_scripts` called `v06.py`

## What Are Stubs and Drivers? 

Imagine you're building a puzzle:
- A **stub** is a fake puzzle piece you use temporarily
- A **driver** is a simple tool to check if your real pieces fit together

Definitions
A **stub** is a simplified version that replaces a real lower component so it doesn't need to be full implemented.
A **driver** is a simple program in a higher system that tests a lower component without fully implementing the higher system.

### Why Use Stubs and Drivers?

1. **Test in parts**: Check each piece of your code separately
2. **No dependencies**: Test without needing everything to be finished
3. **Controlled testing**: Create specific test scenarios easily
4. **Faster development**: Don't need to wait for other parts to be done

This simple approach helps you build and test your code without needing to complete your system!

### Stub Example

Remember a **stub** is a simplified version that replaces a real lower component so it doesn't need to be full implemented. We are going to implement the Audio_Notification Class as a Stub so we can test the components that we will later use in a PedestrianSubSystem before fully implementing the Audio_Notification Class.

```python
# audio_notification.py Stub Implementation
class Audio_Notification:
    def __init__(self, pin):
        self.__pin = pin
    
    def warning_on(self):
        # Just pretend to Beep
        print("Beep")
```

### Driver Example

Remember a **driver** is a simple program in a higher system that tests a lower component without fully implementing the higher system.

```python
# v05.py Driver Implementation

# Import the real component we want to test
from audio_notification import Audio_Notification
from led_light import Led_Light

def PedestrianSubsystem_driver():
    print("Testing Traffic Light...")
    
    # Create the walk light
    led_pedestrian_green = Led_Light(17, True, True)
    
    # Create the Audio Notification
    audio_stub = Audio_Notification(27, False)
    
    # Test walk state
    led_pedestrian_green.on()
    audio_stub.warning_on()

    print("Test complete!")

# Run the test
test_traffic_light()
```

## Implement the Audio_Notification Class

## Imports and Constructor

In your `audio_notification.py`, include your imports, define the class, and configure the initialiser with the parameters' pin' and' debug'. Add the required parameters to store time and set the duty cycle.

```python
from machine import Pin, PWM
from time import sleep, time


class Audio_Notification(PWM):
    def __init__(self, pin, debug=False):
        super().__init__(Pin(pin))
        self.__debug = debug
        self.duty_u16(0)  # Start with buzzer off
        self.__last_toggle_time = time()
```
## Create a Single Beep

```python
    def beep(self, freq=1000, duration=500):
        self.freq(freq)
        self.duty_u16(32768)  # 50% duty cycle
        sleep(duration / 1000)
        self.duty_u16(0)  # Turn off after beep
        if self.__debug:
            print("Beep")
```
## Implement a Non-Blocking Audio Notification

```python
    def warning_on(self):
        if self.__debug:
            print("Warning on")
        now = time()
        if now - self.__last_toggle_time >= 0.5:
            self.beep(freq=500, duration=100)
            self.__last_toggle_time = now
```
## Turn Audio Notification Off

```python
    def warning_off(self):
        if self.__debug:
            print("Warning off")
        self.duty_u16(0)  # Turn off sound
```