import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

def adc_read(channel):
    """
    Reads the ADC value from the specified channel (0-3).
    """
    if channel < 0 or channel > 3:
        raise ValueError("Channel must be between 0 and 3")
    
        # Create single-ended input on channel 0 (A0)
        chan = [AnalogIn(ads, ADS.P0), AnalogIn(ads, ADS.P1), AnalogIn(ads, ADS.P2), AnalogIn(ads, ADS.P3)]

    return chan[channel].value, chan[channel].voltage

#Reminder, the below runs only when this file is executed directly. Used for testing.
if __name__ == "__main__":
    while True:
        adc_read()
        # Read the raw value and convert it to voltage
        print("{:>5}\t{:>5.3f} V".format(chan0.value, chan0.voltage))
        time.sleep(1)