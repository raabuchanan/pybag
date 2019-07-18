#!/usr/bin/env python3
import rosbag
from msg_types.PoseWithCovariance import PoseWithCovariance
from scipy.spatial.transform import Rotation
import numpy as np

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
