import cv2
import sys
import imutils
import time

import ServoControl as servo
servo.reset()


xPosition = 0.0
yPosition = 0.0

# * Video frame re-scale function. Takes in a frame and re-scale that.
# Can be replaced by imutils.resize*()
def rescale_frame(frame, percent):
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


 # * Start of the tracker selection:
tracker_types = ['BOOSTING', 'MIL', 'KCF',
                 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE']
tracker_type = tracker_types[6]  # ! Currently set for coding
if tracker_type == 'BOOSTING':
    tracker = cv2.TrackerBoosting_create()
if tracker_type == 'MIL':
    tracker = cv2.TrackerMIL_create()
if tracker_type == 'KCF':
    tracker = cv2.TrackerKCF_create()
if tracker_type == 'TLD':
    tracker = cv2.TrackerTLD_create()
if tracker_type == 'MEDIANFLOW':
    tracker = cv2.TrackerMedianFlow_create()
if tracker_type == 'GOTURN':
    tracker = cv2.TrackerGOTURN_create()
if tracker_type == 'MOSSE':
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
