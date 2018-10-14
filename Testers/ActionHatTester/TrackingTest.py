from Raspi_PWM_Servo_Driver import PWM
import time

pwm = PWM(0x6F) #Hat setting, do not change!!!
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



while (True):
      print("Moving Pan....")
      pwm.setPWM(PAN_CHANNEL, 0, 300)
      time.sleep(2)

      print("Moving Pan....")
      pwm.setPWM(PAN_CHANNEL, 0, 400)
      time.sleep(5)


      print("Moving tilt....")
      pwm.setPWM(PAN_CHANNEL, 0, 300)
      time.sleep(2)

      print("Moving tilt....")
      pwm.setPWM(PAN_CHANNEL, 0, 400)
      time.sleep(5)