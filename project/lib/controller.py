from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep, time

class TrafficLightSubsystem:
    def __init__(self, red, amber, green, debug=False) -> None:
        self.__red = red
        self.__amber = amber
        self.__green = green
        self.__debug = debug
    
    def show_red(self):
        if self.__debug:
            print("Traffic: Red ON")
        self.__red.on()
        self.__amber.off()
        self.__green.off()
        
    def show_amber(self):
        if self.__debug:
            print("Traffic: Red ON")
        self.__red.off()
        self.__amber.on()
        self.__green.off()
        
    def show_green(self):
        if self.__debug:
            print("Traffic: Red ON")
        self.__red.off()
        self.__amber.off()
        self.__green.on()

class PedestrianSubsystem:
    def __init__(self, red: Led_Light, green: Led_Light, button: Pedestrian_Button, buzzer: Audio_Notification, debug=False):
        self.__red = red
        self.__green = green
        self.__button = button
        self.__buzzer = buzzer
        self.__debug = debug
    
    def show_stop(self):
        if self.__debug:
            print("Pedestrian: Red ON")
        self.__red.on()
        self.__green.off()
        self.__buzzer.warning_off()
    
    def show_walk(self):
        if self.__debug:
            print("Pedestrian: Green ON")
        self.__red.off()
        self.__green.on()
        self.__buzzer.warning_on()
    
    def show_warning(self):
        if self.__debug:
            print("Pedestrian: Warning ON")
        self.__red.flash()
        self.__green.off()
        self.__buzzer.warning_off()
    
    def is_button_pressed(self):
        return self.__button.button_state
    
    def reset_button(self):
        self.__button.button_state = False