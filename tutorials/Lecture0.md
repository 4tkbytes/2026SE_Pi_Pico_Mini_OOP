# Lecture 0

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Introduction Projects](#introduction-projects)
- [Common Mistakes Students Make](#common-mistakes-students-make)
- [Wokwi](#wokwi)
- [Final Project](#final-project)
- [Wire your system](#wire-your-system)
    - [Wokwi Prototype](#wokwi-prototype)
    - [Physical Prototype](#physical-prototype)
- [Components](#components)
- [Pin allocation](#pin-allocation)


## Introduction Projects

The Introduction projects should be completed before starting the OOP Mini Project. Ultimately, students should have a basic understanding of the following concepts: different sensors and actuators, wiring a breadboard, Unit Testing, and debugging both software and hardware.

| | |
| --- | --- |
| ![Blink LED](../introduction_projects/images/blink_led.png)<br/>Blink LED | ![Digital Sensor](../introduction_projects/images/digital_sensor.png)<br/>Digital Sensor |
| ![Analog Sensor](../introduction_projects/images/analog_sensor.png)<br/>Analog Sensor | ![Servo Control](../introduction_projects/images/servo_control.png)<br/>Servo Control |
| ![Ultrasonic Sensor](../introduction_projects/images/ultrasonic_sensor.png)<br/>Ultrasonic Sensor | ![I2C Module](../introduction_projects/images/I2C_module.png)<br/>I2C Module |

## Common Mistakes Students Make
1. Programming GPIO Pin 3, but wiring to the 3rd Pin not GP3 (check diagram).
2. Incorrect polarity on an LED.
3. Connecting to the wrong row on a breadboard.
4. Connecting an analogue sensor to the GND rather than the specific analogue ground AGND.
5. Not uploading the 2IC Libraries either to the Pi Pico or to Wokwi.
6. Overcurrent, as the Pi Pico and most sensors are 3.3V sensitive. Only motors should be connected to the VBUS (5v). If a sensor is connected to the VBUS, it will return 5V to the GND, causing an overcurrent situation.


## Wokwi

Wokwi is an online Electronics simulator. You can use it to simulate Arduino, ESP32, STM32, and many other popular boards, parts and sensors. We will be using it for Pi Pico, you can also use the integrated IDE.

Students can sign up or in with OAuth using either their School Google Account or GitHub account.

1. [Wokwi](https://wokwi.com/)
2. [Wokwi Introduction Video](https://www.youtube.com/watch?v=s4QKFw8fh-4)
3. [Wokwi Pi Pico Docs](https://docs.wokwi.com/parts/wokwi-pi-pico)

> [!Note]
> Students using Wokwi should start with [Template Wokwi Project](https://wokwi.com/projects/433242006092880897).

## Final Project

![Video of Final Project in Operations](/images/demonstration.gif)

### Wire your system

#### Wokwi Prototype

![A prototype of the model](/images/prototype_model.png "Use the below components to wire this model.")

#### Physical Prototype

![A prototype of the model](/images/physical_prototype.png "Use the below components to wire this model.")

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
