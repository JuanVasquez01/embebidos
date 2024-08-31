// Lenguaje: C++ (Arduino)
#include <Adafruit_Sensor.h>
#include <DHT.h>

// Definir el pin al que está conectado el sensor DHT11
#define DHTPIN 13

// Definir el tipo de sensor DHT
#define DHTTYPE DHT11

// Crear una instancia del sensor DHT
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // Iniciar la comunicación serie
  Serial.begin(115200);
  
  // Iniciar el sensor DHT
  dht.begin();
}

void loop() {
  // Esperar 2 segundos entre lecturas
  delay(2000);

  // Leer la humedad
  float h = dht.readHumidity();
  // Leer la temperatura en grados Celsius
  float t = dht.readTemperature();

  // Verificar si alguna lectura falló
  if (isnan(h) || isnan(t)) {
    Serial.println("Error al leer del sensor DHT!");
    return;
  }

  // Imprimir los valores leídos en el monitor serie
  Serial.print("Humedad: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperatura: ");
  Serial.print(t);
  Serial.println(" *C");
}