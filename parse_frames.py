import numpy as np
import cv2 as cv
import glob
import PIL
from PIL import Image

zero_real = np.array([[[0, 0, 0],       [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0]],
                              [[255, 255, 255], [0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [255, 255, 255]],
                              [[255, 255, 255], [0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [255, 255, 255]],
                              [[255, 255, 255], [0, 0, 0],       [255, 255, 255], [0, 0, 0],       [255, 255, 255]],
                              [[255, 255, 255], [0, 0, 0],       [255, 255, 255], [0, 0, 0],       [255, 255, 255]],
                              [[255, 255, 255], [0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [255, 255, 255]],
                              [[255, 255, 255], [0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [255, 255, 255]],
                              [[0, 0, 0],       [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0]]])

zero_bool = np.array([[[False, False, False], [True, True, True],    [True, True, True],    [True, True, True],    [False, False, False]],
                      [[True, True, True],    [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                      [[True, True, True],    [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                      [[True, True, True],    [False, False, False], [True, True, True],    [False, False, False], [True, True, True]],
                      [[True, True, True],    [False, False, False], [True, True, True],    [False, False, False], [True, True, True]],
                      [[True, True, True],    [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                      [[True, True, True],    [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                      [[False, False, False], [True, True, True],    [True, True, True],    [True, True, True],    [False, False, False]]])

one_real = np.array([[[0, 0, 0],       [0, 0, 0],       [255, 255, 255], [0, 0, 0],       [0, 0, 0]],
                     [[0, 0, 0],       [255, 255, 255], [255, 255, 255], [0, 0, 0],       [0, 0, 0]],
                     [[255, 255, 255], [0, 0, 0],       [255, 255, 255], [0, 0, 0],       [0, 0, 0]],
                     [[0, 0, 0],       [0, 0, 0],       [255, 255, 255], [0, 0, 0],       [0, 0, 0]],
                     [[0, 0, 0],       [0, 0, 0],       [255, 255, 255], [0, 0, 0],       [0, 0, 0]],
                     [[0, 0, 0],       [0, 0, 0],       [255, 255, 255], [0, 0, 0],       [0, 0, 0]],
                     [[0, 0, 0],       [0, 0, 0],       [255, 255, 255], [0, 0, 0],       [0, 0, 0]],
                     [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]]])

one_bool = np.array([[[False, False, False], [False, False, False], [True, True, True], [False, False, False], [False, False, False]],
                     [[False, False, False], [True, True, True],    [True, True, True], [False, False, False], [False, False, False]],
                     [[True, True, True],    [False, False, False], [True, True, True], [False, False, False], [False, False, False]],
                     [[False, False, False], [False, False, False], [True, True, True], [False, False, False], [False, False, False]],
                     [[False, False, False], [False, False, False], [True, True, True], [False, False, False], [False, False, False]],
                     [[False, False, False], [False, False, False], [True, True, True], [False, False, False], [False, False, False]],
                     [[False, False, False], [False, False, False], [True, True, True], [False, False, False], [False, False, False]],
                     [[True, True, True],    [True, True, True],    [True, True, True], [True, True, True],    [True, True, True]]])

two_real = np.array([[[0, 0, 0],       [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0]],
                     [[255, 255, 255], [0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [255, 255, 255]],
                     [[0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [255, 255, 255]],
                     [[0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [255, 255, 255], [0, 0, 0]],
                     [[0, 0, 0],       [0, 0, 0],       [255, 255, 255], [0, 0, 0],       [0, 0, 0]],
                     [[0, 0, 0],       [255, 255, 255], [0, 0, 0],       [0, 0, 0],       [0, 0, 0]],
                     [[255, 255, 255], [0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [0, 0, 0]],
                     [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]]])

two_bool = np.array([[[False, False, False], [True, True, True],    [True, True, True],    [True, True, True],    [False, False, False]],
                     [[True, True, True],    [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                     [[False, False, False], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                     [[False, False, False], [False, False, False], [False, False, False], [True, True, True],    [False, False, False]],
                     [[False, False, False], [False, False, False], [True, True, True], [False, False, False],    [False, False, False]],
                     [[False, False, False], [True, True, True],    [False, False, False], [False, False, False], [False, False, False]],
                     [[True, True, True],    [False, False, False], [False, False, False], [False, False, False], [False, False, False]],
                     [[True, True, True],    [True, True, True],    [True, True, True],    [True, True, True],    [True, True, True]]])


three_real = np.array([[[0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0]],
                       [[255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                       [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                       [[0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0]],
                       [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                       [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                       [[255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                       [[0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0]]])

three_bool = np.array([[[False, False, False], [True, True, True], [True, True, True], [True, True, True], [False, False, False]],
                       [[True, True, True], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                       [[False, False, False], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                       [[False, False, False], [False, False, False], [True, True, True], [True, True, True], [False, False, False]],
                       [[False, False, False], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                       [[False, False, False], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                       [[True, True, True], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                       [[False, False, False], [True, True, True], [True, True, True], [True, True, True], [False, False, False]]])


four_real = np.array([[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                      [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255]],
                      [[0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255]],
                      [[0, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                      [[255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                      [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
                      [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                      [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]]])

four_bool = np.array([[[False, False, False], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                      [[False, False, False], [False, False, False], [False, False, False], [True, True, True], [True, True, True]],
                      [[False, False, False], [False, False, False], [True, True, True], [False, False, False], [True, True, True]],
                      [[False, False, False], [True, True, True], [False, False, False], [False, False, False], [True, True, True]],
                      [[True, True, True], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                      [[True, True, True], [True, True, True], [True, True, True], [True, True, True], [True, True, True]],
                      [[False, False, False], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                      [[False, False, False], [False, False, False], [False, False, False], [False, False, False], [True, True, True]]])


five_real = np.array([[[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
                      [[255, 255, 255], [0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [0, 0, 0]],
                      [[255, 255, 255], [0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [0, 0, 0]],
                      [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0]],
                      [[0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [255, 255, 255]],
                      [[0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [255, 255, 255]],
                      [[255, 255, 255], [0, 0, 0],       [0, 0, 0],       [0, 0, 0],       [255, 255, 255]],
                      [[0, 0, 0],       [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0]]])

five_bool = np.array([[[True, True, True], [True, True, True], [True, True, True], [True, True, True], [True, True, True]],
                      [[True, True, True], [False, False, False],       [False, False, False],       [False, False, False],       [False, False, False]],
                      [[True, True, True], [False, False, False],       [False, False, False],       [False, False, False],       [False, False, False]],
                      [[True, True, True], [True, True, True], [True, True, True], [True, True, True], [False, False, False]],
                      [[False, False, False],       [False, False, False],       [False, False, False],       [False, False, False],       [True, True, True]],
                      [[False, False, False],       [False, False, False],       [False, False, False],       [False, False, False],       [True, True, True]],
                      [[True, True, True], [False, False, False],       [False, False, False],       [False, False, False],       [True, True, True]],
                      [[False, False, False],       [True, True, True], [True, True, True], [True, True, True], [False, False, False]]])


six_real = np.array([[[0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0]],
                     [[0, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
                     [[255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
                     [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0]],
                     [[255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                     [[255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                     [[255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                     [[0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0]]])

six_bool = np.array([[[False, False, False], [False, False, False], [True, True, True], [True, True, True], [False, False, False]],
                     [[False, False, False], [True, True, True], [False, False, False], [False, False, False], [False, False, False]],
                     [[True, True, True], [False, False, False], [False, False, False], [False, False, False], [False, False, False]],
                     [[True, True, True], [True, True, True], [True, True, True], [True, True, True], [False, False, False]],
                     [[True, True, True], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                     [[True, True, True], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                     [[True, True, True], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                     [[False, False, False], [True, True, True], [True, True, True], [True, True, True], [False, False, False]]])


seven_real = np.array([[[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
                       [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                       [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 0]],
                       [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 0]],
                       [[0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0]],
                       [[0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0]],
                       [[0, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
                       [[0, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]]])

seven_bool = np.array([[[True, True, True], [True, True, True], [True, True, True], [True, True, True], [True, True, True]],
                       [[False, False, False], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                       [[False, False, False], [False, False, False], [False, False, False], [True, True, True], [False, False, False]],
                       [[False, False, False], [False, False, False], [False, False, False], [True, True, True], [False, False, False]],
                       [[False, False, False], [False, False, False], [True, True, True], [False, False, False], [False, False, False]],
                       [[False, False, False], [False, False, False], [True, True, True], [False, False, False], [False, False, False]],
                       [[False, False, False], [True, True, True], [False, False, False], [False, False, False], [False, False, False]],
                       [[False, False, False], [True, True, True], [False, False, False], [False, False, False], [False, False, False]]])


eight_real = np.array([[[0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0]],
                       [[255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                       [[255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                       [[0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0]],
                       [[255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                       [[255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                       [[255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                       [[0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0]]])

eight_bool = np.array([[[False, False, False], [True, True, True], [True, True, True], [True, True, True], [False, False, False]],
                       [[True, True, True], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                       [[True, True, True], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                       [[False, False, False], [True, True, True], [True, True, True], [True, True, True], [False, False, False]],
                       [[True, True, True], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                       [[True, True, True], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                       [[True, True, True], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                       [[False, False, False], [True, True, True], [True, True, True], [True, True, True], [False, False, False]]])


nine_real = np.array([[[0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0]],
                      [[255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                      [[255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                      [[255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                      [[0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
                      [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255]],
                      [[0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 0]],
                      [[0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0]]])

nine_bool = np.array([[[False, False, False], [True, True, True], [True, True, True], [True, True, True], [False, False, False]],
                      [[True, True, True], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                      [[True, True, True], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                      [[True, True, True], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                      [[False, False, False], [True, True, True], [True, True, True], [True, True, True], [True, True, True]],
                      [[False, False, False], [False, False, False], [False, False, False], [False, False, False], [True, True, True]],
                      [[False, False, False], [False, False, False], [False, False, False], [True, True, True], [False, False, False]],
                      [[False, False, False], [True, True, True], [True, True, True], [False, False, False], [False, False, False]]])


comma_real = np.array([[[0, 0, 0], [255, 255, 255], [0, 0, 0]],
                       [[0, 0, 0], [255, 255, 255], [0, 0, 0]],
                       [[0, 0, 0], [255, 255, 255], [0, 0, 0]],
                       [[255, 255, 255], [0, 0, 0], [0, 0, 0]]])

comma_bool = np.array([[[False, False, False], [True, True, True], [False, False, False]],
                       [[False, False, False], [True, True, True], [False, False, False]],
                       [[False, False, False], [True, True, True], [False, False, False]],
                       [[True, True, True], [False, False, False], [False, False, False]]])


top = 62
bottom = 70
comma_top = 62+6
comma_bottom = 71+1

offset = 5
comma_offset = 3
down_start = 1106
down_end = down_start + offset
up_start = 1050
up_end = up_start + offset
start_start = 1008
start_end = start_start + offset
z_start = 945
z_end = z_start + offset
y_start = 910
y_end = y_start + offset
x_start = 875
x_end = x_start + offset
b_start = 840
b_end = b_start + offset
a_start = 805
a_end = a_start + offset

ana_first_start = 1400
ana_first_end = ana_first_start + offset

ana_second_start = 1407
ana_second_end = ana_second_start + offset

ana_comma_first = 1414
ana_comma_first_end = ana_comma_first + comma_offset

ana_third_start = 1414
ana_third_end = ana_third_start + offset

ana_comma_second_start = 1421
ana_comma_second_end = ana_comma_second_start + comma_offset

late_comma_ana_first_start = 1428
late_comma_ana_first_end = late_comma_ana_first_start + offset
late_comma_ana_second_start = 1435
late_comma_ana_second_end = late_comma_ana_second_start + offset
late_comma_ana_third_start = 1442
late_comma_ana_third_end = late_comma_ana_third_start + offset

early_comma_ana_first_start = 1421
early_comma_ana_first_end = early_comma_ana_first_start + offset
early_comma_ana_second_start = 1428
early_comma_ana_second_end = early_comma_ana_second_start + offset
early_comma_ana_third_start = 1435
early_comma_ana_third_end = early_comma_ana_third_start + offset


def is_number(to_test, number_real, number_bool):
    and_array = to_test == number_real
    bool_array = np.logical_and(and_array, number_bool)
    if np.array_equal(bool_array, number_bool):
        return True
    return False


def is_comma(image):
    and_array = image == comma_real
    bool_array = np.logical_and(and_array, comma_bool)
    if np.array_equal(bool_array, comma_bool):
        return True
    return False


def find_num(image):
    if is_number(image, zero_real, zero_bool):
        return 0
    elif is_number(image, one_real, one_bool):
        return 1
    elif is_number(image, two_real, two_bool):
        return 2
    elif is_number(image, three_real, three_bool):
        return 3
    elif is_number(image, four_real, four_bool):
        return 4
    elif is_number(image, five_real, five_bool):
        return 5
    elif is_number(image, six_real, six_bool):
        return 6
    elif is_number(image, seven_real, seven_bool):
        return 7
    elif is_number(image, eight_real, eight_bool):
        return 8
    elif is_number(image, nine_real, nine_bool):
        return 9
    return .5


def get_analog_x(image):
    first = image[top:bottom, ana_first_start:ana_first_end]
    first_num = find_num(first)
    second = image[top:bottom, ana_second_start:ana_second_end]
    second_num = find_num(second)

    if is_comma(image[comma_top:comma_bottom, ana_comma_first:ana_comma_first_end]):
        return int((first_num * 10) + second_num), True

    third = image[top:bottom, ana_third_start:ana_third_end]
    third_num = find_num(third)
    return int((first_num * 100) + (second_num * 10) + third_num), False


def get_analog_y_early_comma(image):
    first = image[top:bottom, early_comma_ana_first_start:early_comma_ana_first_end]
    first_num = find_num(first)
    second = image[top:bottom, early_comma_ana_second_start:early_comma_ana_second_end]
    second_num = find_num(second)
    third = image[top:bottom, early_comma_ana_third_start:early_comma_ana_third_end]
    third_num = find_num(third)
    if third_num == .5:
        return int((first_num * 10) + second_num)
    return int((first_num * 100) + (second_num * 10) + third_num)


def get_analog_y_late_comma(image):
    first = image[top:bottom, late_comma_ana_first_start:late_comma_ana_first_end]
    first_num = find_num(first)
    second = image[top:bottom, late_comma_ana_second_start:late_comma_ana_second_end]
    second_num = find_num(second)
    third = image[top:bottom, late_comma_ana_third_start:late_comma_ana_third_end]
    third_num = find_num(third)
    if third_num == .5:
        return int((first_num * 10) + second_num)
    return int((first_num * 100) + (second_num * 10) + third_num)


def analog_logic(image):
    stick_x, early_comma = get_analog_x(image)
    if early_comma:
        stick_y = get_analog_y_early_comma(image)
    else:
        stick_y = get_analog_y_late_comma(image)
    return stick_x, stick_y


def get_input_string(image):
    #[Start, a, b, x, y, z, stick-x, stick-y]

    start = image[top:bottom, start_start:start_end]
    if is_number(start, zero_real, zero_bool):
        start = 0
    else:
        start = 1

    a = image[top:bottom, a_start:a_end]
    if is_number(a, zero_real, zero_bool):
        a = 0
    else:
        a = 1

    b = image[top:bottom, b_start:b_end]
    if is_number(b, zero_real, zero_bool):
        b = 0
    else:
        b = 1
    x = image[top:bottom, x_start:x_end]
    if is_number(x, zero_real, zero_bool):
        x = 0
    else:
        x = 1
    y = image[top:bottom, y_start:y_end]
    if is_number(y, zero_real, zero_bool):
        y = 0
    else:
        y = 1
    z = image[top:bottom, z_start:z_end]
    if is_number(z, zero_real, zero_bool):
        z = 0
    else:
        z = 1
    stick_x, stick_y = analog_logic(image)
    #[Start, a, b, x, y, z, stick-x, stick-y]

    return f"{a} {b} {x} {y} {z} {start} {stick_x} {stick_y}"


def main():
    for i, image_path in enumerate(glob.glob("frames/*.png")):
        image = cv.imread(image_path)
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        input_str = get_input_string(image)
        print(input_str)
        print(i)
        image[top:comma_bottom, a_start:late_comma_ana_third_end] = [0,0,0]
        im = PIL.Image.fromarray(image)
        im.save(f"train_frames/{i}.png")
        with open(f"input/{i}.txt", "w") as text_file:
            print(input_str, file=text_file)


if __name__ == "__main__":
    main()
