from Raspi_PWM_Servo_Driver import PWM
import time

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x6F)
# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length /= 50       # 50 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length /= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse /= pulse_length
    pwm.setPWM(channel, 0, pulse)

# Set frequency to 50hz, good for servos.
pwm.setPWMFreq(50)

print('Moving servo on channel 0, press Ctrl-C to quit...')
i = 0;
while (i<2):
    # Move servo on channel O between extremes.
    pwm.setPWM(0, 0, servo_min)
    time.sleep(1)
    pwm.setPWM(0, 0, servo_max)
    time.sleep(1)
    print (i)
    i+=1

pwm.setPWM(0,0,350)