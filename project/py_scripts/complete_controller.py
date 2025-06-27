import controller

debug = True

red_light = controller.Led_Light(3, False, debug)
amber_light = controller.Led_Light(5, False, debug)
green_light = controller.Led_Light(6, False, debug)

p_red_light = controller.Led_Light(17, True, debug)
p_green_light = controller.Led_Light(19, True, debug)


p_button = controller.Pedestrian_Button(22, debug)
p_buzzer = controller.Audio_Notification(27, debug)

trafficController = controller.create_new(
    red_light,
    amber_light, 
    green_light,
    p_red_light,
    p_green_light,
    p_button,
    p_buzzer
)

while True:
    trafficController.update()
    controller.sleep(0.1)