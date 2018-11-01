import time
import atexit
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor  # DC motor driver
from Raspi_PWM_Servo_Driver import PWM  # Servo Control


#! Global Variables and magic numbers
SERVOMIN = 150  # Min pulse length, us (tick 184/4096)
SERVOMAX = 550  # Max pulse length, us  (tick 430/4096)
servoMid = SERVOMAX - ((SERVOMAX-SERVOMIN)/2)  # Midpoint pulse length, us
FREQUENCY = 1600  # frequency length, Hz


#! Initialization
servo = PWM(0x6F)
servo.setPWMFreq(FREQUENCY)  # Set frequency
motorControl = Raspi_MotorHAT(addr=0x6f)


def turnOffMotors():
    motorControl.getMotor(1).run(Raspi_MotorHAT.RELEASE)
    motorControl.getMotor(2).run(Raspi_MotorHAT.RELEASE)
    motorControl.getMotor(3).run(Raspi_MotorHAT.RELEASE)
    motorControl.getMotor(4).run(Raspi_MotorHAT.RELEASE)

def map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)


def pulseWidthCal(inputAngle):
    pulse_wide = map(inputAngle, 0, 180, SERVOMIN, SERVOMAX)
    print("Current pulse is:", pulse_wide)
    return pulse_wide

atexit.register(turnOffMotors)

# DC motor test!
rightMotor = motorControl.getMotor(1)
leftMotor = motorControl.getMotor(2)

# set the speed to start, from 0 (off) to 255 (max speed)
rightMotor.setSpeed(255)
leftMotor.setSpeed(255)
rightMotor.run(Raspi_MotorHAT.FORWARD)
leftMotor.run(Raspi_MotorHAT.FORWARD)
# turn on motor
rightMotor.run(Raspi_MotorHAT.RELEASE)
leftMotor.run(Raspi_MotorHAT.RELEASE)

print('Initialization Complete...')

while (1>0):
    print("Switch to Forward! ")
    rightMotor.run(Raspi_MotorHAT.FORWARD)
    leftMotor.run(Raspi_MotorHAT.FORWARD)

    print("\tSpeed up...")
    for i in range(255):
        rightMotor.setSpeed(i)
        leftMotor.setSpeed(i)
        time.sleep(0.01)

    print("\tSpeed up complete...")
    time.sleep(20)

    print("Going to servo 0 Degree...")
    servo.setPWM(0, 0, pulseWidthCal(0))
    time.sleep(5)

    print("Going to servo 90 Degree...")
    servo.setPWM(0, 0, pulseWidthCal(90))
    time.sleep(5)

    print("Going to servo 180 Degree...")
    servo.setPWM(0, 0, pulseWidthCal(180))
    time.sleep(5)

    print("\tSlow down...")
    for i in reversed(list(range(255))):
        rightMotor.setSpeed(i)
        leftMotor.setSpeed(i)
        time.sleep(0.01)

    time.sleep(1)

    print("Switch to Backward! ")
    rightMotor.run(Raspi_MotorHAT.BACKWARD)
    leftMotor.run(Raspi_MotorHAT.BACKWARD)

    print("\tSpeed up...")
    for i in range(255):
        rightMotor.setSpeed(i)
        leftMotor.setSpeed(i)
        time.sleep(0.01)

    print("\tSpeed up complete...")
    time.sleep(20)

    print("Going to servo 0 Degree...")
    servo.setPWM(0, 0, pulseWidthCal(0))
    time.sleep(5)

    print("Going to servo 90 Degree...")
    servo.setPWM(0, 0, pulseWidthCal(90))
    time.sleep(5)

    print("Going to servo 180 Degree...")
    servo.setPWM(0, 0, pulseWidthCal(180))
    time.sleep(5)

    print("\tSlow down...")
    for i in reversed(list(range(255))):
        rightMotor.setSpeed(i)
        leftMotor.setSpeed(i)
        time.sleep(0.01)

    time.sleep(1)

    print("Reset!")
    rightMotor.run(Raspi_MotorHAT.RELEASE)
    leftMotor.run(Raspi_MotorHAT.RELEASE)
    time.sleep(5.0)
