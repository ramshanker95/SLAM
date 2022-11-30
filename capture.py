# import the opencv library
import cv2
from time import sleep


# define a video capture object
vid = cv2.VideoCapture(0)

while(True):
	
	# Capture the video frame
	# by frame
    
    ret, frame = vid.read()
    cv2.imwrite("photo.png", frame)

	# Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    sleep(0.1)

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
