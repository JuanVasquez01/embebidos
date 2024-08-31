from machine import Pin, SPI, I2C
import time
from i2c_lcd import I2cLcd

class MAX6675:
    def __init__(self, cs_pin, sck_pin, miso_pin):
        self.cs = Pin(cs_pin, Pin.OUT)
        self.spi = SPI(1, baudrate=5000000, polarity=0, phase=0, sck=Pin(sck_pin), mosi=None, miso=Pin(miso_pin))
        self.cs.value(1)
    
    def read_temp(self):
        self.cs.value(0)
        raw_data = self.spi.read(2)
        self.cs.value(1)
        
        value = (raw_data[0] << 8) | raw_data[1]
        if value & 0x4:  # Check if thermocouple is connected
            return None
        
        # The first 12 bits contain the temperature data
        value >>= 3
        temp_c = value * 0.25
        return temp_c

# Configura los pines del MAX6675
cs_pin = 5
sck_pin = 18
miso_pin = 19

# Inicializa el módulo MAX6675
sensor = MAX6675(cs_pin, sck_pin, miso_pin)

# Configura el I2C para la pantalla LCD
i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
I2C_ADDR = 0x27
LCD_WIDTH = 16

# Inicializa la pantalla LCD
lcd = I2cLcd(i2c, I2C_ADDR, LCD_WIDTH)

def display_temperature():
    while True:
        temp = sensor.read_temp()
        if temp is not None:
            # Limpiar pantalla y mostrar la temperatura
            lcd.clear()
            lcd.print("Temp: {:.2f} C".format(temp))
        else:
            # Limpiar pantalla y mostrar mensaje de error
            lcd.clear()
            lcd.print("Termocupla no")
            lcd.move_cursor(1, 0)  # Mover a la segunda línea
            lcd.print("conectada")
        time.sleep(1)

# Ejecuta la función para mostrar la temperatura
display_temperature()
