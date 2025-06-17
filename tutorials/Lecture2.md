# Lecture 2

## Lecture 2 Concepts

- [Overriding Polymorphism](#overriding-polymorphism)
- [DRY](#dry)
    - [Why Use DRY?](#why-use-dry)
- [Encapsulation](#encapsulation)
    - [Benefits of Encapsulation](#benefits-of-encapsulation)
- [Setters and Getters](#setters-and-getters)
    - [State Attribute](#state-attribute)
    - [Getter](#getter)
    - [Setter](#setter)
    - [Why Use Setters & Getters](#why-use-setters--getters)
    - [Test the Setter & Getter](#test-the-setter--getter)
- [Overloading Polymorphism](#overloading-polymorphism)
    - [Adhoc Method Overloading](#adhoc-method-overloading)

## Overriding Polymorphism

**Polymorphism means “many forms.”**

Polymorphism Overriding occurs when a Sub Class provides a new implementation for a method it inherits from its Super Class.

The method in the Sub Class has the same name and parameters as the one in the Super Class. When the method is called on an object of the Sub Class, Python (or any object-oriented language) uses the Sub Class’s version, even if the object is referenced using the Super type (`self.super.method()`).

In this example, we will apply overriding polymorphism and develop new implementations for the `on()`, `off()` and `toggle()` methods. We will extend the functionality of the methods to provide debugging support.

```python
from machine import Pin
from time import sleep

class Led_Light(Pin):
    # Sub Class inherits the 'Pin' Class
    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing

    def on(self):
        # method overriding polymorphism of the Super Class
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is high")

    def off(self):
        # method overriding polymorphism of the Super Class
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is low")

    def toggle(self):
        # method overriding polymorphism of the Super Class
        if self.value() == 0:
            self.on()
        elif self.value() == 1:
           self.off()


red_light = Led_Light(3, False, False)

while True:
    red_light.on()
    sleep(1)
    red_light.off()
    sleep(1)
```

## DRY

The DRY pattern stands for "**Don't Repeat Yourself**"; it is a fundamental principle of programming aimed at reducing repetition of code and logic. This is to avoid duplicating code, logic, or data.

### Why Use DRY?
- Maintainability: When logic is defined in only one place, updates or bug fixes are only needed once.
- Readability: The code is easier to read and understand because there is less repetition.
- Consistency: Reduces the risk of inconsistencies and errors that can occur when updating duplicated code in multiple places.

```python
##### WET #####
    def on(self):
        # method overriding polymorphism of the Super Class
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is high")

    def off(self):
        # method overriding polymorphism of the Super Class
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is low")

    def toggle(self):
        # method overriding polymorphism of the Super Class
        if self.value() == 0:
            self.high()
            if self.__debug:
                print(f"LED connected to Pin {self.__pin} is high")
        elif self.value() == 1:
           self.low()
            if self.__debug:
                print(f"LED connected to Pin {self.__pin} is low")

##### DRY #####
    def on(self):
        # method overriding polymorphism of the Super Class
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is high")

    def off(self):
        # method overriding polymorphism of the Super Class
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is low")

    def toggle(self):
        # method overriding polymorphism of the Super Class
        if self.value() == 0:
            self.on()
        elif self.value() == 1:
           self.off()

```

## Encapsulation
Encapsulation restricts direct access to some of an object's components (such as attributes or methods), meaning the internal representation of the object is hidden from the outside. This is typically achieved by making certain attributes or methods private (i.e., inaccessible from outside the class), and providing public methods (such as getters and setters) to access or modify those private members.

### Benefits of Encapsulation:

- Data Hiding: Internal object details are hidden, exposing only what is necessary.
- Improved Security: Prevents external code from directly modifying internal state in unexpected ways.
- Modularity: Each object manages its own state and behaviour, making code more modular and easier to maintain.
- Flexibility: Implementation can change without affecting code that uses the object, as long as the public interface remains the same.

```python
while True:
    print(red_light.led_light_state) # Allowed
    red_light.led_light_state = 1 # Allowed
    print(f"Not allowed: {red_light.__pin} ???") # Not allowed, should raise AttributeError
```

> [!Note]
> In Python, identifiers (variable or method names) that start with double underscores (e.g., `__my_var`) are not truly private in the sense of other languages like C# or C++. Instead, Python uses a mechanism called name mangling. When you define a variable with double underscores, Python changes its name internally to `_ClassName__my_var`. This means it is harder (but not impossible) to access it from outside the class.

## Setters and Getters

Setters and getters are special methods used in object-oriented programming to access (get) or modify (set) the values of private or protected attributes of a class. They help encapsulate the internal state of an object, providing controlled access.

### State Attribute

First, we need an attribute to hold state for the setter and getter `self.led_light_state`.

```python
def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        self.led_light_state
```

### Getter

- A getter is a method that retrieves (gets) the value of a private attribute.
- It allows you to read the value without providing direct access to the underlying variable.

```python
    @property
    def led_light_state(self):
        # Getter method
        return self.value()
```

### Setter

- A setter is a method that sets (updates) the value of a private attribute.
- It allows you to validate or restrict changes before updating the attribute.

```python
    @led_light_state.setter
    def led_light_state(self, value):
        # Setter method
        if value == 1:
            self.off()
        elif value == 0:
            self.on()
```

### Why Use Setters & Getters
- Encapsulation: Protects the internal state of the object.
- Validation: Allows you to add checks before changing values.
- Abstraction: Hides implementation details from users of the class.

### Test the Setter & Getter

```python
red_light = Led_Light(3, False, False)

while True:
    print(red_light.led_light_state)
    red_light.led_light_state = 1
    sleep(0.25)
    print(red_light.led_light_state)
    red_light.led_light_state = 0
    sleep(0.25)
```

## Overloading Polymorphism

**Polymorphism means “many forms.”**

Overloading occurs when a Sub (sub) and/or Super (super) have multiple methods with the same name but different parameters (number or type).

When you call the method, depending on the parameters passed, the corresponding method is executed.

Because Python is dynamically typed, it does not support overloaded polymorphism, as the last definition of a method overwrites any previous ones.

```text
Class Led_Light inherits from Pin:
    Method __init__(pin, flashing = False, debug = False):
        Call Super Class (Pin) constructor with pin and output mode
        SET led_light_state (property, see below)
        PRIVATE SET debug attribute to debug
        PRIVATE SET pin attribute to pin
        PRIVATE SET flashing attribute to flashing

    METHOD on():
        SET the pin high
        If debug is enabled:
            Print "LED connected to Pin [pin number] is [led_light_state]"

    METHOD off():
        SET the pin low
        IF debug is enabled:
            Print "LED connected to Pin [pin number] is [led_light_state]"

    METHOD toggle():
        IF pin value is 0:
            CALL on()
        ELSE if pin value is 1:
            CALL off()

    METHOD led_light_state ():
        RETURN the pin's current value

    METHOD led_light_state (value):
       IF value is 1:
            CALL off()
        ELSE IF value is 0:
            CALL on()
```

### Adhoc Method Overloading

Adhoc Method Overloading is a common approach to overloading in Python, demonstrated in the implementations below.

```python
# Default parameters
class MyClass:
    def my_method(self, a, b=None):
        if b is None:
            print(f"Called with one argument: {a}")
        else:
            print(f"Called with two arguments: {a}, {b}")

obj = MyClass()
obj.my_method(1)       # Called with one argument: 1
obj.my_method(1, 2)    # Called with two arguments: 1, 2
```

```python
# Variable Arguments
class MyClass:
    def my_method(self, *args, **kwargs):
        if len(args) == 1:
            print(f"One argument: {args[0]}")
        elif len(args) == 2:
            print(f"Two arguments: {args[0]}, {args[1]}")
        else:
            print(f"Other combination: {args}")

obj = MyClass()
obj.my_method(1)       # One argument: 1
obj.my_method(1, 2)    # Two arguments: 1, 2
```

```python
# Manual Type Checking
class MyClass:
    def my_method(self, a):
        if isinstance(a, int):
            print("Integer!")
        elif isinstance(a, str):
            print("String!")
        else:
            print("Other type!")

obj = MyClass()
obj.my_method(42)    # Integer!
obj.my_method("hi")  # String!
```
