from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)

# recommended for auto-disabling motors on shutdown!


def turnOffMotors():
    mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)


atexit.register(turnOffMotors)

# DC motor test!
rightMotor = mh.getMotor(1)
leftMotor = mh.getMotor(2)

# set the speed to start, from 0 (off) to 255 (max speed)
rightMotor.setSpeed(255)
leftMotor.setSpeed(255)
rightMotor.run(Raspi_MotorHAT.FORWARD)
leftMotor.run(Raspi_MotorHAT.FORWARD)
# turn on motor
rightMotor.run(Raspi_MotorHAT.RELEASE)
leftMotor.run(Raspi_MotorHAT.RELEASE)

while (True):
    print("Forward! ")
    rightMotor.run(Raspi_MotorHAT.FORWARD)
    leftMotor.run(Raspi_MotorHAT.FORWARD)

    print("\tSpeed up...")
    for i in range(255):
        rightMotor.setSpeed(i)
        leftMotor.setSpeed(i)
        time.sleep(0.01)

    time.sleep(5)

    print("\tSlow down...")
    for i in reversed(list(range(255))):
        rightMotor.setSpeed(i)
        leftMotor.setSpeed(i)
        time.sleep(0.01)

    time.sleep(5)

    print("Backward! ")
    rightMotor.run(Raspi_MotorHAT.BACKWARD)
    leftMotor.run(Raspi_MotorHAT.BACKWARD)

    print("\tSpeed up...")
    for i in range(255):
        rightMotor.setSpeed(i)
        leftMotor.setSpeed(i)
        time.sleep(0.01)

    time.sleep(5)

    print("\tSlow down...")
    for i in reversed(list(range(255))):
        rightMotor.setSpeed(i)
        leftMotor.setSpeed(i)
        time.sleep(0.01)

    time.sleep(5)

    print("Release")
    rightMotor.run(Raspi_MotorHAT.RELEASE)
    leftMotor.run(Raspi_MotorHAT.RELEASE)
    time.sleep(10.0)
