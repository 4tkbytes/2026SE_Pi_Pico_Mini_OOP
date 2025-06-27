from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep, time


class TrafficLightSubsystem:
    def __init__(self, red: Led_Light, amber: Led_Light, green: Led_Light, debug=False):
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
            print("Traffic: Amber ON")
        self.__red.off()
        self.__amber.on()
        self.__green.off()

    def show_green(self):
        if self.__debug:
            print("Traffic: Green ON")
        self.__red.off()
        self.__amber.off()
        self.__green.on()
    
    def off(self):
        if self.__debug:
            print("Everything is off")
        self.__red.off()
        self.__amber.off()
        self.__green.off()


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
            print("Pedestrian: Warning")
        self.__red.flash()
        self.__green.off()
        self.__buzzer.warning_off()

    def is_button_pressed(self):
        return self.__button.button_state

    def reset_button(self):
        self.__button.button_state = False
    
    def off(self):
        if self.__debug:
            print("Everything is off")
        self.__red.off()
        self.__green.off()


def create_new(
        ped_red: Led_Light,
        ped_green: Led_Light,
        traffic_red: Led_Light,
        traffic_amber: Led_Light,
        traffic_green: Led_Light,
        button: Pedestrian_Button,
        buzzer: Audio_Notification,
        debug=False
    ):
        return Controller(
            TrafficLightSubsystem(traffic_red, traffic_amber, traffic_green, debug),
            PedestrianSubsystem(ped_red, ped_green, button, buzzer, debug),
            debug
        )

def create_with_existing(
    traffic_sub: TrafficLightSubsystem,
    ped_sub: PedestrianSubsystem,
    debug = False
):
    return Controller(
        traffic_sub,
        ped_sub
    )

class Controller:
    def __init__(self, 
        traffic_sub: TrafficLightSubsystem,
        ped_sub: PedestrianSubsystem,
        debug = False
    ):
        self.__traffic_lights = traffic_sub
        self.__pedestrian_signals = ped_sub

        self.__debug = debug
        self.state = "IDLE"
        self.__last_state_change = time()

    def set_idle_state(self):
        if self.__debug:
            print("System: IDLE state")
        self.__pedestrian_signals.show_stop()
        self.__traffic_lights.show_green()

    def set_change_state(self):
        if self.__debug:
            print("System: CHANGE state")
        self.__pedestrian_signals.show_stop()
        self.__traffic_lights.show_amber()

    def set_walk_state(self):
        if self.__debug:
            print("System: WALK state")
        self.__pedestrian_signals.show_walk()
        self.__traffic_lights.show_red()


    def set_error_state(self):
        if self.__debug:
            print("System: ERROR state")
        self.__pedestrian_signals.show_stop()
        self.__traffic_lights.show_amber()  # Flashing amber typically indicates malfunction

    def update(self):
        current_time = time()
        time_passed = current_time - self.__last_state_change

        if self.state == "IDLE":
            if self.__pedestrian_signals.is_button_pressed() and time_passed > 5:
                self.state = "CHANGE"
                self.__last_state_change = current_time
                if self.__debug:
                    print("changing to CHANGE")
            self.set_idle_state()

        elif self.state == "CHANGE":
            if time_passed > 5:
                self.state = "WALK"
                self.__last_state_change = current_time
                if self.__debug:
                    print("changing to WALK")
            self.set_change_state()

        elif self.state == "WALK":
            if time_passed > 5:
                self.state = "WALK_WARNING"
                self.__last_state_change = current_time
                if self.__debug:
                    print("changing to WALK WARNING")
            self.set_walk_state()

        elif self.state == "WALK_WARNING":
            if time_passed > 5:
                self.state = "IDLE"
                self.__last_state_change = current_time
                self.__pedestrian_signals.reset_button()
                if self.__debug:
                    print("changing to IDLE")
            self.set_warning_state()

        else:  # error state
            self.set_error_state()
            sleep(1)
    def set_warning_state(self):
        if self.__debug:
            print("System: WALK WARNING state")
        self.__pedestrian_signals.show_warning()
        self.__traffic_lights.show_red()