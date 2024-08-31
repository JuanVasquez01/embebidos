#include <MAX6675.h>
#include <SPI.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Configura los pines SPI
const int thermoDO = 19;  // MISO
const int thermoCS = 5;   // CS
const int thermoCLK = 18; // SCK

MAX6675 thermocouple(thermoCLK, thermoCS, thermoDO);

// Configura la pantalla LCD
const int LCD_ADDR = 0x27; // Dirección I2C del LCD
const int LCD_COLS = 16;   // Número de columnas del LCD
const int LCD_ROWS = 2;    // Número de filas del LCD
LiquidCrystal_I2C lcd(LCD_ADDR, LCD_COLS, LCD_ROWS);

void setup() {
  Serial.begin(9600);
  Serial.println("MAX6675 Test");

  // Inicializa el sensor MAX6675
  // No es necesario llamar a begin() para MAX6675

  // Inicializa la pantalla LCD
  lcd.init();      // Función correcta para inicializar el LCD
  lcd.backlight(); // Enciende la retroiluminación del LCD
}

void loop() {
  // Lee la temperatura en grados Celsius
  float temperature = thermocouple.readCelsius();
  
  
  // Imprime la temperatura en el monitor serial
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" C");

  // Muestra la temperatura en la pantalla LCD
  lcd.clear(); // Limpia la pantalla antes de mostrar nuevos datos
  lcd.setCursor(0, 0); // Coloca el cursor en la primera columna, primera fila
  lcd.print("Temp: ");
  lcd.print(temperature);
  lcd.print(" C");

  // Espera 2 segundos antes de la siguiente lectura
  delay(2000); // tiempo en milisegundos para la espera

  
}

