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
    
    def off(self):
        if self.__debug:
            print("Traffic: All lights are OFF")
        self.__red.off()
        self.__amber.off()
        self.__green.off()
    
    def error(self):
        self.__amber.flash()

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
    
    def off(self):
        if self.__debug:
            print("Pedestrian: All lights are OFF")
        self.__red.off()
        self.__green.off()

class Controller:
    def __init__(self, p_red, p_green, t_red, t_amber, t_green, button, buzzer, debug):
        self.__traffic_lights = TrafficLightSubsystem(t_red, t_amber, t_green, debug)
        self.__pedestrian_signals = PedestrianSubsystem(p_red, p_green, button, buzzer, debug)
        self.__debug = debug
        self.state = "IDLE"
        self.last_state_change = time()
    
    def set_idle_state(self):
        if self.__debug: print("System: IDLE state")
        self.__pedestrian_signals.show_stop()
        self.__traffic_lights.show_green()
    
    def set_change_state(self):
        if self.__debug: print("System: CHANGE state")
        self.__traffic_lights.show_amber()
        self.__pedestrian_signals.show_stop()
    
    def set_walk_state(self):
        if self.__debug: print("System: WALK state")
        self.__pedestrian_signals.show_walk()
        self.__traffic_lights.show_red
    
    def set_warning_state(self):
        if self.__debug: print("System: WARNING state")
        self.__pedestrian_signals.show_warning()
        self.__traffic_lights.show_red()
    
    def set_error_state(self):
        if self.__debug: print("System: ERROR state")
        self.__traffic_lights.error()
        self.__pedestrian_signals.off()