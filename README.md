# MicroPython OOP Pi Pico Mini Project

This repository is a series of introduction tasks to teach students the basics of Pi Pico and common mechatronic components. Then students will create a mini OOP based project to explicitly teach Object Oriented Paradigm (OOP) programming concepts specifically in the microcontroller context.

Students will be recreating a model of the pedestrian crossing on Unwins Bridge Road out the front of Tempe High School.

## Introduction to Pi Pico & Common Mechatronic Commonents

### Projects

1. [Connect and control a LED](introduction_projects/1.blink_led.md)
2. [Connect a digital sensor that controls the LEDs](introduction_projects/2.digital_sensor.md)
3. [Connect a analog sensor that controls the LEDs](introduction_projects/3.analog_sensor.md)
4. [Control the brightness of the LED with Pulse Width Modulation](introduction_projects/4.pulse_width_modulation.md)
5. [Connect and control a servo motor](introduction_projects/5.servo_control.md)
6. [Connect and read a ultrasonic sensor use it to control the servo motor](introduction_projects/6.ultrasonic_sensor.md)
7. [Connect and control a I2C 16x2 LCD Display](introduction_projects/7.I2C_module.md)

### Components

> [!Note]
> Students can build using physical components or prototype using this [Template Wokwi Project](https://wokwi.com/projects/433242006092880897).

- Breadboard
- Jumper leads
- Pi Pico
- 1x LED
- 1x 130Ω resistors
- 1x Potentiometer or analog sensor
- 1x Momentary switch or digital sensor
- 1x Servo motor
- 1x Ultrasonic sensor
- 1x 2IC 16x2 LCD Display

### Pin Allocation

| Pin  |                        |
| ---- | ---------------------- |
| GP0  | SDA                    |
| GP1  | SCL                    |
| GP4  | Keyboard Interrupt     |
| GP10 | Servo Motor Signal     |
| GP11 | Ultrasonic Echo Signal |
| GP12 | Ultrasonic Trig Signal |
| GP13 | Digital Sensor Signal  |
| GP15 | External LED           |
| GP25 | Inbuilt LED            |
| GP26 | Analog Sensor Signal   |
| AGND | Analog Ground          |
| GND  | Ground                 |
| 3V3  | 3V Power               |
| VBUS | 5V Power               |

## OOP Mini Project

![A street view image of the system we will be modeling](/images/real_world_situation.png "The traffic lights, pedestrian warning lights, pedestrian button and control system.")

### Final Product

![Video of Final Project in Operations](/images/demonstration.gif)

### Wire your system

![A prototype of the model](/images/prototype_model.png "Use the below components to wire this model.")

### Components

> [!Note]
> Students can build using physical components or prototype using this [Template Wokwi Project](https://wokwi.com/projects/433242006092880897).

- Breadboard
- Jumper leads
- Pi Pico
- 1x Momentary switch
- 5x LED
- 1x Piezo buzzer
- 5x 130Ω resistors

### Pin allocation

| Pin  |                      |
| ---- | -------------------- |
| GP3  | Red LED              |
| GP4  | Keyboard Interrupt   |
| GP5  | Amber LED            |
| GP7  | Red LED              |
| GP17 | Flashing Green LED   |
| GP19 | Flashing Red LED     |
| GP22 | Button signal        |
| GP27 | Piezo Buzzer         |
| GND  | Circuit Ground       |
| 3V3  | Button logic voltage |

### Final UML Diagram

```mermaid
classDiagram
    class Pin {
        -__pin: int
        +__init__(pin: int)
        +value()
        +high()
        +low()
        +toggle()
    }

    class PWM {
        -__pin: int
        +__init__(pin: int)
        +freq(freq: int)
        +duty_u16(duty: int)
    }

    class Audio_Notification {
        -__debug: bool
        +__init__(pin: int, debug: bool)
        +warning_on()
        +warning_off()
        +beep(freq: int, duration: int)
    }
    PWM <|-- Audio_Notification : Inheritance

    class Led_Light {
        -__debug: bool
        -__pin: int
        -__flashing: bool
        +__init__(pin: int, flashing: bool, debug: bool)
        +on()
        +off()
        +toggle()
        +flash(duration: int)
        +on_for(duration: int)
        +led_light_state: int
    }
    Pin <|-- Led_Light : Inheritance

    class Pedestrian_Button {
        -__debug: bool
        -__pin: int
        -__last_pressed: int
        -__pedestrian_waiting: bool
        +__init__(pin: int, debug: bool)
        +callback(pin: Pin)
        +button_state
        +reset
    }
    Pin <|-- Pedestrian_Button : Inheritance

    class Controller {
        -__object: Led_Light
        -__object: Led_Light
        -__object: Led_Light
        -__object: Led_Light
        -__object: Led_Light
        -__object: Pedestrian_Button
        -__object: Audio_Notification
    }

    Led_Light --> Controller : Composition
    Audio_Notification --> Controller : Composition
    Pedestrian_Button --> Controller : Composition

```

> [!Note]
> Inheritance and association labels are note required in a UML diagram but have been added for understanding.

## Script Versions Provided

| Version | Notes                                                                                                                     |
| ------- | ------------------------------------------------------------------------------------------------------------------------- |
| v01.py  | Basic "Blink" Program (the Hello World of mechatronics) for Unit Testing the Microcontroller.                                                                  |
| v02.py  | Unit Test for wiring and use basic methods from parent `Pin` and `PWM` class.                                                                |
| v03.py  | A blank python script.    |

##

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/TempeHS/MicroPython_OOP_Pi_Pico_Mini_Project_Source">MicroPython_OOP_Pi_Pico_Mini_Project_Source
</a> and <a property="dct:title" rel="cc:attributionURL" href="https://github.com/TempeHS/MicroPython_OOP_Pi_Pico_Mini_Project_Template">MicroPython_OOP_Pi_Pico_Mini_Project_Template
</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/benpaddlejones">Ben Jones</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>
