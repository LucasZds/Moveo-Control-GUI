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
  motor1.setMaxSpeed(500);
  motor1.setAcceleration(60);
  
  motor2.setMaxSpeed(500);
  motor2.setAcceleration(60);
 
  motor3.setMaxSpeed(500);
  motor3.setAcceleration(60);

  motor4.setMaxSpeed(500);
  motor4.setAcceleration(60);
  
  motor5.setMaxSpeed(500);
  motor5.setAcceleration(60);
  
  motor6.setMaxSpeed(500);
  motor6.setAcceleration(60);

 /* // Habilitamos los motores
  digitalWrite(motor1_en_pin, LOW);
  digitalWrite(motor2_en_pin, LOW);
  digitalWrite(motor3_en_pin, LOW);
  digitalWrite(motor4_en_pin, LOW);
  digitalWrite(motor5_en_pin, LOW);
  digitalWrite(motor6_en_pin, LOW);
  */
  // Iniciar la comunicación serial
  Serial.begin(9600);
}

void loop() {
char input = Serial.read();
if (input == '0') {
  Serial.println("Valor 0");
 delay(2000);
 for (int i =0 ; i < 6;i++) {
    motor1.moveTo(160);
    motor5.moveTo(400);
    motor6.moveTo(80);
    motor3.moveTo(50);
    motor2.moveTo(50);
    motor4.moveTo(-20);
    for (int pos = 0; pos <= 180; pos ++){
      pinza1.write(pos);                                     
      delay(10);
   }
    while(motor1.distanceToGo() != 0 || motor2.distanceToGo() != 0 || motor3.distanceToGo() != 0 || motor4.distanceToGo() != 0 || motor5.distanceToGo() != 0 ||motor6.distanceToGo() != 0){
        motor1.run(); 
        motor2.run();
        motor3.run();
        motor4.run();
        motor5.run();
        motor6.run();          
        }
        
    motor1.moveTo(-160);
    motor5.moveTo(-400);
    motor6.moveTo(-80);
    motor3.moveTo(-50);
    motor2.moveTo(-50);
    motor4.moveTo(20);
    for (int pos = 80; pos >= 0; pos --){
      pinza1.write(pos);
      delay(10);                                     
   }
    if (i==5)break;
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
    // Si el carácter es '1', giramos el motor en el otro sentido MULTIPLES MOTORES A LA VEZ
    else if (input == '1') {

for (int pos = 0; pos <= 180; pos ++){
      pinza1.write(pos);                                     
      delay(10);
   }

 for (int pos = 180; pos >= 0; pos --){
      pinza1.write(pos);
      delay(10);                                     
   } 
      Serial.println("Valor 1");
  }













  
  /*  

   // Leemos el carácter que el usuario escriba por consola
  char input = Serial.read();
delay(3000);
  // Si se ha recibido algún carácter
  if (input != -1) {
    // Si el carácter es '0', giramos el motor en un sentido DE A UN MOTOR
    if (input == '0') {
      
      
    }
    // Si el carácter es '1', giramos el motor en el otro sentido MULTIPLES MOTORES A LA VEZ
    else if (input == '1') {
      for(int i=0;i<8;i++) {
        Serial.println("adelante");
        stepper4.moveTo(80); // Movemos el motor 3
        stepper1.moveTo(80); // Movemos el motor 3
          while(stepper4.distanceToGo() != 0){
            stepper4.run(); // Esperamos a que el motor 2 llegue a la posición deseada
            stepper1.run(); // Esperamos a que el motor 2 llegue a la posición deseada
    }
    Serial.println("atras");
      stepper4.moveTo(-80); // Movemos el motor 3
      stepper1.moveTo(-80); // Movemos el motor 3
          while(stepper4.distanceToGo() != 0){
            stepper4.run(); // Esperamos a que el motor 2 llegue a la posición deseada
            stepper1.run(); // Esperamos a que el motor 2 llegue a la posición deseada
         }
       }
    }
  }
  
  
/*  
  
  // Esperar a recibir datos por el puerto serial
  while (Serial.available() >= 2) {}

    // Leer los datos recibidos
    uint16_t cadena; 
    uint8_t primerbyte = Serial.read(); // Leer el byte menos significativo
    uint8_t segundobyte = Serial.read(); // Leer el byte más significativo
    cadena = (high_byte << 8) | low_byte;
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
  if (motor1_enable == '1'){
    motor1_dir -= 2 * (motor1_dir == '1') - 1;
    int paso = motor1_dir * 5;
    motor1.move(paso);
    motor1.runToPosition();
  }
  

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
  */
}
