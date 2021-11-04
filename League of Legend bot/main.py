import cv2 as cv
import os
from time import time
from capture import WindowCapture
from window_vision import Vision

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    vision = Vision("images\league_popup_accept.jpeg")
    window_capture = WindowCapture("League of Legends")

    # Get list of windows currently open on the machine
    # WindowCapture.get_list_window_names()
    # exit()

    loop_time = time()
    while True:
        screenshot = window_capture.get_screenshot()
        point = vision.find(screenshot, output_name="accept", threshold=0.8, debug_mode="point")
        if point:
            point = window_capture.get_screen_position(point[0])
            vision.click(point[0], point[1])

        print('FPS: {}'.format(1 / (time() - loop_time)))
        loop_time = time()

        if cv.waitKey(1) == 27:
            cv.destroyAllWindows()
            break


if __name__ == '__main__':
    main()
