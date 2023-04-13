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
const int motor4_step_pin = A8;

const int motor5_en_pin = 8;
const int motor5_dir_pin = 9;
const int motor5_step_pin = 10;

const int motor6_en_pin = 5;
const int motor6_dir_pin = 6;
const int motor6_step_pin = 7;

// Variables para guardar string
char datos[50]; // buffer para almacenar los datos recibidos
int pasos_motor1, sentido_motor1, enable_motor1;
int pasos_motor2, sentido_motor2, enable_motor2;
int pasos_motor3, sentido_motor3, enable_motor3;
int pasos_motor4, sentido_motor4, enable_motor4;
int pasos_motor5, sentido_motor5, enable_motor5;
int pasos_motor6, sentido_motor6, enable_motor6;
int pasos_pinza, sentido_pinza, enable_pinza, pos_pinza;

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
}

void loop() {
  if (Serial.available() > 0) {
      // leer los datos recibidos en el buffer
      int i = 0;
      while (Serial.available() > 0) {
        datos[i] = Serial.read();
        i++;
      }
      datos[i] = '\0'; // agregar el terminador de string

      // dividir los datos en substrings separados por comas
      char *ptr = strtok(datos, ",");
      pasos_motor1 = atoi(ptr); ptr = strtok(NULL, ","); sentido_motor1 = atoi(ptr); ptr = strtok(NULL, ","); enable_motor1 = atoi(ptr); ptr = strtok(NULL, ",");
      pasos_motor2 = atoi(ptr); ptr = strtok(NULL, ","); sentido_motor2 = atoi(ptr); ptr = strtok(NULL, ","); enable_motor2 = atoi(ptr); ptr = strtok(NULL, ",");
      pasos_motor3 = atoi(ptr); ptr = strtok(NULL, ","); sentido_motor3 = atoi(ptr); ptr = strtok(NULL, ","); enable_motor3 = atoi(ptr); ptr = strtok(NULL, ",");
      pasos_motor4 = atoi(ptr); ptr = strtok(NULL, ","); sentido_motor4 = atoi(ptr); ptr = strtok(NULL, ","); enable_motor4 = atoi(ptr); ptr = strtok(NULL, ",");
      pasos_motor5 = atoi(ptr); ptr = strtok(NULL, ","); sentido_motor5 = atoi(ptr); ptr = strtok(NULL, ","); enable_motor5 = atoi(ptr); ptr = strtok(NULL, ",");
      pasos_motor6 = atoi(ptr); ptr = strtok(NULL, ","); sentido_motor6 = atoi(ptr); ptr = strtok(NULL, ","); enable_motor6 = atoi(ptr); ptr = strtok(NULL, ",");
      pasos_pinza = atoi(ptr); ptr = strtok(NULL, ","); sentido_pinza = atoi(ptr); ptr = strtok(NULL, ","); enable_pinza = atoi(ptr);

      motor1.moveTo(pasos_motor1);
      motor2.moveTo(pasos_motor2);
      motor3.moveTo(pasos_motor3);
      motor4.moveTo(pasos_motor4);
      motor5.moveTo(pasos_motor5);
      motor6.moveTo(pasos_motor6);

      if (enable_pinza==1){
          if(sentido_pinza==1){
              for (pos_pinza; pos_pinza <= pasos_pinza; pos_pinza ++){
                pinza1.write(pos_pinza);                                     
                delay(10);
              }
          }
          if(sentido_pinza==0){
              for (pasos_pinza; pasos_pinza >= pos_pinza; pos_pinza --){
                pinza1.write(pos_pinza);
                delay(10);                                      
              }   
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
  }
}
