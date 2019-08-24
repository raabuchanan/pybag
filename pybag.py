#!/usr/bin/env python3
from BagParser import BagParser
import sys
import numpy as np
import matplotlib.pyplot as plt



def print_low_indoor_experiment(position_values, rotation_values, time_stamps):

    start_time = 0
    end_time = 100

    body_height_offset = 0.08
    body_height = 0.24
    mount_height = 0.11
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
    plt.rcParams['axes.labelsize'] = 20
    plt.rcParams['xtick.labelsize'] = 14
    plt.rcParams['ytick.labelsize'] = 14
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
    position_figure = plt.figure(0, figsize=(16, 9), dpi=120)
    position_figure.suptitle("Position and Rotation over Time", fontsize=30)
    left_ax1 = plt.subplot(3, 1, 1)
    plt.plot(x_axis_values[start_index:end_index],
             rotation_values[start_index:end_index, 0], color=(1, 0, 0), label='Roll (degrees)')
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
                                   rotation_values[start_index:end_index, 2], color=(0, 0, 1), label="Yaw (degrees)")


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
                                              2] + body_height_offset - body_height + mount_height / 2.0,
                              position_values[start_index:end_index, 2] + body_height_offset + body_height + mount_height / 2.0, color=(0, 0, 1), alpha=0.1, label='Z Position (m)')
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 2] + body_height_offset - body_height + mount_height / 2.0, color=(0, 0, 1))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 2] + body_height_offset + body_height + mount_height / 2.0, color=(0, 0, 1))

    right_ax3 = left_ax3.twinx()
    right_ax3.plot(x_axis_values[start_index:end_index],
                                   rotation_values[start_index:end_index, 1], color=(0, 1, 0), label="Pitch (degrees)")


    left_ax3.fill_between(x_axis_values[obstacle_above_start_idx:obstacle_above_end_idx, 0],
                                1.0,
                                0.6, color=(0, 0, 0), alpha=0.5)

    plt.xlabel('Time (s)')
    left_ax3.legend(loc="upper left")
    left_ax3.set_ylim(0, 1)
    right_ax3.legend(loc="upper right")
    right_ax3.set_ylim(-25, 25)

    position_figure.savefig(
        sys.argv[2] + "indoor-low-plot.pdf", bbox_inches='tight', format='pdf')

    position_figure.show()

    input()


def print_first_field_experiment(position_values, rotation_values, time_stamps):

    start_time = 0
    end_time = 55

    body_height_offset = 0.08
    body_height = 0.24
    mount_height = 0.11
    body_width = 0.27
    body_length = 0.531

    hole_start = 1.25
    length_hole = 0.3
    hole_start_idx = parser.convert_value_to_index(
        position_values[:, 0], hole_start)
    hole_end_idx = parser.convert_value_to_index(
        position_values[:, 0], hole_start + length_hole)
    hole_width = 0.75
    step_height = 0.1
    hole_height = 0.8

    start_index = parser.convert_value_to_index(time_stamps, start_time)
    end_index = parser.convert_value_to_index(time_stamps, end_time)

    x_axis_values = time_stamps  # position_values

    plt.rcParams['axes.titlesize'] = 22
    plt.rcParams['axes.labelsize'] = 20
    plt.rcParams['xtick.labelsize'] = 14
    plt.rcParams['ytick.labelsize'] = 14
######################################################################################################################################
    position_figure = plt.figure(0, figsize=(16, 9), dpi=120)
    position_figure.suptitle("Position over Time", fontsize=30)
    position_ax1 = plt.subplot(3, 1, 1)
    position_ax1.fill_between(x_axis_values[start_index:end_index, 0],
                              position_values[start_index:end_index,
                                              0] - body_length / 2.0,
                              position_values[start_index:end_index, 0] + body_length / 2.0, color=(1, 0, 0), alpha=0.1)
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 0] - body_length / 2.0, color=(1, 0, 0))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 0] + body_length / 2.0, color=(1, 0, 0))
    #plt.xlabel('Time (s)')
    plt.ylabel('X Position (m)')

    position_ax2 = plt.subplot(3, 1, 2)
    position_ax2.fill_between(x_axis_values[start_index:end_index, 0],
                              position_values[start_index:end_index,
                                              1] - body_width / 2.0,
                              position_values[start_index:end_index, 1] + body_width / 2.0, color=(0, 1, 0), alpha=0.1, label='Y Position (m)')
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 1] - body_width / 2.0, color=(0, 1, 0))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 1] + body_width / 2.0, color=(0, 1, 0))

    position_ax2_rotation_ax1 = position_ax2.twinx()
    position_ax2_rotation_ax1.plot(x_axis_values[start_index:end_index],
                                   rotation_values[start_index:end_index, 2], color=(0, 0, 1), label="Yaw (degrees)")

    position_ax2.fill_between(x_axis_values[hole_start_idx:hole_end_idx, 0],
                              -0.5,
                              -hole_width / 2.0, color=(0, 0, 0), alpha=0.5)
    position_ax2.fill_between(x_axis_values[hole_start_idx:hole_end_idx, 0],
                              hole_width / 2.0,
                              0.5, color=(0, 0, 0), alpha=0.5)

    #plt.xlabel('Time (s)')
    position_ax2.legend(loc="upper left")
    position_ax2.set_ylabel('Y Position (m)')
    position_ax2.set_ylim(-0.5, 0.5)
    position_ax2_rotation_ax1.legend(loc="upper right")
    position_ax2_rotation_ax1.set_ylabel('Yaw (degrees)')
    position_ax2_rotation_ax1.set_ylim(-5, 5)

    position_ax3 = plt.subplot(3, 1, 3)
    position_ax3.fill_between(x_axis_values[start_index:end_index, 0],
                              position_values[start_index:end_index,
                                              2] + body_height_offset - body_height + mount_height / 2.0,
                              position_values[start_index:end_index, 2] + body_height_offset + body_height + mount_height / 2.0, color=(0, 0, 1), alpha=0.1, label='Z Position (m)')
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 2] + body_height_offset - body_height + mount_height / 2.0, color=(0, 0, 1))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 2] + body_height_offset + body_height + mount_height / 2.0, color=(0, 0, 1))

    position_ax3_rotation_ax1 = position_ax3.twinx()
    position_ax3_rotation_ax1.plot(x_axis_values[start_index:end_index],
                                   rotation_values[start_index:end_index, 1], color=(0, 1, 0), label="Pitch (degrees)")

    position_ax3.fill_between(x_axis_values[hole_start_idx:hole_end_idx, 0],
                              step_height + hole_height,
                              step_height + hole_height + 1, color=(0, 0, 0), alpha=0.5)
    position_ax3.fill_between(x_axis_values[hole_start_idx:end_index, 0],
                              0,
                              step_height, color=(0, 0, 0), alpha=0.5)
    plt.xlabel('Time (s)')
    position_ax3.legend(loc="upper left")
    position_ax3.set_ylabel('Z Position (m)')
    position_ax3.set_ylim(0, 1)
    position_ax3_rotation_ax1.legend(loc="upper right")
    position_ax3_rotation_ax1.set_ylabel('Pitch (degrees)')
    position_ax3_rotation_ax1.set_ylim(-10, 10)

    position_figure.savefig(
        sys.argv[2] + "position_figure.pdf", bbox_inches='tight', format='pdf')

    position_figure.show()
#########################################################################################################################################
    rotation_figure = plt.figure(1, figsize=(16, 9), dpi=120)
    rotation_figure.suptitle("Rotation over Time", fontsize=30)
    plt.subplot(3, 1, 1)
    plt.plot(x_axis_values[start_index:end_index],
             rotation_values[start_index:end_index, 0], color=(1, 0, 0))
    #plt.xlabel('Time (s)')
    plt.ylabel('Roll (degrees)')
    plt.ylim(-10, 10)

    plt.subplot(3, 1, 2)
    plt.plot(x_axis_values[start_index:end_index],
             rotation_values[start_index:end_index, 1], color=(0, 1, 0))
    #plt.xlabel('Time (s)')
    plt.ylabel('Pitch (degrees)')
    plt.ylim(-10, 10)

    plt.subplot(3, 1, 3)
    plt.plot(x_axis_values[start_index:end_index],
             rotation_values[start_index:end_index, 2], color=(0, 0, 1))
    plt.xlabel('Time (s)')
    plt.ylabel('Yaw (degrees)')
    plt.ylim(-10, 10)

    rotation_figure.savefig(
        sys.argv[2] + "rotation_figure.pdf", bbox_inches='tight', format='pdf')

    rotation_figure.show()

    input()


def print_second_field_experiment(position_values, rotation_values, time_stamps):

    start_time = 0
    end_time = 50

    body_height_offset = 0.08
    body_height = 0.24
    mount_height = 0.11
    body_width = 0.27
    body_length = 0.531

    hole_start = 1.20
    length_hole = 0.3
    hole_start_idx = parser.convert_value_to_index(
        position_values[:, 0], hole_start)
    hole_end_idx = parser.convert_value_to_index(
        position_values[:, 0], hole_start + length_hole)
    hole_width = 0.75
    step_height = 0.0
    hole_height = 0.62

    left_obstacle_start = 0.0
    left_obstacle_end = 0.5

    left_obstacle_start_idx = parser.convert_value_to_index(
        position_values[:, 0], left_obstacle_start)
    left_obstacle_end_idx = parser.convert_value_to_index(
        position_values[:, 0], left_obstacle_end)

    start_index = parser.convert_value_to_index(time_stamps, start_time)
    end_index = parser.convert_value_to_index(time_stamps, end_time)

    x_axis_values = time_stamps  # position_values

    plt.rcParams['axes.titlesize'] = 22
    plt.rcParams['axes.labelsize'] = 20
    plt.rcParams['xtick.labelsize'] = 14
    plt.rcParams['ytick.labelsize'] = 14
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
    position_figure = plt.figure(0, figsize=(16, 9), dpi=120)
    position_figure.suptitle("Position over Time", fontsize=30)
    position_ax1 = plt.subplot(3, 1, 1)
    position_ax1.fill_between(x_axis_values[start_index:end_index, 0],
                              position_values[start_index:end_index,
                                              0] - body_length / 2.0,
                              position_values[start_index:end_index, 0] + body_length / 2.0, color=(1, 0, 0), alpha=0.1)
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 0] - body_length / 2.0, color=(1, 0, 0))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 0] + body_length / 2.0, color=(1, 0, 0))
    #plt.xlabel('Time (s)')
    plt.ylabel('X Position (m)')
######################################################################################################################################
    position_ax2 = plt.subplot(3, 1, 2)
    position_ax2.fill_between(x_axis_values[start_index:end_index, 0],
                              position_values[start_index:end_index,
                                              1] - body_width / 2.0,
                              position_values[start_index:end_index, 1] + body_width / 2.0, color=(0, 1, 0), alpha=0.1, label='Y Position (m)')
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 1] - body_width / 2.0, color=(0, 1, 0))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 1] + body_width / 2.0, color=(0, 1, 0))

    position_ax2_rotation_ax1 = position_ax2.twinx()
    position_ax2_rotation_ax1.plot(x_axis_values[start_index:end_index],
                                   rotation_values[start_index:end_index, 2], color=(0, 0, 1), label="Yaw (degrees)")

    position_ax2.fill_between(x_axis_values[hole_start_idx:hole_end_idx, 0],
                              -0.25,
                              -0.04, color=(0, 0, 0), alpha=0.5)
    position_ax2.fill_between(x_axis_values[start_index:end_index, 0],
                              0.5,
                              1.0, color=(0, 0, 0), alpha=0.5)
    position_ax2.fill_between(x_axis_values[left_obstacle_start_idx:left_obstacle_end_idx, 0],
                              0.25,
                              0.5, color=(0, 0, 0), alpha=0.5)
    #plt.xlabel('Time (s)')
    position_ax2.legend(loc="upper left")
    position_ax2.set_ylabel('Y Position (m)')
    position_ax2.set_ylim(-0.25, 1.0)
    position_ax2_rotation_ax1.legend(loc="upper right")
    position_ax2_rotation_ax1.set_ylabel('Yaw (degrees)')
    position_ax2_rotation_ax1.set_ylim(-15, 15)
######################################################################################################################################
    position_ax3 = plt.subplot(3, 1, 3)
    position_ax3.fill_between(x_axis_values[start_index:end_index, 0],
                              position_values[start_index:end_index,
                                              2] + body_height_offset - body_height + mount_height / 2.0,
                              position_values[start_index:end_index, 2] + body_height_offset + body_height + mount_height / 2.0, color=(0, 0, 1), alpha=0.1, label='Z Position (m)')
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 2] + body_height_offset - body_height + mount_height / 2.0, color=(0, 0, 1))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 2] + body_height_offset + body_height + mount_height / 2.0, color=(0, 0, 1))

    position_ax3_rotation_ax1 = position_ax3.twinx()
    position_ax3_rotation_ax1.plot(x_axis_values[start_index:end_index],
                                   rotation_values[start_index:end_index, 1], color=(0, 1, 0), label="Pitch (degrees)")

    position_ax3.fill_between(x_axis_values[hole_start_idx:hole_end_idx, 0],
                              step_height + hole_height,
                              step_height + hole_height + 1, color=(0, 0, 0), alpha=0.5)
    position_ax3.fill_between(x_axis_values[hole_start_idx:end_index, 0],
                              0,
                              step_height, color=(0, 0, 0), alpha=0.5)
    plt.xlabel('Time (s)')
    position_ax3.legend(loc="upper left")
    position_ax3.set_ylabel('Z Position (m)')
    position_ax3.set_ylim(0, 1)
    position_ax3_rotation_ax1.legend(loc="upper right")
    position_ax3_rotation_ax1.set_ylabel('Pitch (degrees)')
    position_ax3_rotation_ax1.set_ylim(-25, 25)

    position_figure.savefig(
        sys.argv[2] + "position_figure.pdf", bbox_inches='tight', format='pdf')

    position_figure.show()
    ######################################################################################################################################
    ######################################################################################################################################
#########################################################################################################################################
    # rotation_figure = plt.figure(1, figsize=(16, 9), dpi=120)
    # rotation_figure.suptitle("Rotation over Time", fontsize=30)
    # plt.subplot(3, 1, 1)
    # plt.plot(x_axis_values[start_index:end_index],
    #          rotation_values[start_index:end_index, 0], color=(1, 0, 0))
    # #plt.xlabel('Time (s)')
    # plt.ylabel('Roll (degrees)')
    # plt.ylim(-10, 10)

    # plt.subplot(3, 1, 2)
    # plt.plot(x_axis_values[start_index:end_index],
    #          rotation_values[start_index:end_index, 1], color=(0, 1, 0))
    # #plt.xlabel('Time (s)')
    # plt.ylabel('Pitch (degrees)')
    # plt.ylim(-10, 10)

    # plt.subplot(3, 1, 3)
    # plt.plot(x_axis_values[start_index:end_index],
    #          rotation_values[start_index:end_index, 2], color=(0, 0, 1))
    # plt.xlabel('Time (s)')
    # plt.ylabel('Yaw (degrees)')
    # plt.ylim(-10, 10)

    # rotation_figure.savefig(
    #     sys.argv[2] + "rotation_figure.pdf", bbox_inches='tight', format='pdf')

    # rotation_figure.show()

    input()


def plot_collapsed_building(position_values, rotation_values, time_stamps):

    start_time = 10
    end_time = 100

    body_height_offset = 0.08
    body_height = 0.24
    mount_height = 0.11
    body_width = 0.27
    body_length = 0.531

    obstacle_above_start = 1.7
    obstacle_above_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_above_start)

    obstacle_right_start = 1.2
    obstacle_right_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_right_start)
    obstacle_right_end = 1.4
    obstacle_right_end_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_right_end)

    obstacle_left_start = 9*0.25
    obstacle_left_start_idx = parser.convert_value_to_index(
        position_values[:, 0], obstacle_left_start)


    start_index = parser.convert_value_to_index(time_stamps, start_time)
    end_index = parser.convert_value_to_index(time_stamps, end_time)

    x_axis_values = time_stamps  # position_values

    plt.rcParams['axes.titlesize'] = 22
    plt.rcParams['axes.labelsize'] = 20
    plt.rcParams['xtick.labelsize'] = 14
    plt.rcParams['ytick.labelsize'] = 14
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
    position_figure = plt.figure(0, figsize=(16, 9), dpi=120)
    position_figure.suptitle("Position over Time", fontsize=30)
    left_ax1 = plt.subplot(3, 1, 1)
    plt.plot(x_axis_values[start_index:end_index],
             rotation_values[start_index:end_index, 0], color=(1, 0, 0), label='Roll (degrees)')
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
                                   rotation_values[start_index:end_index, 2], color=(0, 0, 1), label="Yaw (degrees)")


    left_ax2.fill_between(x_axis_values[obstacle_right_start_idx:obstacle_right_end_idx, 0],
                              -0.4,
                              -0.25, color=(0, 0, 0), alpha=0.5)
    left_ax2.fill_between(x_axis_values[obstacle_right_end_idx:end_index, 0],
                              0.65,
                              0.75, color=(0, 0, 0), alpha=0.5)

    left_ax2.legend(loc="upper left")
    left_ax2.set_ylim(-0.4, 0.4)
    right_ax2.legend(loc="upper right")
    right_ax2.set_ylim(-45, 45)
######################################################################################################################################
    left_ax3 = plt.subplot(3, 1, 3)
    left_ax3.fill_between(x_axis_values[start_index:end_index, 0],
                              position_values[start_index:end_index,
                                              2] + body_height_offset - body_height + mount_height / 2.0,
                              position_values[start_index:end_index, 2] + body_height_offset + body_height + mount_height / 2.0, color=(0, 0, 1), alpha=0.1, label='Z Position (m)')
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 2] + body_height_offset - body_height + mount_height / 2.0, color=(0, 0, 1))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 2] + body_height_offset + body_height + mount_height / 2.0, color=(0, 0, 1))

    right_ax3 = left_ax3.twinx()
    right_ax3.plot(x_axis_values[start_index:end_index],
                                   rotation_values[start_index:end_index, 1], color=(0, 1, 0), label="Pitch (degrees)")

    obstacle_above = np.linspace(0.7,0.85,end_index-obstacle_above_start_idx)
    left_ax3.fill_between(x_axis_values[obstacle_above_start_idx:end_index, 0],
                              obstacle_above,
                              1.0, color=(0, 0, 0), alpha=0.5)
    plt.xlabel('Time (s)')
    left_ax3.legend(loc="upper left")
    left_ax3.set_ylim(0, 1)
    right_ax3.legend(loc="upper right")
    right_ax3.set_ylim(-25, 25)

    position_figure.savefig(
        sys.argv[2] + "position_figure.pdf", bbox_inches='tight', format='pdf')

    position_figure.show()

    input()


if __name__ == "__main__":

    parser = BagParser(sys.argv[1])
    parser.parse()

    position_values = parser.get_pose_position()
    rotation_values = parser.get_pose_euler_rotation()
    time_stamps = parser.get_pose_time()
    time_stamps = time_stamps - time_stamps[0]

    print_low_indoor_experiment(position_values, rotation_values, time_stamps)
    #print_first_field_experiment(position_values, rotation_values, time_stamps)
    #print_second_field_experiment(position_values, rotation_values, time_stamps)
    #plot_collapsed_building(position_values, rotation_values, time_stamps)
