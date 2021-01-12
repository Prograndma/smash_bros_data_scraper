import numpy as np
import PIL as PIL
from time import sleep
import mss


if __name__ == "__main__":

    sleep(5)
    i = 785
    with mss.mss() as screen_cap:
        # Use the 1st monitor
        monitor = screen_cap.monitors[1]

        # Capture a bbox using percent values
        left = monitor["left"] + monitor["width"] * 20 // 100  # 5% from the left
        top = monitor["top"] + monitor["height"] * 7 // 100  # 5% from the top
        right = left + monitor["width"] * 80 // 100
        lower = top + monitor["height"] * 93 // 100
        bbox = (left, top, right, lower)
        while True:
            im = screen_cap.grab(bbox)  # type: ignore
            # array = np.array(im)
            # array = np.flip(array[:, :, :3], 2)

            # y_array = array[TOP:BOTTOM, y_start:y_end]
            # print(y_array)
            # zero = array[TOP:BOTTOM, a_start:a_end]
            # one = array[TOP:BOTTOM, b_start:b_end]
            # array[TOP:BOTTOM, b_start:b_end] = [255, 0, 0]

            # array = array[500:600, 500:600, :]
            # print(array.shape)

            # Save it!
            i += 1
            mss.tools.to_png(im.rgb, im.size, output=f"frames/screenshot{i}.png")

        # im = PIL.Image.fromarray(array)
        # im.show()

        # im = PIL.Image.fromarray(y_array)
        # im.show()

    # while True:
    #
    #     screen_red = np.array(ImageGrab.grab(bbox=game_cords))[:, :, 1]
    #
    #     if not up:
    #         up = check_up_press(screen_red)
    #     else:
    #         up_counter += 1
    #         if up_counter > normal_limit:
    #             up = False
    #             up_counter = 0
    #     if not right:
    #         right = check_right_press(screen_red)
    #     else:
    #         right_counter += 1
    #         if right_counter > normal_limit:
    #             right = False
    #             right_counter = 0
    #     if not down:
    #         down = check_down_press(screen_red)
    #     else:
    #         down_counter += 1
    #         if down_counter > normal_limit:
    #             down = False
    #             down_counter = 0
    #     if not left:
    #         left = check_left_press(screen_red)
    #     else:
    #         left_counter += 1
    #         if left_counter > special_limit:
    #             left = False
    #             left_counter = 0