from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep, time


class Controller:
    def __init__(
        self, ped_red, ped_green, car_red, car_amber, car_green, button, buzzer, debug
    ):
        self.__Ped_Red = ped_red
        self.__Ped_Green = ped_green
        self.__Car_Red = car_red
        self.__Car_Amber = car_amber
        self.__Car_Green = car_green
        self.__Buzzer = buzzer
        self.__Button = button
        self.__debug = debug
        self.state = "IDLE"
        self.last_state_change = time()

    def walk_on(self):
        if self.__debug:
            print("Walking")
        self.__Ped_Red.off()
        self.__Ped_Green.on()
        self.__Car_Green.off()
        self.__Car_Amber.off()
        self.__Car_Red.on()
        self.__Buzzer.warning_on()

    def walk_warning(self):
        if self.__debug:
            print("No Walking Warning")
        self.__Ped_Red.flash()
        self.__Ped_Green.off()
        self.__Car_Green.off()
        self.__Car_Amber.off()
        self.__Car_Red.on()
        self.__Buzzer.warning_off()

    def walk_off(self):
        if self.__debug:
            print("No Walking")
        self.__Ped_Red.on()
        self.__Ped_Green.off()
        self.__Car_Green.on()
        self.__Car_Amber.off()
        self.__Car_Red.off()
        self.__Ped_Green.off()
        self.__Buzzer.warning_off()

    def change(self):
        if self.__debug:
            print("Changing")
        self.__Ped_Red.on()
        self.__Ped_Green.off()
        self.__Car_Green.off()
        self.__Car_Amber.on()
        self.__Car_Red.off()
        self.__Ped_Green.off()
        self.__Buzzer.warning_off()

    def update(self):
        # State machine logic
        if self.state == "IDLE":
            if self.__Button.button_state:
                if self.__debug:
                    print("Pedestrian waiting detected, switching to CAR_AMBER")
                self.state = "CAR_AMBER"
                self.last_state_change = time()
                self.change()
            else:
                self.walk_off()
        elif self.state == "CAR_AMBER":
            # Wait 10 seconds before allowing walk
            self.change()
            if time() - self.last_state_change > 5:
                if self.__debug:
                    print("Switching to WALK_ON")
                self.state = "WALK_ON"
                self.last_state_change = time()
                self.walk_on()
        elif self.state == "WALK_ON":
            # Walk signal for 5 seconds
            self.walk_on()
            if time() - self.last_state_change > 5:
                if self.__debug:
                    print("Switching to No Walk Warning")
                self.state = "WALK_WARNING"
                self.last_state_change = time()
                self.walk_warning()
        elif self.state == "WALK_WARNING":
            # Walk signal for 5 seconds
            self.walk_warning()
            if time() - self.last_state_change > 5:
                if self.__debug:
                    print("Returning to IDLE")
                self.state = "IDLE"
                self.last_state_change = time()
                self.walk_off()
                self.__Button.button_state = False
        else:  # error
            self.__Ped_Red.on()
            self.__Ped_Green.off()
            self.__Car_Green.off()
            self.__Car_Amber.toggle()
            self.__Car_Red.off()
            self.__Ped_Green.off()
            sleep(1)
