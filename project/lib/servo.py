from machine import PWM


class Servo:
    """Servo Class for controlling pulse density modulation servos.

    This class provides an interface for controlling servo motors using PWM signals.
    It handles the conversion between angles (0-180 degrees) and pulse widths.

    Args:
        pwm (PWM): A PWM object to control the servo.
        min_us (int, optional): Minimum pulse width in microseconds. Defaults to 500.
        max_us (int, optional): Maximum pulse width in microseconds. Defaults to 2500.
        dead_zone_us (int, optional): Pulse width for the servo's neutral position. Defaults to 1500.
        freq (int, optional): PWM frequency in Hz. Defaults to 50.
    """

    def __init__(
        self,
        pwm: PWM,
        min_us=500,
        max_us=2500,
        dead_zone_us=1500,
        freq=50,
    ):
        """Initialize the Servo object with the given parameters.

        Args:
            pwm (PWM): A PWM object to control the servo.
            min_us (int, optional): Minimum pulse width in microseconds. Defaults to 500.
            max_us (int, optional): Maximum pulse width in microseconds. Defaults to 2500.
            dead_zone_us (int, optional): Pulse width for the servo's neutral position. Defaults to 1500.
            freq (int, optional): PWM frequency in Hz. Defaults to 50.
        """
        self.pwm = pwm
        self.pwm.freq(freq)
        self._move_period_ms = 1000 // freq
        min_us = min_us if min_us > 0 else 0
        max_us = max_us if min_us < max_us < (1000 // freq) * 1000 else 0
        self._curr_duty = 0
        self.dead_zone_us = dead_zone_us

    def set_duty(self, duty_us: int):
        """Set the duty cycle of the PWM signal in microseconds.

        Args:
            duty_us (int): Pulse width in microseconds.
        """
        self._curr_duty = duty_us
        self.pwm.duty_ns(duty_us * 1000)

    def set_angle(self, angle: int):
        """Set the servo angle between 0 and 180 degrees.

        Converts the angle to the appropriate duty cycle and applies it.

        Args:
            angle (int): Desired angle in degrees (0-180).
        """
        angle = min(max(angle, 0), 180)
        duty_us = int(500 + (angle / 180) * 2000)
        self.set_duty(duty_us)

    def get_duty(self) -> int:
        """Get the current duty cycle of the PWM signal.

        Returns:
            int: Current pulse width in microseconds.
        """
        return self._curr_duty

    def stop(self):
        """Stop the servo by setting it to the neutral position (dead zone)."""
        self.set_duty(self.dead_zone_us)

    def deinit(self):
        """Deinitialize the PWM object.

        This should be called when the servo is no longer needed to free resources.
        """
        self.pwm.deinit()
