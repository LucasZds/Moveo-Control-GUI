#include <AccelStepper.h>

// Definir pines para los motores
const int motor1_dir_pin = 2;
const int motor1_step_pin = 3;
const int motor2_dir_pin = 4;
const int motor2_step_pin = 5;
const int motor3_dir_pin = 6;
const int motor3_step_pin = 7;
const int motor4_dir_pin = 8;
const int motor4_step_pin = 9;
const int motor5_dir_pin = 10;
const int motor5_step_pin = 11;
const int motor6_dir_pin = 12;
const int motor6_step_pin = 13;

// Crear objetos AccelStepper para cada motor
AccelStepper motor1(AccelStepper::DRIVER, motor1_step_pin, motor1_dir_pin);
AccelStepper motor2(AccelStepper::DRIVER, motor2_step_pin, motor2_dir_pin);
AccelStepper motor3(AccelStepper::DRIVER, motor3_step_pin, motor3_dir_pin);
AccelStepper motor4(AccelStepper::DRIVER, motor4_step_pin, motor4_dir_pin);
AccelStepper motor5(AccelStepper::DRIVER, motor5_step_pin, motor5_dir_pin);
AccelStepper motor6(AccelStepper::DRIVER, motor6_step_pin, motor6_dir_pin);

void setup() {
  // Configurar los pines como salidas
  pinMode(motor1_dir_pin, OUTPUT);
  pinMode(motor1_step_pin, OUTPUT);
  pinMode(motor2_dir_pin, OUTPUT);
  pinMode(motor2_step_pin, OUTPUT);
  pinMode(motor3_dir_pin, OUTPUT);
  pinMode(motor3_step_pin, OUTPUT);
  pinMode(motor4_dir_pin, OUTPUT);
  pinMode(motor4_step_pin, OUTPUT);
  pinMode(motor5_dir_pin, OUTPUT);
  pinMode(motor5_step_pin, OUTPUT);
  pinMode(motor6_dir_pin, OUTPUT);
  pinMode(motor6_step_pin, OUTPUT);

  // Configurar los motores
  motor1.setMaxSpeed(1000);
  motor1.setAcceleration(500);
  motor2.setMaxSpeed(1000);
  motor2.setAcceleration(500);
  motor3.setMaxSpeed(1000);
  motor3.setAcceleration(500);
  motor4.setMaxSpeed(1000);
  motor4.setAcceleration(500);
  motor5.setMaxSpeed(1000);
  motor5.setAcceleration(500);
  motor6.setMaxSpeed(1000);
  motor6.setAcceleration(500);

  // Iniciar la comunicación serial
  Serial.begin(9600);
}

void loop() {
  // Esperar a recibir datos por el puerto serial
  while (!Serial.available()) {}

    // Leer los datos recibidos
    byte data[2];
    Serial.readBytes(data, 2);
    // Interpretar los bits recibidos

//"0-0 0-0 0-0 0-0 0-0 0-0" lectura de serial
//motor6_enable-motor6_dir motor5_enable-motor5_dir motor4_enable-motor4_dir motor3_enable-motor3_dir motor2_enable-motor2_dir motor1_enable-motor1_dir 
    
    int motor1_dir = (data[0] & 0b00000001) ? HIGH : LOW;
    int motor1_enable = (data[0] & 0b00000010) ? HIGH : LOW;
    
    int motor2_dir = (data[0] & 0b00000100) ? HIGH : LOW;
    int motor2_enable = (data[0] & 0b00001000) ? HIGH : LOW;
    
    int motor3_dir = (data[0] & 0b00010000) ? HIGH : LOW;
    int motor3_enable = (data[0] & 0b00100000) ? HIGH : LOW;
    
    int motor4_dir = (data[1] & 0b00000001) ? HIGH : LOW;
    int motor4_enable = (data[1] & 0b00000010) ? HIGH : LOW;
    
    int motor5_dir = (data[1] & 0b00000100) ? HIGH : LOW;
    int motor5_enable = (data[1] & 0b00001000) ? HIGH : LOW;
    
    int motor6_dir = (data[1] & 0b00010000) ? HIGH : LOW;
    int motor6_enable = (data[1] & 0b00100000) ? HIGH : LOW;

  // Controlar los motores correspondientes
  motor1.setEnablePin(motor1_enable);
  motor1_dir -= 2 * (motor1_dir == LOW) - 1;
  motor1.move(motor1_dir);
  motor1.run();

  motor2.setEnablePin(motor2_enable);
  motor2_dir -= 2 * (motor2_dir == LOW) - 1;
  motor2.move(motor2_dir);
  motor2.run();

  motor3.setEnablePin(motor3_enable);
  motor3_dir -= 2 * (motor3_dir == LOW) - 1;
  motor3.move(motor3_dir);
  motor3.run();

  motor4.setEnablePin(motor4_enable);
  motor4_dir -= 2 * (motor4_dir == LOW) - 1;
  motor4.move(motor4_dir);
  motor4.run();

  motor5.setEnablePin(motor5_enable);
  motor5_dir -= 2 * (motor5_dir == LOW) - 1;
  motor5.move(motor5_dir);
  motor5.run();

  motor6.setEnablePin(motor6_enable);
  motor6_dir -= 2 * (motor6_dir == LOW) - 1;
  motor6.move(motor6_dir);
  motor6.run();
}
