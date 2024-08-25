import RPi.GPIO as GPIO
import time


class PinHandler:
    def __init__(self, pin, hz=50) -> None:
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)

        self.pwm = GPIO.PWM(pin, hz)
        self.pwm.start(0)

    def set_servo_position(self, angle):
        try:
            duty_cycle = self._angle_to_duty_cycle(angle)
            self.pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.5)  # Give the servo time to reach the position
            self.pwm.ChangeDutyCycle(0)  # Stop sending the signal
        except Exception as e:
            print(f"Error: {e}")

    # Helper function to convert angle to duty cycle
    def _angle_to_duty_cycle(self, angle):
        return (angle / 18) + 2.5

    def stop(self):
        """Stop the PWM signal and clean up the GPIO resources."""
        self.pwm.stop()
        GPIO.cleanup()
