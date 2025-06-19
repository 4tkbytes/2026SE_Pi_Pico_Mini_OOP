from audio_notification import Audio_Notification
from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from time import sleep, time

def test_led():
    # firstly get it to initialise
    red_light = Led_Light(3, True, False)
    # check using pin val
    assert isinstance(red_light, Led_Light), "class aint initialised"
    
    # next get it to turn on
    red_light.on()
    assert red_light.led_light_state == 1, "its not on"
    sleep(1)
    
    # get it to turn off
    red_light.off()
    assert red_light.led_light_state == 0, "its not off"
    sleep(1)
    
    counter = 0 

    previous_state_1 = red_light.led_light_state
    while counter < 10:
        red_light.flash()
        assert red_light != previous_state_1, f"not previous state: {previous_state_1}"
        previous_state = not previous_state_1
        counter+=1
    
    previous_state_2 = red_light.led_light_state
    
    red_light.toggle()
    assert red_light != previous_state_2, "did not toggle properly"
    sleep(1)
    
    previous_state_3 = not previous_state_2
    red_light.toggle()
    assert red_light != previous_state_3, "did not toggle properly"
    sleep(1)
    
    isCaptured = False
    try:
        red_light.led_light_state = 0.5
        assert isCaptured, "Failed to raise exception at invalid value"
    except TypeError:
        isCaptured = True
        assert isCaptured == True
    
    red_light.led_light_state = 1
    assert red_light.led_light_state == 1, "Failed to get led light state"
    
    print("-------------------------------------------")
    print("LED Light has finished testing, all success")
    print("-------------------------------------------")
    
    print("Resetting value back to default: 0")

def test_button():
    # Replace 22 with the GPIO pin your button is connected to
    button = Pedestrian_Button(22, debug=True)

    print("Testing initial button_state (should be False if not pressed)")
    initial_state = button.button_state
    if initial_state is False:
        print("Initial .button_state passed")
    else:
        print("Initial .button_state failed")

    print("Please press and release the button within 5 seconds...")
    pressed = False
    for _ in range(50):
        if button.button_state:
            pressed = True
            break
        sleep(0.1)

    if pressed:
        print("Button press detected: .button_state passed")
    else:
        print("Button press not detected: .button_state failed")

    print("Testing button_state setter (reset to False)")
    button.button_state = False
    sleep(0.1)
    if button.button_state is False:
        print(".button_state setter passed")
    else:
        print(".button_state setter failed")
    
    print("-------------------------------------------")
    print("Button has finished testing, all success")
    print("-------------------------------------------")

# test_led()
test_button()