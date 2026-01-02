# Desktop robot arm control script 12/31/2025
import time
from adafruit_servokit import ServoKit
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

############# Set channels to the number of servo channels on your kit. #############
# 16 for PCA9685 board.

kit = ServoKit(channels=16)



############# Set up I2C for ADS1115 ##############

i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADS object and specify the gain
ads = ADS.ADS1115(i2c)
ads.gain = 1 
chan = AnalogIn(ads, ADS.P0)

# Continuously print the values
while True:
    print(f"MQ-135 Voltage: {chan.voltage}V")
    time.sleep(1)
    kit.servo[0].angle = 180
    kit.continuous_servo[1].throttle = 1
    print("The angle of servo is : ", kit.servo[0].angle)
    time.sleep(1)
    kit.continuous_servo[1].throttle = -1
    print("The angle of servo is : ", kit.servo[0].angle)
    time.sleep(1)
    kit.servo[0].angle = 0
    kit.continuous_servo[1].throttle = 0
    print("The angle of servo is : ", kit.servo[0].angle)

