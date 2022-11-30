import cv2
import numpy as np

def get_grid_map():
    gr =np.int16(cv2.imread("map.png", 0)/255) 
    # print(gr)
    return gr.tolist()

if __name__ == "__main__":
    get_grid_map()