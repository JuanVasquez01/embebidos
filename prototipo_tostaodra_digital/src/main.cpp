#include <Arduino.h>
#include <MAX6675.h>
#include <LiquidCrystal_I2C.h>

// Definición de pines y variables
const int thermoCLK = 18; // SCK
const int thermoCS = 19;  // CS
const int thermoDO = 20;  // SO
const int toasterPin = 2;
const int convectionFanPin = 3;
const int coolingSystemPin = 4;
const int agitatorPin = 5;

MAX6675 thermocouple(thermoCLK, thermoCS, thermoDO);

// Configura la pantalla LCD
const int LCD_ADDR = 0x27; // Dirección I2C del LCD
const int LCD_COLS = 16;   // Número de columnas del LCD
const int LCD_ROWS = 2;    // Número de filas del LCD
LiquidCrystal_I2C lcd(LCD_ADDR, LCD_COLS, LCD_ROWS);

// Función para controlar el tostador
void controlToaster(int temperature, int time) {
  digitalWrite(toasterPin, HIGH); // Enciende el tostador
  // Configura la temperatura y el tiempo de tostado
  delay(time * 1000); // Espera el tiempo configurado (en milisegundos)
  digitalWrite(toasterPin, LOW); // Apaga el tostador
}

// Función para controlar la convección
void controlConvection(int speed, int time) {
  analogWrite(convectionFanPin, speed); // Configura la velocidad del ventilador
  delay(time * 1000); // Espera el tiempo configurado (en milisegundos)
  analogWrite(convectionFanPin, 0); // Apaga el ventilador
}

// Función para controlar el enfriamiento
void controlCooling(int temperature, int time) {
  digitalWrite(coolingSystemPin, HIGH); // Enciende el sistema de enfriamiento
  // Configura la temperatura de enfriamiento
  delay(time * 1000); // Espera el tiempo configurado (en milisegundos)
  digitalWrite(coolingSystemPin, LOW); // Apaga el sistema de enfriamiento
}

// Función para controlar el agitador
void controlAgitator(int speed, int time) {
  analogWrite(agitatorPin, speed); // Configura la velocidad del agitador
  delay(time * 1000); // Espera el tiempo configurado (en milisegundos)
  analogWrite(agitatorPin, 0); // Apaga el agitador
}

void setup() {
  Serial.begin(9600);
  Serial.println("MAX6675 Test");

  // Inicializa el sensor MAX6675
  // No es necesario llamar a begin() para MAX6675

  // Inicializa la pantalla LCD
  lcd.init();      // Función correcta para inicializar el LCD
  lcd.backlight(); // Enciende la retroiluminación del LCD

  // Configura los pines como salida
  pinMode(toasterPin, OUTPUT);
  pinMode(convectionFanPin, OUTPUT);
  pinMode(coolingSystemPin, OUTPUT);
  pinMode(agitatorPin, OUTPUT);
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
