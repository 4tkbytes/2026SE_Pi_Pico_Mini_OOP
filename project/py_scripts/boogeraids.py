from controller import TrafficLightSubsystem, PedestrianSubsystem
from audio_notification import Audio_Notification
from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from time import sleep

def Subsystem_Driver():
    
    red_light = Led_Light(3, False, True)
    amber_light = Led_Light(5, False, True)
    green_light = Led_Light(7, False, True)
    assert isinstance(red_light, Led_Light), "class aint initialised"
    assert isinstance(amber_light, Led_Light), "class aint initialised"
    assert isinstance(green_light, Led_Light), "class aint initialised"
    
    p_red_light = Led_Light(17, True, True)
    p_green_light = Led_Light(19, True, True)
    assert isinstance(p_red_light, Led_Light), "class aint initialised"
    assert isinstance(p_green_light, Led_Light), "class aint initialised"
    
    p_button = Pedestrian_Button(22, True)
    p_buzzer = Audio_Notification(27, True)
    assert isinstance(p_button, Pedestrian_Button), "class aint initialised"
    assert isinstance(p_buzzer, Audio_Notification), "class aint initialised"
    
    traffic_subsystem = TrafficLightSubsystem(red_light, amber_light, green_light, True)
    p_subsystem = PedestrianSubsystem(p_red_light, p_green_light, p_button, p_buzzer, True)
    assert isinstance(traffic_subsystem, TrafficLightSubsystem), "class aint initialised"
    assert isinstance(p_subsystem, PedestrianSubsystem), "class aint initialised"
    
    traffic_subsystem.show_red()
    sleep(1)
    traffic_subsystem.show_amber()
    sleep(1)
    traffic_subsystem.show_green()
    
    sleep(5)
    
    p_subsystem.show_stop()
    sleep(1)

    p_subsystem.show_walk()
    sleep(1)

    p_subsystem.show_warning()
    sleep(1)

    p_subsystem.show_stop()
    sleep(1)
    
    print("-------------------------------------------")
    print("Subsystem has finished testing, all success")
    print("-------------------------------------------")

Subsystem_Driver()