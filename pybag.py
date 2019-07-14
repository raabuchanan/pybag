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
    def convert_time_to_index(self, time_arr, time):
        return (np.abs(time_arr - time)).argmin()

    def __del__(self):
        self.bag.close()


if __name__ == "__main__":

    parser = BagParser(sys.argv[1])
    parser.parse()

    start_time = 0
    end_time = 55

    position_values = parser.get_pose_position()
    rotation_valuse = parser.get_pose_euler_rotation()
    x_axis_values = parser.get_pose_time()
    x_axis_values = x_axis_values - x_axis_values[0]

    start_index = parser.convert_time_to_index(x_axis_values, start_time)
    end_index = parser.convert_time_to_index(x_axis_values, end_time)

    position_figure = plt.figure(0)
    plt.subplot(3,1,1)
    plt.plot(x_axis_values[start_index:end_index], position_values[start_index:end_index,0], color=(1,0,0))
    plt.xlabel('Time (s)')
    plt.ylabel('X Position (m)')

    plt.subplot(3,1,2)
    plt.plot(x_axis_values[start_index:end_index], position_values[start_index:end_index,1], color=(0,1,0))
    plt.xlabel('Time (s)')
    plt.ylabel('Y Position (m)')

    plt.subplot(3,1,3)
    plt.plot(x_axis_values[start_index:end_index], position_values[start_index:end_index,2], color=(0,0,1))
    plt.xlabel('Time (s)')
    plt.ylabel('Z Position (m)')

    position_figure.savefig(sys.argv[2] + "position_figure.pdf", bbox_inches='tight')

    position_figure.show()
       

    rotation_figure = plt.figure(1)
    plt.subplot(3,1,1)
    plt.plot(x_axis_values[start_index:end_index], rotation_valuse[start_index:end_index,0], color=(1,0,0))
    plt.xlabel('Time (s)')
    plt.ylabel('Roll (degrees)')
    plt.ylim(-5, 5)

    plt.subplot(3,1,2)
    plt.plot(x_axis_values[start_index:end_index], rotation_valuse[start_index:end_index,1], color=(0,1,0))
    plt.xlabel('Time (s)')
    plt.ylabel('Pitch (degrees)')
    plt.ylim(-5, 5)

    plt.subplot(3,1,3)
    plt.plot(x_axis_values[start_index:end_index], rotation_valuse[start_index:end_index,2], color=(0,0,1))
    plt.xlabel('Time (s)')
    plt.ylabel('Yaw (degrees)')
    plt.ylim(-5, 5)

    rotation_figure.savefig(sys.argv[2] + "rotation_figure.pdf", bbox_inches='tight')

    rotation_figure.show()


    input()