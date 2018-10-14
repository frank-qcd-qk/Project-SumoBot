from Raspi_PWM_Servo_Driver import PWM
# Following are magic numbers, Do not change!!!
G_FREQUENCY = 50
#Pan setting
PAN_CHANNEL = 0
SERVOMIN_PAN = 150 #Pan Minimal pulse
SERVOMAX_PAN = 550 #Pan Max pulse
SERVONEUTRAL_PAN = 300


def resetPan():
    pwm.setPWM(PAN_CHANNEL,0,SERVONEUTRAL_PAN)

def movePan(desiredPulse):
    pwm.setPWM(PAN_CHANNEL,0,desiredPulse)
