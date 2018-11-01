from Raspi_PWM_Servo_Driver import PWM
import time

pwm = PWM(0x6F) #Hat setting, do not change!!!
pwm.setPWMFreq(50) # Set frequency to 50Hz, mandatory!!!
# Following are magic numbers, Do not change!!!
G_FREQUENCY = 50
#Pan setting
PAN_CHANNEL = 0
SERVOMIN_PAN = 150 #Pan Minimal pulse
SERVOMAX_PAN = 550 #Pan Max pulse
SERVONEUTRAL_PAN = 350
#Tilt Setting
TILT_CHANNEL = 1
SERVOMIN_TILT = 150
SERVOMAX_TILT = 400
SERVONEUTRAL_TILT = 200 

pwm.setPWM(PAN_CHANNEL,0,SERVONEUTRAL_PAN)
pwm.setPWM(TILT_CHANNEL,0,SERVONEUTRAL_TILT)
print("Reset Complete, wait 5 seconds....")
time.sleep(5)


while (True):
    i = 300
    while (i<400):
        print("Moving Pan....")
        pwm.setPWM(PAN_CHANNEL, 0, i)
        time.sleep(0.5)
        i = i + 1
    
    while (i>300):
        print("Moving Pan....")
        pwm.setPWM(PAN_CHANNEL, 0, i)
        time.sleep(0.5)
        i = i - 1

