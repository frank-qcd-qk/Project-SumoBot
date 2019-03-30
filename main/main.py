import cv2
import sys
import imutils
import time
from Raspi_PWM_Servo_Driver import PWM

#! Global Variables



#! Robot Initialization
#* Motor initialization







pwm = PWM(0x6F) #Hat setting, do not change!!!
pwm.setPWMFreq(50) # Set frequency to 50Hz, mandatory!!!
# Following are magic numbers, Do not change!!!
G_FREQUENCY = 50
#Pan setting
PAN_CHANNEL = 0
SERVOMIN_PAN = 150 #Pan Minimal pulse
SERVOMup1AX_PAN = 550 #Pan Max pulse
SERVONEUTRAL_PAN = 350
#Tilt Setting
TILT_CHANNEL = 1
SERVOMIN_TILT = 150
SERVOMAX_TILT = 400
SERVONEUTRAL_TILT = 200 



def map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)


# Video frame re-scale function. Takes in a frame and re-scale that.
def rescale_frame(frame, percent):
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)



def reset():
    pwm.setPWM(PAN_CHANNEL,0,SERVONEUTRAL_PAN)
    pwm.setPWM(TILT_CHANNEL,0,SERVONEUTRAL_TILT)

def movePan(desiredPulse):
    pwm.setPWM(PAN_CHANNEL,0,desiredPulse)

servo.reset()

xPosition = 0.0
yPosition = 0.0


tracker = cv2.TrackerMOSSE_create() 

# * Read video and test video validity
video = cv2.VideoCapture(0)
if not video.isOpened():
    print("Could not open video!!!")
    sys.exit()

# * Read first frame and test readability
ok, frame = video.read()
if not ok:
    print('Cannot read video file')
    sys.exit()

#! Down samples frame size for complicated tracker.
#! Leave out for mosse tracker, always use full resolution
# Choose one of the downsample methods:
# frame = rescale_frame(frame, percent=100) #Relative downsample
# frame = imutils.resize(frame, width= 320) #Absolute downsample

# * ROI Selection section, not implemented yet...
# TODO: Change this in the future to edge readout
bbox = cv2.selectROI(frame, False)
# Initialize tracker with first frame and bounding box
ok = tracker.init(frame, bbox)

# *Store the initial xposition and y position
xPosition = bbox[0]
yPosition = bbox[1]

# * Main Program loop
while (1 > 0):
    # * Read a new frame, and test frame
    grabbed, frame = video.read()
    if not grabbed:
        break

    #! Down samples frame size for complicated tracker.
    #! Leave out for mosse tracker, always use full resolution
    # Choose one of the downsample methods:
    #  frame = rescale_frame(frame, percent=100) #Relative downsample
    # frame = imutils.resize(frame, width= 320) #Absolute downsample

    # * DEBUG: Start timer
    timer = cv2.getTickCount()

    # Update tracker and prints out the bounding box
    track_status, bbox = tracker.update(frame)
    print("DEBUG: Current bounding box array is:", bbox)

    # ! Debug section for printing movement
    # TODO: Add corresponding action in the future
    if ((bbox[0] - xPosition) > 0):
        print("Moving RIght! Current X Position: ",
              bbox[0], " Last X position", xPosition)
    elif ((bbox[0] - xPosition) < 0):
        print("Moving Left! Current X Position: ",
              bbox[0], " Last X position", xPosition)
    else:
        print("No Movement! Current X Position: ",
            bbox[0], " Last X position", xPosition)
    xPosition = bbox[0]

    if ((bbox[1] - yPosition) > 0):
        print("Moving Closer! Current Y Position: ",
              bbox[1], " Last Y position", yPosition)
    elif ((bbox[1] - yPosition) < 0):
        print("Moving Farther! Current Y Position: ",
              bbox[1], " Last Y position", xPosition)
    else:
        print("No Movement! Current Y Position: ",
              bbox[1], " Last Y position", yPosition)
    yPosition = bbox[1]






    # * DEBUG: Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    # Draw bounding box
    if track_status:
        # Tracking success
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
    else:
        # Tracking failure
        cv2.putText(frame, "Tracking failure detected", (100, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Display FPS on frame
    cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

    # Display result
    cv2.imshow("Tracking", frame)

    # Exit if ESC pressed
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
