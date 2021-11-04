import cv2 as cv
import numpy as np
import pyautogui
import time


class Vision:
    # properties
    needle_img = None
    w = 0
    h = 0
    method = None

    def __init__(self, neddle_img_path, method=cv.TM_CCOEFF_NORMED):
        self.needle_img = cv.imread(
            neddle_img_path, cv.IMREAD_UNCHANGED)
        self.w = self.needle_img.shape[1]
        self.h = self.needle_img.shape[0]
        self.method = method


    def find(self, main_image, output_name="accept", threshold=0.8, debug_mode=None):
        result = cv.matchTemplate(main_image, self.needle_img, self.method)

        # Get the best match location and it's value
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        points = []
        if max_val > threshold:
            x_loc = max_loc[0]
            y_loc = max_loc[1]

            top_left = (x_loc, y_loc)
            bottom_right = (x_loc + self.w, y_loc + self.h)

            center_x = x_loc + int(self.w/2)
            center_y = y_loc + int(self.h/2)

            points.append((center_x, center_y))

            if debug_mode == "rectangle":
                cv.rectangle(main_image, top_left, bottom_right,
                            color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
            elif debug_mode == "point":
                cv.drawMarker(main_image, (center_x, center_y),
                            (0, 255, 0), thickness=2, markerType=cv.MARKER_CROSS)

            if debug_mode:
                cv.imshow('Matches', main_image)
            
            return points
        else:
            print("Not Found!")
    
    def click(self, x, y):
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print("Click!")
        time.sleep(5)
