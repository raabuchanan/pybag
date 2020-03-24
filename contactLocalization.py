#!/usr/bin/env python2.7
from BagParser import BagParser
import datetime
import time
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
from plyfile import PlyData, PlyElement
from scipy.spatial.transform import Rotation



def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def find_nearest_idx(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx



def print_leica_ts16(ground_truth_position_values, robot_position_values, ground_truth_times, robot_times):

    start_time = 0
    end_time = 350


    gt_start_index = parser.convert_value_to_index(ground_truth_times, start_time)
    gt_end_index = parser.convert_value_to_index(ground_truth_times, end_time)

    robot_start_index = parser.convert_value_to_index(robot_times, start_time)
    robot_end_index = parser.convert_value_to_index(robot_times, end_time)

    x_axis_values = ground_truth_times  # ground_truth_position_values

    plt.rcParams['axes.titlesize'] = 22
    plt.rcParams['axes.labelsize'] = 22
    plt.rcParams['xtick.labelsize'] = 22
    plt.rcParams['ytick.labelsize'] = 22
    plt.rcParams.update({'font.size': 20})
# Top
    position_figure = plt.figure(0, figsize=(16, 9), dpi=120)
    left_ax1 = plt.subplot(3, 1, 1)
    plt.plot(x_axis_values[gt_start_index:gt_end_index],
             ground_truth_position_values[gt_start_index:gt_end_index, 0], '--', color=(1, 0, 0), label='X (m)')
    plt.plot(robot_times[robot_start_index:robot_end_index],
             robot_position_values[robot_start_index:robot_end_index, 0], '--', color=(0, 1, 0), label='X (m)')
    #left_ax1.set_ylim(-45, 45)
    left_ax1.legend(loc="upper left")

# Middle
    left_ax2 = plt.subplot(3, 1, 2)
    plt.plot(x_axis_values[gt_start_index:gt_end_index],
             ground_truth_position_values[gt_start_index:gt_end_index, 1], '--', color=(1, 0, 0), label='Y (m)')
    plt.plot(robot_times[robot_start_index:robot_end_index],
             robot_position_values[robot_start_index:robot_end_index, 1], '--', color=(0, 1, 0), label='Y (m)')
    left_ax2.legend(loc="upper left")
    #left_ax2.set_ylim(-0.6, 0.6)
######################################################################################################################################
    left_ax3 = plt.subplot(3, 1, 3)
    plt.plot(x_axis_values[gt_start_index:gt_end_index],
             ground_truth_position_values[gt_start_index:gt_end_index, 2], '--', color=(1, 0, 0), label='Z (m)')
    plt.plot(robot_times[robot_start_index:robot_end_index],
             robot_position_values[robot_start_index:robot_end_index, 2], '--', color=(0, 1, 0), label='Z (m)')
    left_ax3.set_xlabel('Time (s)')
    left_ax3.legend(loc="upper left")
    #left_ax3.set_ylim(0, 1)

    # position_figure.savefig(
    #     sys.argv[2] + "indoor-low-plot.pdf", bbox_inches='tight', format='pdf')



    position_figure.show()

    input()






if __name__ == "__main__":

    print("Loading ROSbag")
    parser = BagParser(sys.argv[1])
    print("Parsing bag")
    parser.parse()

    base_positions = parser.get_base_position()
    base_rotations = parser.get_base_rotation()
    base_times = parser.get_state_times()

    base_positions = np.subtract(base_positions, base_positions[0,:])
    base_times = np.subtract(base_times, base_times[0])

    tf_positions = parser.get_tf_positions()
    tf_rotations = parser.get_tf_rotations()
    tf_times = parser.get_tf_times()

    ground_truth_positions = np.empty((0, 3), np.double)
    ground_truth_rotations = np.empty((0, 1), np.double) # Yaw only
    ground_truth_times = np.empty((0, 1), np.double)

    # Leica TS16
    print("Ground Truth")
    file = open(sys.argv[2], "rU")
    reader = csv.reader(file, delimiter=',')
    skip = True
    first_time = -1.0
    first_position = np.empty((0, 3), np.double)
    for row in reader:
            if(row[0] == "Auto_00097"):
                skip = False

            if(skip):
                continue

            x = float(row[1]) - 1000.0
            y = float(row[2]) - 1000.0
            z = float(row[3])
            input_time = row[4].split(":")
            # hr:min:sec.xx
            leica_time = 60*60*float(input_time[0]) + 60*float(input_time[1]) + float(input_time[2])

            if(first_time < 0.0):
                first_time = leica_time
                first_position = np.array([x,y,z])

            ground_truth_positions = np.append(ground_truth_positions, np.array([[x - first_position[0], y - first_position[1], z - first_position[2]]]), axis=0)
            ground_truth_times = np.append(ground_truth_times, np.array([[leica_time - first_time]]), axis=0)

    # transform base pose
    # for i in range(base_times.shape[0]):
    #   tf_time_idx = find_nearest_idx(tf_times, base_times[i])
    #   rotation_trasform = Rotation.from_quat(tf_rotations[tf_time_idx]).inv()
    #   position_transform = tf_positions[tf_time_idx]

    #   base_positions[i,:] = rotation_trasform.apply(base_positions[i,:]) - position_transform


    print_leica_ts16(ground_truth_positions, base_positions, ground_truth_times, base_times)