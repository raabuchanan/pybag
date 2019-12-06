#!/usr/bin/env python3
from BagParser import BagParser
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon


def print_low_indoor_experiment(position_values, rotation_values, time_stamps):
    #  "args": ["/media/russellb/Bradburrito/JFR2019/jfr_data/bags/60cm/2019-07-14-21-35-14.bag", "/home/russellb/Dropbox/Apps/ShareLaTeX/Buchanan JFR 2019/figures/pdf/"],

    start_time = 20
    end_time = 100

    body_height_offset = 0.08
    body_height = 0.24
    mount_height = 0.13
    body_width = 0.27
    body_length = 0.531

    obstacle_above_start = 1.4
    obstacle_above_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_above_start)

    obstacle_above_end = 1.45
    obstacle_above_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_above_end)

    obstacle_right_start = 1.4
    obstacle_right_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_right_start)
    obstacle_right_end = 1.45
    obstacle_right_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_right_end)

    obstacle_left_start = 1.4
    obstacle_left_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_left_start)
    obstacle_left_end = 1.45
    obstacle_left_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_left_end)


    start_index = parser.convert_value_to_index(time_stamps, start_time)
    end_index = parser.convert_value_to_index(time_stamps, end_time)

    x_axis_values = time_stamps  # position_values

    plt.rcParams['axes.titlesize'] = 22
    plt.rcParams['axes.labelsize'] = 22
    plt.rcParams['xtick.labelsize'] = 22
    plt.rcParams['ytick.labelsize'] = 22
    plt.rcParams.update({'font.size': 20})
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
    position_figure = plt.figure(0, figsize=(16, 9), dpi=120)
    #position_figure.suptitle("Low Gap", fontsize=30)
    left_ax1 = plt.subplot(3, 1, 1)
    plt.plot(x_axis_values[start_index:end_index],
             rotation_values[start_index:end_index, 0], '--', color=(1, 0, 0), label='Roll (degrees)')
    #plt.xlabel('Time (s)')
    #plt.ylabel('Roll (degrees)')
    left_ax1.set_ylim(-45, 45)
    left_ax1.legend(loc="upper left")
######################################################################################################################################
    left_ax2 = plt.subplot(3, 1, 2)
    left_ax2.fill_between(x_axis_values[start_index:end_index, 0],
                              position_values[start_index:end_index,
                                              1] - body_width / 2.0,
                              position_values[start_index:end_index, 1] + body_width / 2.0, color=(0, 1, 0), alpha=0.1, label='Y Position (m)')
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 1] - body_width / 2.0, color=(0, 1, 0))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 1] + body_width / 2.0, color=(0, 1, 0))

    right_ax2 = left_ax2.twinx()
    right_ax2.plot(x_axis_values[start_index:end_index],
                                   rotation_values[start_index:end_index, 2], '--', color=(0, 0, 1), label="Yaw (degrees)")


    left_ax2.fill_between(x_axis_values[obstacle_right_start_idx:obstacle_right_end_idx, 0],
                              -0.5,
                              -0.6, color=(0, 0, 0), alpha=0.5)
    left_ax2.fill_between(x_axis_values[obstacle_left_start_idx:obstacle_left_end_idx, 0],
                              0.5,
                              0.6, color=(0, 0, 0), alpha=0.5)

    left_ax2.legend(loc="upper left")
    left_ax2.set_ylim(-0.6, 0.6)
    right_ax2.legend(loc="upper right")
    right_ax2.set_ylim(-45, 45)
######################################################################################################################################
    left_ax3 = plt.subplot(3, 1, 3)
    left_ax3.fill_between(x_axis_values[start_index:end_index, 0],
                              position_values[start_index:end_index,
                                              2] + body_height_offset - body_height / 2.0,
                              position_values[start_index:end_index, 2] + body_height_offset + body_height / 2.0 + mount_height, color=(0, 0, 1), alpha=0.1, label='Z Position (m)')
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 2] + body_height_offset - body_height / 2.0, color=(0, 0, 1))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 2] + body_height_offset + body_height / 2.0 + mount_height, color=(0, 0, 1))

    right_ax3 = left_ax3.twinx()
    right_ax3.plot(x_axis_values[start_index:end_index],
                                   rotation_values[start_index:end_index, 1], '--', color=(0, 1, 0), label="Pitch (degrees)")


    left_ax3.fill_between(x_axis_values[obstacle_above_start_idx:obstacle_above_end_idx, 0],
                                1.0,
                                0.6, color=(0, 0, 0), alpha=0.5)

    left_ax3.set_xlabel('Time (s)')
    left_ax3.legend(loc="upper left")
    left_ax3.set_ylim(0, 1)
    right_ax3.legend(loc="upper right")
    right_ax3.set_ylim(-45, 45)

    #position_figure.tight_layout()

    position_figure.savefig(
        sys.argv[2] + "indoor-low-plot.pdf", bbox_inches='tight', format='pdf')

    min_height = np.amin(position_values[start_index:end_index,2])
    max_height = np.max(position_values[start_index:end_index,2])
    print("Min Height: %f (%f,%f)" % (min_height, min_height + body_height_offset - body_height / 2.0, 
                                        min_height + body_height_offset + body_height / 2.0 + mount_height))

    print("Max Height: %f (%f,%f)" % (max_height, max_height + body_height_offset - body_height / 2.0, 
                                        max_height + body_height_offset + body_height / 2.0 + mount_height))

    print("Max Roll: %f" % (np.amax(rotation_values[start_index:end_index,0])) )
    print("Max Pitch: %f" % (np.amax(rotation_values[start_index:end_index,1])) )
    print("Max Yaw: %f" % (np.amax(rotation_values[start_index:end_index,2])) )

    print("Min Roll: %f" % (np.amin(rotation_values[start_index:end_index,0])) )
    print("Min Pitch: %f" % (np.amin(rotation_values[start_index:end_index,1])) )
    print("Min Yaw: %f" % (np.amin(rotation_values[start_index:end_index,2])) )


    position_figure.show()

    input()



def print_rotated_indoor_experiment(position_values, rotation_values, time_stamps):
# "args": ["/media/russellb/Bradburrito/JFR2019/jfr_data/bags/45degrees/2019-07-21-10-33-17.bag", "/home/russellb/Dropbox/Apps/ShareLaTeX/Buchanan JFR 2019/figures/pdf/"],
    start_time = 20
    end_time = 100

    body_height_offset = 0.08
    body_height = 0.24
    mount_height = 0.13
    body_width = 0.27
    body_length = 0.531

    obstacle_above_start = 1.2
    obstacle_above_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_above_start)

    obstacle_above_end = 1.25
    obstacle_above_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_above_end)

    obstacle_right_start = 1.2
    obstacle_right_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_right_start)
    obstacle_right_end = 1.25
    obstacle_right_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_right_end)

    obstacle_left_start = 1.2
    obstacle_left_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_left_start)
    obstacle_left_end = 1.25
    obstacle_left_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_left_end)

    start_index = parser.convert_value_to_index(time_stamps, start_time)
    end_index = parser.convert_value_to_index(time_stamps, end_time)

    x_axis_values = time_stamps  # position_values

    plt.rcParams['axes.titlesize'] = 22
    plt.rcParams['axes.labelsize'] = 22
    plt.rcParams['xtick.labelsize'] = 22
    plt.rcParams['ytick.labelsize'] = 22
    plt.rcParams.update({'font.size': 20})
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
    position_figure = plt.figure(0, figsize=(16, 9), dpi=100)
    #position_figure.suptitle("Rotated Gap", fontsize=30)
    left_ax1 = plt.subplot(3, 1, 1)
    plt.plot(x_axis_values[start_index:end_index],
             rotation_values[start_index:end_index, 0], '--', color=(1, 0, 0), label='Roll (degrees)')
    #plt.xlabel('Time (s)')
    #plt.ylabel('Roll (degrees)')
    left_ax1.set_ylim(-45, 45)
    left_ax1.legend(loc="upper left")
######################################################################################################################################
    left_ax2 = plt.subplot(3, 1, 2)
    left_ax2.fill_between(x_axis_values[start_index:end_index, 0],
                              position_values[start_index:end_index,
                                              1] - body_width / 2.0,
                              position_values[start_index:end_index, 1] + body_width / 2.0, color=(0, 1, 0), alpha=0.1, label='Y Position (m)')
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 1] - body_width / 2.0, color=(0, 1, 0))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 1] + body_width / 2.0, color=(0, 1, 0))

    right_ax2 = left_ax2.twinx()
    right_ax2.plot(x_axis_values[start_index:end_index],
                                   rotation_values[start_index:end_index, 2], '--', color=(0, 0, 1), label="Yaw (degrees)")


    left_ax2.fill_between(x_axis_values[obstacle_right_start_idx:obstacle_right_end_idx, 0],
                              -0.5,
                              -0.6, color=(0, 0, 0), alpha=0.5)
    left_ax2.fill_between(x_axis_values[obstacle_left_start_idx:obstacle_left_end_idx, 0],
                              0.5,
                              0.6, color=(0, 0, 0), alpha=0.5)

    left_ax2.legend(loc="upper left")
    left_ax2.set_ylim(-0.6, 0.6)
    right_ax2.legend(loc="upper right")
    right_ax2.set_ylim(-45, 45)
######################################################################################################################################
    left_ax3 = plt.subplot(3, 1, 3)
    left_ax3.fill_between(x_axis_values[start_index:end_index, 0],
                              position_values[start_index:end_index,
                                              2] + body_height_offset - body_height / 2.0,
                              position_values[start_index:end_index, 2] + body_height_offset + body_height / 2.0 + mount_height, color=(0, 0, 1), alpha=0.1, label='Z Position (m)')
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 2] + body_height_offset - body_height / 2.0, color=(0, 0, 1))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 2] + body_height_offset + body_height / 2.0 + mount_height, color=(0, 0, 1))

    right_ax3 = left_ax3.twinx()
    right_ax3.plot(x_axis_values[start_index:end_index],
                                   rotation_values[start_index:end_index, 1], '--', color=(0, 1, 0), label="Pitch (degrees)")


    left_ax3.fill_between(x_axis_values[obstacle_above_start_idx:obstacle_above_end_idx, 0],
                                1.0,
                                0.71, color=(0, 0, 0), alpha=0.5)

    left_ax3.set_xlabel('Time (s)')
    left_ax3.legend(loc="upper left")
    left_ax3.set_ylim(0, 1)
    right_ax3.legend(loc="upper right")
    right_ax3.set_ylim(-45, 45)

    #position_figure.tight_layout()

    min_height = np.amin(position_values[start_index:end_index,2])
    max_height = np.max(position_values[start_index:end_index,2])
    print("Min Height: %f (%f,%f)" % (min_height, min_height + body_height_offset - body_height / 2.0, 
                                        min_height + body_height_offset + body_height / 2.0 + mount_height))

    print("Max Height: %f (%f,%f)" % (max_height, max_height + body_height_offset - body_height / 2.0, 
                                        max_height + body_height_offset + body_height / 2.0 + mount_height))

    print("Max Roll: %f" % (np.amax(rotation_values[start_index:end_index,0])) )
    print("Max Pitch: %f" % (np.amax(rotation_values[start_index:end_index,1])) )
    print("Max Yaw: %f" % (np.amax(rotation_values[start_index:end_index,2])) )

    print("Min Roll: %f" % (np.amin(rotation_values[start_index:end_index,0])) )
    print("Min Pitch: %f" % (np.amin(rotation_values[start_index:end_index,1])) )
    print("Min Yaw: %f" % (np.amin(rotation_values[start_index:end_index,2])) )


    position_figure.savefig(
        sys.argv[2] + "indoor-rotated-plot.pdf", bbox_inches='tight', format='pdf')

    position_figure.show()

    input()


def print_step_indoor_experiment(position_values, rotation_values, time_stamps):
#"args": ["/media/russellb/Bradburrito/JFR2019/jfr_data/bags/step/2019-07-21-11-49-35.bag", "/home/russellb/Dropbox/Apps/ShareLaTeX/Buchanan JFR 2019/figures/pdf/"],
    start_time = 0
    end_time = 100

    body_height_offset = 0.08
    body_height = 0.24
    mount_height = 0.13
    body_width = 0.27
    body_length = 0.531

    obstacle_above_start = 1.5
    obstacle_above_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_above_start)

    obstacle_above_end = 1.55
    obstacle_above_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_above_end)

    obstacle_below_start = 1.5
    obstacle_below_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_below_start)

    obstacle_below_end = 1.55
    obstacle_below_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_below_end)

    obstacle_right_start = 1.5
    obstacle_right_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_right_start)
    obstacle_right_end = 1.55
    obstacle_right_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_right_end)

    obstacle_left_start = 1.5
    obstacle_left_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_left_start)
    obstacle_left_end = 1.55
    obstacle_left_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_left_end)

    start_index = parser.convert_value_to_index(time_stamps, start_time)
    end_index = parser.convert_value_to_index(time_stamps, end_time)

    x_axis_values = time_stamps  # position_values

    plt.rcParams['axes.titlesize'] = 22
    plt.rcParams['axes.labelsize'] = 22
    plt.rcParams['xtick.labelsize'] = 22
    plt.rcParams['ytick.labelsize'] = 22
    plt.rcParams.update({'font.size': 20})
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
    position_figure = plt.figure(0, figsize=(16, 9), dpi=120)
    #position_figure.suptitle("Gap with Step", fontsize=30)
    left_ax1 = plt.subplot(3, 1, 1)
    plt.plot(x_axis_values[start_index:end_index],
             rotation_values[start_index:end_index, 0], '--', color=(1, 0, 0), label='Roll (degrees)')
    plt.xlabel('Time (s)')
    #plt.ylabel('Roll (degrees)')
    left_ax1.set_ylim(-45, 45)
    left_ax1.legend(loc="upper left")
######################################################################################################################################
    left_ax2 = plt.subplot(3, 1, 2)
    left_ax2.fill_between(x_axis_values[start_index:end_index, 0],
                              position_values[start_index:end_index,
                                              1] - body_width / 2.0,
                              position_values[start_index:end_index, 1] + body_width / 2.0, color=(0, 1, 0), alpha=0.1, label='Y Position (m)')
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 1] - body_width / 2.0, color=(0, 1, 0))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 1] + body_width / 2.0, color=(0, 1, 0))

    right_ax2 = left_ax2.twinx()
    right_ax2.plot(x_axis_values[start_index:end_index],
                                   rotation_values[start_index:end_index, 2], '--', color=(0, 0, 1), label="Yaw (degrees)")


    left_ax2.fill_between(x_axis_values[obstacle_right_start_idx:obstacle_right_end_idx, 0],
                              -0.5,
                              -0.6, color=(0, 0, 0), alpha=0.5)
    left_ax2.fill_between(x_axis_values[obstacle_left_start_idx:obstacle_left_end_idx, 0],
                              0.5,
                              0.6, color=(0, 0, 0), alpha=0.5)

    left_ax2.legend(loc="upper left")
    left_ax2.set_ylim(-0.6, 0.6)
    right_ax2.legend(loc="upper right")
    right_ax2.set_ylim(-45, 45)
######################################################################################################################################
    left_ax3 = plt.subplot(3, 1, 3)
    left_ax3.fill_between(x_axis_values[start_index:end_index, 0],
                              position_values[start_index:end_index,
                                              2] + body_height_offset - body_height / 2.0,
                              position_values[start_index:end_index, 2] + body_height_offset + body_height / 2.0 + mount_height, color=(0, 0, 1), alpha=0.1, label='Z Position (m)')
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 2] + body_height_offset - body_height / 2.0, color=(0, 0, 1))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 2] + body_height_offset + body_height / 2.0 + mount_height, color=(0, 0, 1))

    right_ax3 = left_ax3.twinx()
    right_ax3.plot(x_axis_values[start_index:end_index],
                                   rotation_values[start_index:end_index, 1], '--', color=(0, 1, 0), label="Pitch (degrees)")


    left_ax3.fill_between(x_axis_values[obstacle_above_start_idx:obstacle_above_end_idx, 0],
                                1.0,
                                0.71, color=(0, 0, 0), alpha=0.5)

    left_ax3.fill_between(x_axis_values[obstacle_below_start_idx:obstacle_below_end_idx, 0],
                                0.0,
                                0.1, color=(0, 0, 0), alpha=0.5)

    left_ax3.set_xlabel('Time (s)')
    left_ax3.legend(loc="upper left")
    left_ax3.set_ylim(0, 1)
    right_ax3.legend(loc="upper right")
    right_ax3.set_ylim(-45, 45)

    #position_figure.tight_layout()

    min_height = np.amin(position_values[start_index:end_index,2])
    max_height = np.max(position_values[start_index:end_index,2])
    print("Min Height: %f (%f,%f)" % (min_height, min_height + body_height_offset - body_height / 2.0, 
                                        min_height + body_height_offset + body_height / 2.0 + mount_height))

    print("Max Height: %f (%f,%f)" % (max_height, max_height + body_height_offset - body_height / 2.0, 
                                        max_height + body_height_offset + body_height / 2.0 + mount_height))

    print("Max Roll: %f" % (np.amax(rotation_values[start_index:end_index,0])) )
    print("Max Pitch: %f" % (np.amax(rotation_values[start_index:end_index,1])) )
    print("Max Yaw: %f" % (np.amax(rotation_values[start_index:end_index,2])) )

    print("Min Roll: %f" % (np.amin(rotation_values[start_index:end_index,0])) )
    print("Min Pitch: %f" % (np.amin(rotation_values[start_index:end_index,1])) )
    print("Min Yaw: %f" % (np.amin(rotation_values[start_index:end_index,2])) )


    position_figure.savefig(
        sys.argv[2] + "indoor-step-plot.pdf", bbox_inches='tight', format='pdf')

    position_figure.show()

    input()


def print_first_field_experiment(position_values, rotation_values, time_stamps):
    #"args": ["/media/russellb/Bradburrito/JFR2019/jfr_data/bags/best_bags/2019-05-31-13-11-28.bag", "/home/russellb/Dropbox/Apps/ShareLaTeX/Buchanan JFR 2019/figures/pdf/"],

    start_time = 0
    end_time = 55

    body_height_offset = 0.08
    body_height = 0.24
    mount_height = 0.13
    body_width = 0.27
    body_length = 0.531

    hole_width = 0.75
    step_height = 0.1
    hole_height = 0.8

    obstacle_above_start = 1.25
    obstacle_above_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_above_start)

    obstacle_above_end = 1.55
    obstacle_above_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_above_end)

    obstacle_below_start = 1.25
    obstacle_below_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_below_start)

    obstacle_below_end = 1.55
    obstacle_below_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_below_end)

    obstacle_right_start = 1.25
    obstacle_right_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_right_start)
    obstacle_right_end = 1.55
    obstacle_right_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_right_end)

    obstacle_left_start = 1.25
    obstacle_left_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_left_start)
    obstacle_left_end = 1.55
    obstacle_left_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_left_end)

    start_index = parser.convert_value_to_index(time_stamps, start_time)
    end_index = parser.convert_value_to_index(time_stamps, end_time)

    obstacle_below_end_idx = end_index
    x_axis_values = time_stamps  # position_values

    plt.rcParams['axes.titlesize'] = 22
    plt.rcParams['axes.labelsize'] = 22
    plt.rcParams['xtick.labelsize'] = 22
    plt.rcParams['ytick.labelsize'] = 22
    plt.rcParams.update({'font.size': 20})
######################################################################################################################################
    position_figure = plt.figure(0, figsize=(16, 9), dpi=120)
    #position_figure.suptitle("Rectangular Gap", fontsize=30)
    left_ax1 = plt.subplot(3, 1, 1)
    plt.plot(x_axis_values[start_index:end_index],
             rotation_values[start_index:end_index, 0], '--', color=(1, 0, 0), label='Roll (degrees)')
    left_ax1.set_ylim(-45, 45)
    left_ax1.legend(loc="upper left")
######################################################################################################################################
    left_ax2 = plt.subplot(3, 1, 2)
    left_ax2.fill_between(x_axis_values[start_index:end_index, 0],
                              position_values[start_index:end_index,
                                              1] - body_width / 2.0,
                              position_values[start_index:end_index, 1] + body_width / 2.0, color=(0, 1, 0), alpha=0.1, label='Y Position (m)')
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 1] - body_width / 2.0, color=(0, 1, 0))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 1] + body_width / 2.0, color=(0, 1, 0))

    right_ax2 = left_ax2.twinx()
    right_ax2.plot(x_axis_values[start_index:end_index],
                                   rotation_values[start_index:end_index, 2], '--', color=(0, 0, 1), label="Yaw (degrees)")


    left_ax2.fill_between(x_axis_values[obstacle_right_start_idx:obstacle_right_end_idx, 0],
                              -(hole_width / 2.0),
                              -1.0, color=(0, 0, 0), alpha=0.5)
    left_ax2.fill_between(x_axis_values[obstacle_left_start_idx:obstacle_left_end_idx, 0],
                              1.0,
                              hole_width / 2.0, color=(0, 0, 0), alpha=0.5)

    left_ax2.legend(loc="upper left")
    left_ax2.set_ylim(-0.6, 0.6)
    right_ax2.legend(loc="upper right")
    right_ax2.set_ylim(-45, 45)

###################################################################################################################3
    left_ax3 = plt.subplot(3, 1, 3)
    left_ax3.fill_between(x_axis_values[start_index:end_index, 0],
                              position_values[start_index:end_index,
                                              2] + body_height_offset - body_height / 2.0,
                              position_values[start_index:end_index, 2] + body_height_offset + body_height / 2.0 + mount_height, color=(0, 0, 1), alpha=0.1, label='Z Position (m)')
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 2] + body_height_offset - body_height / 2.0, color=(0, 0, 1))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 2] + body_height_offset + body_height / 2.0 + mount_height, color=(0, 0, 1))

    right_ax3 = left_ax3.twinx()
    right_ax3.plot(x_axis_values[start_index:end_index],
                                   rotation_values[start_index:end_index, 1], '--', color=(0, 1, 0), label="Pitch (degrees)")


    left_ax3.fill_between(x_axis_values[obstacle_above_start_idx:obstacle_above_end_idx, 0],
                                1.0,
                                hole_height + step_height, color=(0, 0, 0), alpha=0.5)

    left_ax3.fill_between(x_axis_values[obstacle_below_start_idx:obstacle_below_end_idx, 0],
                                -0.1,
                                step_height, color=(0, 0, 0), alpha=0.5)

    left_ax3.set_xlabel('Time (s)')
    left_ax3.legend(loc="upper left")
    left_ax3.set_ylim(0, 1)
    right_ax3.legend(loc="upper right")
    right_ax3.set_ylim(-45, 45)

    #position_figure.tight_layout()

    min_height = np.amin(position_values[start_index:end_index,2])
    max_height = np.max(position_values[start_index:end_index,2])
    print("Min Height: %f (%f,%f)" % (min_height, min_height + body_height_offset - body_height / 2.0, 
                                        min_height + body_height_offset + body_height / 2.0 + mount_height))

    print("Max Height: %f (%f,%f)" % (max_height, max_height + body_height_offset - body_height / 2.0, 
                                        max_height + body_height_offset + body_height / 2.0 + mount_height))

    print("Max Roll: %f" % (np.amax(rotation_values[start_index:end_index,0])) )
    print("Max Pitch: %f" % (np.amax(rotation_values[start_index:end_index,1])) )
    print("Max Yaw: %f" % (np.amax(rotation_values[start_index:end_index,2])) )

    print("Min Roll: %f" % (np.amin(rotation_values[start_index:end_index,0])) )
    print("Min Pitch: %f" % (np.amin(rotation_values[start_index:end_index,1])) )
    print("Min Yaw: %f" % (np.amin(rotation_values[start_index:end_index,2])) )

    position_figure.savefig(
        sys.argv[2] + "rectangular-gap-plot.pdf", bbox_inches='tight', format='pdf')

    position_figure.show()

    input()

def print_second_field_experiment(position_values, rotation_values, time_stamps):
    #"args": ["/media/russellb/Bradburrito/JFR2019/jfr_data/bags/2019-07-03/2019-07-03-11-58-41.bag", "/home/russellb/Dropbox/Apps/ShareLaTeX/Buchanan JFR 2019/figures/pdf/"],

    start_time = 0
    end_time = 65

    body_height_offset = 0.08
    body_height = 0.24
    mount_height = 0.13
    body_width = 0.27
    body_length = 0.531

    obstacle_above_start = 1.20
    obstacle_above_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_above_start)

    obstacle_above_end = 2.10
    obstacle_above_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_above_end)

    obstacle_right_start = 1.2
    obstacle_right_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_right_start)
    obstacle_right_end = 1.50
    obstacle_right_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_right_end)

    obstacle_left_start = 0.0
    obstacle_left_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_left_start)
    obstacle_left_end = 0.5
    obstacle_left_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_left_end)

    start_index = parser.convert_value_to_index(time_stamps, start_time)
    end_index = parser.convert_value_to_index(time_stamps, end_time)

    x_axis_values = time_stamps  # position_values

    plt.rcParams['axes.titlesize'] = 22
    plt.rcParams['axes.labelsize'] = 22
    plt.rcParams['xtick.labelsize'] = 22
    plt.rcParams['ytick.labelsize'] = 22
    plt.rcParams.update({'font.size': 20})
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
    position_figure = plt.figure(0, figsize=(16, 9), dpi=120)
    #position_figure.suptitle("Crumbling Wall", fontsize=30)
    left_ax1 = plt.subplot(3, 1, 1)
    plt.plot(x_axis_values[start_index:end_index],
             rotation_values[start_index:end_index, 0], '--', color=(1, 0, 0), label='Roll (degrees)')
    plt.xlabel('Time (s)')
    #plt.ylabel('Roll (degrees)')
    left_ax1.set_ylim(-45, 45)
    left_ax1.legend(loc="upper left")
######################################################################################################################################
    left_ax2 = plt.subplot(3, 1, 2)
    left_ax2.fill_between(x_axis_values[start_index:end_index, 0],
                              position_values[start_index:end_index,
                                              1] - body_width / 2.0,
                              position_values[start_index:end_index, 1] + body_width / 2.0, color=(0, 1, 0), alpha=0.1, label='Y Position (m)')
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 1] - body_width / 2.0, color=(0, 1, 0))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 1] + body_width / 2.0, color=(0, 1, 0))

    right_ax2 = left_ax2.twinx()
    right_ax2.plot(x_axis_values[start_index:end_index],
                                   rotation_values[start_index:end_index, 2], '--', color=(0, 0, 1), label="Yaw (degrees)")

    left_ax2.fill_between(x_axis_values[obstacle_right_start_idx:obstacle_right_end_idx, 0],
                              -0.02,
                              -0.6, color=(0, 0, 0), alpha=0.5)
    left_ax2.fill_between(x_axis_values[obstacle_left_start_idx:obstacle_left_end_idx, 0],
                              0.5,
                              0.29, color=(0, 0, 0), alpha=0.5)

    left_ax2.fill_between(x_axis_values[start_index:end_index, 0],
                              0.6,
                              0.5, color=(0, 0, 0), alpha=0.5)

    # position_ax2.fill_between(x_axis_values[left_obstacle_start_idx:left_obstacle_end_idx, 0],
    #                           0.25,
    #                           0.5, color=(0, 0, 0), alpha=0.5)

    left_ax2.legend(loc="upper left")
    left_ax2.set_ylim(-0.6, 0.6)
    right_ax2.legend(loc="upper right")
    right_ax2.set_ylim(-45, 45)
######################################################################################################################################
    left_ax3 = plt.subplot(3, 1, 3)
    left_ax3.fill_between(x_axis_values[start_index:end_index, 0],
                              position_values[start_index:end_index,
                                              2] + body_height_offset - body_height / 2.0,
                              position_values[start_index:end_index, 2] + body_height_offset + body_height / 2.0 + mount_height, color=(0, 0, 1), alpha=0.1, label='Z Position (m)')
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 2] + body_height_offset - body_height / 2.0, color=(0, 0, 1))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 2] + body_height_offset + body_height / 2.0 + mount_height, color=(0, 0, 1))

    right_ax3 = left_ax3.twinx()
    right_ax3.plot(x_axis_values[start_index:end_index],
                                   rotation_values[start_index:end_index, 1], '--', color=(0, 1, 0), label="Pitch (degrees)")


    left_ax3.fill_between(x_axis_values[obstacle_above_start_idx:obstacle_above_end_idx, 0],
                                1.0,
                                0.75, color=(0, 0, 0), alpha=0.5)


    left_ax3.set_xlabel('Time (s)')
    left_ax3.legend(loc="upper left")
    left_ax3.set_ylim(0, 1)
    right_ax3.legend(loc="upper right")
    right_ax3.set_ylim(-45, 45)

    min_height = np.amin(position_values[start_index:end_index,2])
    max_height = np.max(position_values[start_index:end_index,2])
    print("Min Height: %f (%f,%f)" % (min_height, min_height + body_height_offset - body_height / 2.0, 
                                        min_height + body_height_offset + body_height / 2.0 + mount_height))

    print("Max Height: %f (%f,%f)" % (max_height, max_height + body_height_offset - body_height / 2.0, 
                                        max_height + body_height_offset + body_height / 2.0 + mount_height))

    print("Max Roll: %f" % (np.amax(rotation_values[start_index:end_index,0])) )
    print("Max Pitch: %f" % (np.amax(rotation_values[start_index:end_index,1])) )
    print("Max Yaw: %f" % (np.amax(rotation_values[start_index:end_index,2])) )

    print("Min Roll: %f" % (np.amin(rotation_values[start_index:end_index,0])) )
    print("Min Pitch: %f" % (np.amin(rotation_values[start_index:end_index,1])) )
    print("Min Yaw: %f" % (np.amin(rotation_values[start_index:end_index,2])) )


    position_figure.savefig(
        sys.argv[2] + "crumbling-wall-plot.pdf", bbox_inches='tight', format='pdf')

    position_figure.show()

    input()


def plot_collapsed_building(position_values, rotation_values, time_stamps):
    #/media/raab/Bixby/JFR2019/jfr_data/bags/best_bags/2019-07-03-23-09-13.bag.active

    start_time = 10
    end_time = 100

    body_height_offset = 0.08
    body_height = 0.24
    mount_height = 0.13
    body_width = 0.27
    body_length = 0.531

    obstacle_above_start = 1.7
    obstacle_above_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_above_start)

    obstacle_above_end = 1.55
    obstacle_above_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_above_end)

    obstacle_below_start = 1.2
    obstacle_below_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_below_start)

    obstacle_below_end = 1.70
    obstacle_below_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_below_end)

    obstacle_right_start = 1.2
    obstacle_right_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_right_start)
    obstacle_right_end = 1.4
    obstacle_right_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_right_end)

    obstacle_left_start = 1.75
    obstacle_left_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_left_start)
    obstacle_left_end = 1.80
    obstacle_left_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_left_end)

    start_index = parser.convert_value_to_index(time_stamps, start_time)
    end_index = parser.convert_value_to_index(time_stamps, end_time)

    x_axis_values = time_stamps  # position_values

    plt.rcParams['axes.titlesize'] = 22
    plt.rcParams['axes.labelsize'] = 22
    plt.rcParams['xtick.labelsize'] = 22
    plt.rcParams['ytick.labelsize'] = 22
    plt.rcParams.update({'font.size': 20})
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
    position_figure = plt.figure(0, figsize=(16, 9), dpi=120)
    #position_figure.suptitle("Collapsed Building", fontsize=30)
    left_ax1 = plt.subplot(3, 1, 1)
    plt.plot(x_axis_values[start_index:end_index],
             rotation_values[start_index:end_index, 0], '--', color=(1, 0, 0), label='Roll (degrees)')
    plt.xlabel('Time (s)')
    #plt.ylabel('Roll (degrees)')
    left_ax1.set_ylim(-45, 45)
    left_ax1.legend(loc="upper left")
######################################################################################################################################
    left_ax2 = plt.subplot(3, 1, 2)
    left_ax2.fill_between(x_axis_values[start_index:end_index, 0],
                              position_values[start_index:end_index,
                                              1] - body_width / 2.0,
                              position_values[start_index:end_index, 1] + body_width / 2.0, color=(0, 1, 0), alpha=0.1, label='Y Position (m)')
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 1] - body_width / 2.0, color=(0, 1, 0))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 1] + body_width / 2.0, color=(0, 1, 0))

    right_ax2 = left_ax2.twinx()
    right_ax2.plot(x_axis_values[start_index:end_index],
                                   rotation_values[start_index:end_index, 2], '--', color=(0, 0, 1), label="Yaw (degrees)")

    left_ax2.fill_between(x_axis_values[obstacle_right_start_idx:obstacle_right_end_idx, 0],
                              -0.6,
                              -0.25, color=(0, 0, 0), alpha=0.5)
    left_ax2.fill_between(x_axis_values[obstacle_right_end_idx:end_index, 0],
                              0.65,
                              0.75, color=(0, 0, 0), alpha=0.5)

    left_ax2.legend(loc="upper left")
    left_ax2.set_ylim(-0.6, 0.6)
    right_ax2.legend(loc="upper right")
    right_ax2.set_ylim(-45, 45)
######################################################################################################################################
    left_ax3 = plt.subplot(3, 1, 3)
    left_ax3.fill_between(x_axis_values[start_index:end_index, 0],
                              position_values[start_index:end_index,
                                              2] + body_height_offset - body_height / 2.0,
                              position_values[start_index:end_index, 2] + body_height_offset + body_height / 2.0 + mount_height, color=(0, 0, 1), alpha=0.1, label='Z Position (m)')
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 2] + body_height_offset - body_height / 2.0, color=(0, 0, 1))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 2] + body_height_offset + body_height / 2.0 + mount_height, color=(0, 0, 1))

    right_ax3 = left_ax3.twinx()
    right_ax3.plot(x_axis_values[start_index:end_index],
                                   rotation_values[start_index:end_index, 1], '--', color=(0, 1, 0), label="Pitch (degrees)")

    obstacle_above = np.linspace(0.7,0.85,end_index-obstacle_above_start_idx)
    left_ax3.fill_between(x_axis_values[obstacle_above_start_idx:end_index, 0],
                              obstacle_above,
                              1.0, color=(0, 0, 0), alpha=0.5)

    left_ax3.fill_between(x_axis_values[start_index:obstacle_below_start_idx, 0],
                              -0.05,
                              0.0, color=(0, 0, 0), alpha=0.5)
    left_ax3.fill_between(x_axis_values[obstacle_below_end_idx:end_index, 0],
                              -0.05,
                              0.0, color=(0, 0, 0), alpha=0.5)

    left_ax3.set_xlabel('Time (s)')
    left_ax3.legend(loc="upper left")
    left_ax3.set_ylim(-0.05, 1)
    right_ax3.legend(loc="lower right")
    right_ax3.set_ylim(-45, 45)

    position_figure.savefig(
        sys.argv[2] + "collapsed-building-plot.pdf", bbox_inches='tight', format='pdf')

    min_height = np.amin(position_values[start_index:end_index,2])
    max_height = np.max(position_values[start_index:end_index,2])
    print("Min Height: %f (%f,%f)" % (min_height, min_height + body_height_offset - body_height / 2.0, 
                                        min_height + body_height_offset + body_height / 2.0 + mount_height))

    print("Max Height: %f (%f,%f)" % (max_height, max_height + body_height_offset - body_height / 2.0, 
                                        max_height + body_height_offset + body_height / 2.0 + mount_height))

    print("Max Roll: %f" % (np.amax(rotation_values[start_index:end_index,0])) )
    print("Max Pitch: %f" % (np.amax(rotation_values[start_index:end_index,1])) )
    print("Max Yaw: %f" % (np.amax(rotation_values[start_index:end_index,2])) )

    print("Min Roll: %f" % (np.amin(rotation_values[start_index:end_index,0])) )
    print("Min Pitch: %f" % (np.amin(rotation_values[start_index:end_index,1])) )
    print("Min Yaw: %f" % (np.amin(rotation_values[start_index:end_index,2])) )


    position_figure.show()

    input()


def print_anymal_foot_velocity(position_values):
  fig = plt.figure()
  ax = plt.axes()

  velocity_values = np.array(np.gradient(position_values, 1/400.0))

  probability =  np.array(np.gradient(expon.cdf(np.power( velocity_values[0,:,0], 2)), 0.5))

  print probability.shape

  ax.plot(position_values[:,0], color=(1, 0, 0))
  ax.plot(velocity_values[0,:,0], color=(0, 1, 0))
  ax.plot(probability, color=(0, 0, 1))

  fig.show()

  input()

if __name__ == "__main__":

    parser = BagParser(sys.argv[1])
    parser.parse()

    position_values = parser.get_rf_position()
    print_anymal_foot_velocity(position_values)

    # position_values = parser.get_pose_position()
    # rotation_values = parser.get_pose_euler_rotation()
    # time_stamps = parser.get_pose_time()
    # time_stamps = time_stamps - time_stamps[0]

    #print_low_indoor_experiment(position_values, rotation_values, time_stamps)
    #print_rotated_indoor_experiment(position_values, rotation_values, time_stamps)
    #print_step_indoor_experiment(position_values, rotation_values, time_stamps)
    #print_first_field_experiment(position_values, rotation_values, time_stamps)
    #print_second_field_experiment(position_values, rotation_values, time_stamps)
    #plot_collapsed_building(position_values, rotation_values, time_stamps)
