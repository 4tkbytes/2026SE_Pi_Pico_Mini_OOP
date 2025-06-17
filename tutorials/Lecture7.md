# Lecture 7

## Lecture 7 concepts

- [Open and Closed Loop Control Systems](#open-and-closed-loop-control-systems)
  - [Open-Loop](#open-loop)
  - [Closed-Loop](#closed-loop)
- [State Machine](#state-machine)
- [Implement an Open Loop State Machine](#implement-an-open-loop-state-machine)
  - [Define the Controller Class and Initialiser](#define-the-controller-class-and-initialiser)
  - [Define the States](#define-the-states)
  - [Implement the State Machine](#implement-the-state-machine)

## Open and Closed Loop Control Systems

Open-loop and closed-loop control systems are two fundamental types of control systems used in engineering, automation, robotics, and other fields to manage the behaviour of devices or processes.

### Open-Loop

An open-loop control system is a type of system in which the control action is independent of the desired output or the actual system output.

How it works:

- The system receives an input (command or reference signal).
- The controller processes this input and sends a control signal to the actuator.
- The actuator executes the control action, affecting the system or process.
- There is no feedback mechanism to compare the output with the input.

Example:

A microwave oven: You set the cooking time, and the microwave runs for that duration regardless of how hot the food actually gets.

### Closed-Loop

A closed-loop control system (also called a feedback control system) is a system in which the control action is dependent on the desired output and the actual system output.

How it works:

- The system receives an input (desired value or setpoint).
- The controller processes this input and sends a control signal to the actuator.
- The actuator operates on the system.
- A sensor measures the actual output.
- The output is fed back and compared with the input (setpoint).
- The difference (error) is used to adjust the control action, thereby reducing the error.

Example:

A home thermostat allows homeowners to set a desired temperature. The system then measures the actual room temperature and adjusts the heater or cooler to reach and maintain the set temperature. As the system approaches—or overshoots—the desired temperature, it modifies its output accordingly.

## State Machine

A state machine (also known as a finite state machine or FSM) is a computational model used to design and describe systems that can be in one of a finite number of states at any given time. It transitions between these states in response to external inputs or events such as time, button presses, or sensor values.

Key concepts:

- States: Distinct modes or conditions in which the system can exist.
- Transitions: Rules that define how and when the system moves from one state to another, often triggered by events or inputs.
- Events/Inputs: External actions or signals that cause state transitions.
- A State Machine can be open or closed

## Implement an Open Loop State Machine

### Define the Controller Class and Initialiser

> [!Note]
> The subsystems (TrafficLightSubsystem, PedestrianSubsystem) are only used by the Controller Class. They are tightly coupled to it, so we will keep them in the same `controller.py` file as the Controller Class for simplicity and easier maintenance. However, students can equally abstract them to individual `*.py` files for independence if they wish.

```python
class Controller:
    def __init__(
        self,
        ped_red,
        ped_green,
        car_red,
        car_amber,
        car_green,
        button,
        buzzer,
        debug=False,
    ):
        # Initialise subsystems
        self.__traffic_lights = TrafficLightSubsystem(
            car_red, car_amber, car_green, debug
        )
        self.__pedestrian_signals = PedestrianSubsystem(
            ped_red, ped_green, button, buzzer, debug
        )

        # Other controller attributes
        self.__debug = debug
        self.state = "IDLE"
        self.__last_state_change = time()
```

## Define the States

```python
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

    def set_warning_state(self):
        if self.__debug:
            print("System: WALK WARNING state")
        self.__pedestrian_signals.show_warning()
        self.__traffic_lights.show_red()

    def set_error_state(self):
        if self.__debug:
            print("System: ERROR state")
        self.__pedestrian_signals.show_stop()
        self.__traffic_lights.show_amber()  # Flashing amber typically indicates malfunction
```

## Implement the State Machine
This is the main interface method that clients call to operate the entire system. It manages state transitions based on timing and pedestrian button input.

The system cycles through the following states:
- IDLE: Normal operation, traffic flowing
- CHANGE: Transitioning to stop traffic (amber light)
- WALK: Pedestrians crossing (red traffic light, green pedestrian light)
- WALK_WARNING: Warning that walk cycle is ending
- Back to IDLE

```python
    def update(self):
        current_time = time()
        elapsed = current_time - self.__last_state_change

        if self.state == "IDLE":
            if self.__pedestrian_signals.is_button_pressed() and elapsed > 5:
                self.state = "CHANGE"
                self.__last_state_change = current_time
                if self.__debug:
                    print("Switching to CHANGE")
            self.set_idle_state()

        elif self.state == "CHANGE":
            if elapsed > 5:
                self.state = "WALK"
                self.__last_state_change = current_time
                if self.__debug:
                    print("Switching to WALK")
            self.set_change_state()

        elif self.state == "WALK":
            if elapsed > 5:
                self.state = "WALK_WARNING"
                self.__last_state_change = current_time
                if self.__debug:
                    print("Switching to WALK WARNING")
            self.set_walk_state()

        elif self.state == "WALK_WARNING":
            if elapsed > 5:
                self.state = "IDLE"
                self.__last_state_change = current_time
                self.__pedestrian_signals.reset_button()
                if self.__debug:
                    print("Returning to IDLE")
            self.set_warning_state()

        else:  # error state
            self.set_error_state()
            sleep(1)
```
