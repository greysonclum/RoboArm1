import board
import time
i2c = board.I2C()
from adafruit_ads1x15 import ADS1115, AnalogIn, ads1x15

# Create the ADC object using the I2C bus
ads = ADS1115(i2c)

def adc_read():
    """
    Reads the ADC value from the specified channel (0-3).
    """
    #if channel < 0 or channel > 3:
        #raise ValueError("Channel must be between 0 and 3")
    
        # Create single-ended input on channel 0 (A0)
    chan = AnalogIn(ads, ads1x15.Pin.A0)

    return chan.value, chan.voltage

#Reminder, the below runs only when this file is executed directly. Used for testing.
if __name__ == "__main__":
    while True:
        value, voltage = adc_read()
        print(f"ADC Value: {value}, Voltage: {voltage}V")
        time.sleep(1)
        time.sleep(1)
