from led_light import Led_Light
from controller import TrafficLightSubsystem, PedestrianSubsystem, Controller
from audio_notification import Audio_Notification
from pedestrian_button import Pedestrian_Button
from time import sleep, time

instancingWorks = False
trafficLEDWorks = False
pedestrianWorks = False
buttonWorks = False
fullTrafficControllerWorks = False

def Subsystem_Driver():
    debug = False
    
    red_light = Led_Light(3, False, debug)
    amber_light = Led_Light(5, False, debug)
    green_light = Led_Light(6, False, debug)
    assert isinstance(red_light, Led_Light), "class aint initialised"
    assert isinstance(amber_light, Led_Light), "class aint initialised"
    assert isinstance(green_light, Led_Light), "class aint initialised"
    
    p_red_light = Led_Light(19, True, debug)
    p_green_light = Led_Light(17, True, debug)
    assert isinstance(p_red_light, Led_Light), "class aint initialised"
    assert isinstance(p_green_light, Led_Light), "class aint initialised"
    
    p_button = Pedestrian_Button(22, debug)
    p_buzzer = Audio_Notification(27, debug)
    assert isinstance(p_button, Pedestrian_Button), "class aint initialised"
    assert isinstance(p_buzzer, Audio_Notification), "class aint initialised"
    
    traffic_subsystem = TrafficLightSubsystem(red_light, amber_light, green_light, debug)
    p_subsystem = PedestrianSubsystem(p_red_light, p_green_light, p_button, p_buzzer, debug)
    assert isinstance(traffic_subsystem, TrafficLightSubsystem), "class aint initialised"
    assert isinstance(p_subsystem, PedestrianSubsystem), "class aint initialised"
    print("-------------------------------------------")
    print("✅ Class instantiation success"); instancingWorks = True
    print("-------------------------------------------")
    
    error = False
    print("Setting everything off to start testing")
    traffic_subsystem.off()
    p_subsystem.off()
    
    print("Pass if: Red ON, Amber OFF, Green OFF")
    print("Showing red")
    traffic_subsystem.show_red()
    if not traffic_subsystem.__red.led_light_state == 1:
        print("Red is not on")
        error = True
    sleep(1)
    
    print("Pass if: Red OFF, Amber ON, Green OFF")
    print("Showing amber")
    traffic_subsystem.show_amber()
    if not traffic_subsystem.__amber.led_light_state == 1:
        print("Amber is not on")
        error = True
    sleep(1)
    
    print("Pass if: Red OFF, Amber OFF, Green ON")
    print("Showing green")
    traffic_subsystem.show_green()
    if not traffic_subsystem.__green.led_light_state == 1:
            print("Green is not on")
            error = True
    sleep(1)
    
    print("-------------------------------------------")
    if not error: print("✅ Traffic LED success"); trafficLEDWorks = True
    else: print("❌ Traffic LED failed")
    print("-------------------------------------------")
    error = False

    print("All lights are OFF")
    traffic_subsystem.off()
    if not traffic_subsystem.__red.led_light_state == 0: print("Red is expected to be off"); error = True
    if not traffic_subsystem.__green.led_light_state == 0: print("Green is expected to be off"); error = True
    sleep(1)
    
    print("Showing walking")
    p_subsystem.show_walk()
    if not traffic_subsystem.__red.led_light_state== 0: print("Red is expected to be off"); error = True
    if not traffic_subsystem.__green.led_light_state == 0: print("Green is expected to be on"); error = True
    sleep(2)

    print("Showing warning")
    for i in range(3):
        p_subsystem.show_warning()
        if not traffic_subsystem.__red.led_light_state == 0: print("Red is expected to be off"); error = True
        if not traffic_subsystem.__amber.led_light_state == 1: print("Amber is expected to be on"); error = True
        if not traffic_subsystem.__green.led_light_state == 0: print("Green is expected to be off"); error = True
        sleep(0.5)

    print("Showing stop")
    p_subsystem.show_stop()
    if not traffic_subsystem.__red.led_light_state == 0: print("Red is expected to be off"); error = True
    if not traffic_subsystem.__green.led_light_state == 0: print("Green is expected to be off"); error = True
    sleep(2)
    
    print("-------------------------------------------")
    if not error: print("✅ Pedestrian System success"); pedestrianWorks = True
    else: print("❌ Pedestrian System failed")
    print("-------------------------------------------")
    error = False
    # testing out button
    print("Resetting button state. Please release your finger if it is on it")
    p_subsystem.reset_button()
    print("Testing out button press. Click on it")
    while not p_subsystem.is_button_pressed():
        print("Awaiting button press")
    
    print("Button registered input")
    
    print("-------------------------------------------")
    if not error: print("✅ Pedestrian Button success"); buttonWorks = True
    else: print("❌ Pedestrian Button failed")
    print("-------------------------------------------")
    error = False
    
    print("Resetting values of pins")
    p_subsystem.off()
    traffic_subsystem.off()
    
    print("Testing controller")
    
    print("Instantiating controller class")
    controller = Controller(p_red_light, p_green_light, red_light, amber_light, green_light, p_button, p_buzzer, debug)
    assert isinstance(controller, Controller)
    print("Instancing test success")
    
    print("Testing idle state")
    controller.set_idle_state()
    if not controller.__traffic_lights.__red.led_light_state == 0: print("Red is expected to be off"); error = True
    if not controller.__traffic_lights.__amber.led_light_state == 0: print("Amber is expected to be off"); error = True
    if not controller.__traffic_lights.__green.led_light_state == 1: print("Green is expected to be on"); error = True
    
    if not controller.__pedestrian_signals.__red.led_light_state == 1: print("Red is expected to be on"); error = True
    if not controller.__pedestrian_signals.__green.led_light_state == 0: print("Green is expected to be off"); error = True
    sleep(3)
    
    print("Testing change state")
    controller.set_change_state()
    if not controller.__traffic_lights.__red.led_light_state == 0: print("Red is expected to be off"); error = True
    if not controller.__traffic_lights.__amber.led_light_state == 1: print("Amber is expected to be on"); error = True
    if not controller.__traffic_lights.__green.led_light_state == 0: print("Green is expected to be off"); error = True
    
    if not controller.__pedestrian_signals.__red.led_light_state == 1: print("Red is expected to be on"); error = True
    if not controller.__pedestrian_signals.__green.led_light_state == 0: print("Green is expected to be off"); error = True
    sleep(3)

    
    print("Testing walk state")
    controller.set_walk_state()
    if not controller.__traffic_lights.__red.led_light_state == 1: print("Red is expected to be on"); error = True
    if not controller.__traffic_lights.__amber.led_light_state == 0: print("Amber is expected to be off"); error = True
    if not controller.__traffic_lights.__green.led_light_state == 0: print("Green is expected to be off"); error = True
    
    if not controller.__pedestrian_signals.__red.led_light_state == 0: print("Red is expected to be off"); error = True
    if not controller.__pedestrian_signals.__green.led_light_state == 1: print("Green is expected to be on"); error = True
    sleep(3)

    
    print("Testing warning state")
    controller.set_warning_state()    
    if not controller.__traffic_lights.__red.led_light_state == 1: print("Red is expected to be on"); error = True
    if not controller.__traffic_lights.__amber.led_light_state == 0: print("Amber is expected to be off"); error = True
    if not controller.__traffic_lights.__green.led_light_state == 0: print("Green is expected to be off"); error = True
    
    if not controller.__pedestrian_signals.__red.led_light_state == 1: print("Red is expected to be flashing/on"); error = True
    if not controller.__pedestrian_signals.__green.led_light_state == 0: print("Green is expected to be off"); error = True
    
    if not controller.__pedestrian_signals.__red.led_light_state == 1:
        print("Pedestrian Red expected to flash")
        error = True
    sleep(3)
    
    print("Extra: Testing error")
    controller.set_error_state()
    if not controller.__traffic_lights.__red.led_light_state == 0: print("Red is expected to be off"); error = True
    if not controller.__traffic_lights.__amber.led_light_state == 1: print("Amber is expected to be on/flashing"); error = True
    if not controller.__traffic_lights.__green.led_light_state == 0: print("Green is expected to be off"); error = True
    
    if not controller.__pedestrian_signals.__red.led_light_state == 0: print("Red is expected to be off"); error = True
    if not controller.__pedestrian_signals.__green.led_light_state == 0: print("Green is expected to be off"); error = True
    sleep(3)
    
    print("-------------------------------------------")
    if not error: print("✅ Full traffic subsystem success"); fullTrafficControllerWorks = True
    else: print("❌ Full traffic subsystem failed")
    print("-------------------------------------------")
    
    print("-------------------------------------------")
    print("❌ Cleaning Up")
    print("-------------------------------------------")
    traffic_subsystem.off()
    p_subsystem.off()
    
    print("-------------------------------------------")
    print("Subsystem has finished testing, check results")
    print("-------------------------------------------")
    
    print(f"""
          Summary: 
            - Class instancing: {instancingWorks}
            - Traffic LED: {trafficLEDWorks}
            - Pedestrian System: {pedestrianWorks}
            - Pedestrian Button: {buttonWorks}
            - Full Traffic Controller: {fullTrafficControllerWorks} 
          """)

Subsystem_Driver()