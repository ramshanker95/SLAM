# import the opencv library
import cv2
import os

def get_img():
    lf = "D:\\photos\\Camera\\"
    pth = os.listdir("D:\\photos\\Camera")
    while True:
        # for i in pth:
            # yield cv2.imread(f"{lf}{i}")
        yield cv2.imread(f"photo.png")


# while(True):
for img in get_img():
    # img = get_img() # cv2.imread("map1.png")
	# Display the resulting frame
    try:
        cv2.imshow('frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except:
        pass

# After the loop release the cap object
# vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
