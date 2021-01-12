import cv2 as cv
import numpy as np
import os
from time import sleep

if __name__ == "__main__":
    cap = cv.VideoCapture('/home/thomas/smashAI/dolphin/Build/Binaries/Frames/Frames/framedump0.avi')
    filename = '/home/thomas/smashAI/dolphin/Build/Binaries/pad_0.txt'
    with open(filename) as f:
        content = f.readlines()
    ret = True
    i = 0
    content = [x.strip() for x in content]
    # content = content[2300:]
    # content = content[500:-500:2]
    ret, frame = cap.read()

    frames = 0

    while ret:
        buttons = content[i]
        frames += 1
        i += 1
        # # cv.imshow("name", frame)
        # key = cv.waitKey(1) & 0xFF
        # # if the `q` key was pressed, break from the loop
        # if key == ord("k"):
        #     cap.release()
        #     cv.destroyAllWindows()
        #     break
        # if key == ord("p"):
        #     sleep(10)
        # if key == ord("q"):
        #     cv.destroyAllWindows()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        print(buttons)

        ret, frame = cap.read()
    for thing in content[i:]:
        print(f"{i}{thing}")
    print(f"Frame numbers = {frames}")
    print(len(content[i:]))
    print(i)
    print(len(content))
    print(len(content) - i)
