import spidev
import time

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI bus 0, device (CS) 0
spi.max_speed_hz = 1350000

def read_adc(channel):
    """
    Reads the ADC value from the specified channel (0-7).
    """
    if channel < 0 or channel > 7:
        raise ValueError("Channel must be between 0 and 7")
    
    # Send start bit, single-ended mode, and channel selection
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    # Combine the result to get a 10-bit value
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def main():
    print("Reading ADC values. Press Ctrl+C to stop.")
    try:
        while True:
            # Read from channel 0 (you can change this to other channels)
            adc_value = read_adc(0)
            print(f"ADC Channel 0 Value: {adc_value}")
            time.sleep(0.5)  # Delay for readability
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        spi.close()

if __name__ == "__main__":
    main()