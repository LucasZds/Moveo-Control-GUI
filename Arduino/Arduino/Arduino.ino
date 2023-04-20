#include <AccelStepper.h>
#include <Servo.h>

Servo pinza1;

// Definir pines para los motores
const int motor1_en_pin = A3;
const int motor1_dir_pin = A4;
const int motor1_step_pin = A5;

const int motor2_en_pin = A0;
const int motor2_dir_pin = A1;
const int motor2_step_pin = A2;

const int motor3_en_pin = 2;
const int motor3_dir_pin = 3;
const int motor3_step_pin = 4;

const int motor4_en_pin = A6;
const int motor4_dir_pin = A7;
const int motor4_step_pin = 1;

const int motor5_en_pin = 8;
const int motor5_dir_pin = 9;
const int motor5_step_pin = 10;

const int motor6_en_pin = 5;
const int motor6_dir_pin = 6;
const int motor6_step_pin = 7;

int pos_pinza = 0;

// Variables para guardar string
String bufferdatos = "";
int valores[7];

// Crear objetos AccelStepper para cada motor
AccelStepper motor1(AccelStepper::DRIVER, motor1_step_pin, motor1_dir_pin);
AccelStepper motor2(AccelStepper::DRIVER, motor2_step_pin, motor2_dir_pin);
AccelStepper motor3(AccelStepper::DRIVER, motor3_step_pin, motor3_dir_pin);
AccelStepper motor4(AccelStepper::DRIVER, motor4_step_pin, motor4_dir_pin);
AccelStepper motor5(AccelStepper::DRIVER, motor5_step_pin, motor5_dir_pin);
AccelStepper motor6(AccelStepper::DRIVER, motor6_step_pin, motor6_dir_pin);

void setup() {

  pinza1.attach(11);
  // Configurar los pines como salidas
  pinMode(motor1_en_pin, OUTPUT);
  pinMode(motor1_dir_pin, OUTPUT);
  pinMode(motor1_step_pin, OUTPUT);

  pinMode(motor2_en_pin, OUTPUT);
  pinMode(motor2_dir_pin, OUTPUT);
  pinMode(motor2_step_pin, OUTPUT);
  
  pinMode(motor3_en_pin, OUTPUT);
  pinMode(motor3_dir_pin, OUTPUT);
  pinMode(motor3_step_pin, OUTPUT);

  pinMode(motor4_en_pin, OUTPUT);
  pinMode(motor4_dir_pin, OUTPUT);
  pinMode(motor4_step_pin, OUTPUT);
  
  pinMode(motor5_en_pin, OUTPUT);
  pinMode(motor5_dir_pin, OUTPUT);
  pinMode(motor5_step_pin, OUTPUT);

  pinMode(motor6_en_pin, OUTPUT);
  pinMode(motor6_dir_pin, OUTPUT);
  pinMode(motor6_step_pin, OUTPUT);

  // Configurar los motores
  motor1.setMaxSpeed(1000);
  motor1.setAcceleration(100);
  
  motor2.setMaxSpeed(1000);
  motor2.setAcceleration(100);
 
  motor3.setMaxSpeed(1000);
  motor3.setAcceleration(100);

  motor4.setMaxSpeed(1000);
  motor4.setAcceleration(100);
  
  motor5.setMaxSpeed(1000);
  motor5.setAcceleration(100);
  
  motor6.setMaxSpeed(1000);
  motor6.setAcceleration(100);

  // Iniciar la comunicación serial
  Serial.begin(9600);
  
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    /* Hay uno o más caracteres a leer en la serial.*/
    int car = Serial.read();
    /* Agregamos cada caracter al string*/
    if (car == '\n') {
     /* "/n" tenemos un paquete completo
     se limpia el string de las "," y sictuado de cada valor*/


        int index = 0;
        while (bufferdatos.indexOf(',') >= 0) {
          String subcadena = bufferdatos.substring(0, bufferdatos.indexOf(','));
          valores[index] = subcadena.toInt();
          bufferdatos = bufferdatos.substring(bufferdatos.indexOf(',') + 1);
          index++;
        }
        
        // El último valor está después de la última coma
        String subcadena = bufferdatos.substring(0, bufferdatos.indexOf('\n'));
        valores[index] = subcadena.toInt();
      
      motor1.moveTo(valores[0]);
      motor2.moveTo(valores[1]);
      motor3.moveTo(valores[2]);
      motor4.moveTo(valores[3]);
      motor5.moveTo(valores[4]);
      motor6.moveTo(valores[5]);

      if (valores[0] > 300)digitalWrite(LED_BUILTIN,HIGH);
      if (valores[1] > 250)digitalWrite(LED_BUILTIN,LOW);
          if(valores[6]>1){
              for (pos_pinza; pos_pinza <= valores[6]; pos_pinza ++){
                pinza1.write(pos_pinza);                                     
                delay(10);
              }
          }
          if(valores[6]<0){
              for (valores[6]; valores[6] >= pos_pinza; pos_pinza --){
                pinza1.write(pos_pinza);
                delay(10);                                      
              }   
          }
      
    while(motor1.distanceToGo() != 0 || motor2.distanceToGo() != 0 || motor3.distanceToGo() != 0 || motor4.distanceToGo() != 0 || motor5.distanceToGo() != 0 ||motor6.distanceToGo() != 0){
          motor1.run(); 
          motor2.run();
          motor3.run();
          motor4.run();
          motor5.run();
          motor6.run();          
        }
      bufferdatos = "";  // Limpiar el buffer una vez procesado.
      
    } else {
      /*Acumular los caracteres leídos.*/
      bufferdatos += (char) car;
    }
  }
}
