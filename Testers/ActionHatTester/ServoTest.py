from Raspi_PWM_Servo_Driver import PWM
import time

# Initialise the PWM device using the default address
pwm = PWM(0x6F)




# Configure min and max servo pulse lengths
SERVOMIN = 150  # Min pulse length, us (tick 184/4096)
SERVOMAX = 550  # Max pulse length, us  (tick 430/4096)
servoMid = SERVOMAX - ((SERVOMAX-SERVOMIN)/2) # Midpoint pulse length, us
FREQUENCY = 50 # frequency length, Hz

pwm.setPWMFreq(FREQUENCY) # Set frequency

def map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

def pulseWidthCal(inputAngle):
      pulse_wide = map(inputAngle, 0, 180, SERVOMIN, SERVOMAX)
      print("Current pulse is:" , pulse_wide)
      return pulse_wide

print('Moving servo on channel 0, press Ctrl-C to quit...')
while (True):
      print("Going to servo 0 Degree...")
      pwm.setPWM(0, 0, pulseWidthCal(0))
      time.sleep(5)

      print("Going to servo 90 Degree...")
      pwm.setPWM(0, 0, pulseWidthCal(90))
      time.sleep(5)

      print("Going to servo 180 Degree...")
      pwm.setPWM(0, 0, pulseWidthCal(180))
      time.sleep(5)
