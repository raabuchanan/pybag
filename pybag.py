#!/usr/bin/env python3
import sys
import rosbag
import matplotlib.pyplot as plt
import numpy as np

from scipy.spatial.transform import Rotation
from msg_types.PoseWithCovariance import PoseWithCovariance


class BagParser:
    def __init__(self, bag_string):
        self.bag = rosbag.Bag(bag_string)
        self.pose = PoseWithCovariance()

    def parse(self):
        topics = self.bag.get_type_and_topic_info().topics
        for topic, topic_info in topics.items():
            if topic_info.msg_type == "geometry_msgs/PoseWithCovarianceStamped":
                print(topic)
                self.pose.load_messages(self.bag.read_messages(topics=[topic]))

    def get_pose_position(self):
        return self.pose.position_arr

    def get_pose_euler_rotation(self):
        return self.pose.euler_rotation_arr

    def get_pose_time(self):
        return self.pose.time_arr

    # return index of closest timestamp to given time
    def convert_value_to_index(self, data_arr, val):
        return (np.abs(data_arr - val)).argmin()

    def __del__(self):
        self.bag.close()


if __name__ == "__main__":

    parser = BagParser(sys.argv[1])
    parser.parse()

    position_values = parser.get_pose_position()
    rotation_valuse = parser.get_pose_euler_rotation()
    time_stamps = parser.get_pose_time()
    time_stamps = time_stamps - time_stamps[0]

    start_time = 0
    end_time = 55

    body_height_offset = 0.08
    body_height = 0.24
    mount_height = 0.11
    body_width = 0.27
    body_length = 0.531

    hole_start = 1.25
    length_hole = 0.3
    hole_start_idx = parser.convert_value_to_index(position_values[:,0], hole_start)
    hole_end_idx = parser.convert_value_to_index(position_values[:,0], hole_start + length_hole)
    hole_width = 0.75
    step_height = 0.1
    hole_height = 0.8


    start_index = parser.convert_value_to_index(time_stamps, start_time)
    end_index = parser.convert_value_to_index(time_stamps, end_time)

    x_axis_values = time_stamps #position_values
    

    position_figure = plt.figure(0, figsize=(16, 9), dpi=120)
    position_figure.suptitle("Position over time")
    position_ax1 = plt.subplot(3, 1, 1)
    position_ax1.fill_between(x_axis_values[start_index:end_index, 0],
                     position_values[start_index:end_index,
                                     0] - body_length / 2.0,
                     position_values[start_index:end_index, 0] + body_length / 2.0, color=(1, 0, 0), alpha=0.1)
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 0] - body_length / 2.0, color=(1, 0, 0))
    plt.plot(x_axis_values[start_index:end_index],
             position_values[start_index:end_index, 0] + body_length / 2.0, color=(1, 0, 0))
    plt.xlabel('Time (s)')
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
            rotation_valuse[start_index:end_index, 2], color=(0, 0, 1), label="Yaw (degrees)")

    position_ax2.fill_between(x_axis_values[hole_start_idx:hole_end_idx, 0],
                     -0.5,
                      -hole_width / 2.0, color=(0, 0, 0), alpha=0.5)
    position_ax2.fill_between(x_axis_values[hole_start_idx:hole_end_idx, 0],
                     hole_width / 2.0,
                     0.5, color=(0, 0, 0), alpha=0.5)

    plt.xlabel('Time (s)')
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
            rotation_valuse[start_index:end_index, 1], color=(0, 1, 0), label="Pitch (degrees)")

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
    position_ax3_rotation_ax1.set_ylim(-5, 5)
    

    position_figure.savefig(
        sys.argv[2] + "position_figure.pdf", bbox_inches='tight', format='pdf')

    position_figure.show()

    rotation_figure = plt.figure(1, figsize=(16, 9), dpi=120)
    rotation_figure.suptitle("Rotation over time")
    plt.subplot(3, 1, 1)
    plt.plot(x_axis_values[start_index:end_index],
             rotation_valuse[start_index:end_index, 0], color=(1, 0, 0))
    plt.xlabel('Time (s)')
    plt.ylabel('Roll (degrees)')
    plt.ylim(-5, 5)

    plt.subplot(3, 1, 2)
    plt.plot(x_axis_values[start_index:end_index],
             rotation_valuse[start_index:end_index, 1], color=(0, 1, 0))
    plt.xlabel('Time (s)')
    plt.ylabel('Pitch (degrees)')
    plt.ylim(-5, 5)

    plt.subplot(3, 1, 3)
    plt.plot(x_axis_values[start_index:end_index],
             rotation_valuse[start_index:end_index, 2], color=(0, 0, 1))
    plt.xlabel('Time (s)')
    plt.ylabel('Yaw (degrees)')
    plt.ylim(-5, 5)

    rotation_figure.savefig(
        sys.argv[2] + "rotation_figure.pdf", bbox_inches='tight', format='pdf')

    rotation_figure.show()

    input()
