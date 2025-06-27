import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin where the servo is connected
SERVO_PIN = 17
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Set up PWM on the servo pin at 50Hz
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

def set_servo_angle(angle):
    '''Move servo to the specified angle (0-180)'''
    duty = 2 + (angle / 18)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(0)

try:
    # Example: Move servo to 0, 90, and 180 degrees
    set_servo_angle(0)
    time.sleep(1)
    set_servo_angle(90)
    time.sleep(1)
    set_servo_angle(180)
    time.sleep(1)
finally:
    pwm.stop()
    GPIO.cleanup()
