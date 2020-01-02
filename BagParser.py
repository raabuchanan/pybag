#!/usr/bin/env python3
import rosbag
from msg_types.PoseWithCovariance import PoseWithCovariance
from msg_types.AnymalState import AnymalState
from msg_types.TFMessage import TFMessage
from scipy.spatial.transform import Rotation
import numpy as np


class BagParser:
    def __init__(self, bag_string):
        self.bag = rosbag.Bag(bag_string)
        self.pose = PoseWithCovariance()
        self.state = AnymalState()
        self.transform = TFMessage()

    def parse(self):
        topics = self.bag.get_type_and_topic_info().topics
        for topic, topic_info in topics.items():
            # if topic_info.msg_type == "geometry_msgs/PoseWithCovarianceStamped":
            #     print(topic)
            #     self.pose.load_messages(self.bag.read_messages(topics=[topic]))
            if topic_info.msg_type == "anymal_msgs/AnymalState":
                print(topic)
                self.state.load_messages(
                    self.bag.read_messages(topics=[topic]))
            if topic == "/tf" and topic_info.msg_type == "tf2_msgs/TFMessage":
                print(topic)
                self.transform.load_messages(
                    self.bag.read_messages(topics=[topic]))

    def get_pose_position(self):
        return self.pose.position_arr

    def get_pose_euler_rotation(self):
        return self.pose.euler_rotation_arr

    def get_pose_time(self):
        return self.pose.time_arr

    def get_rf_position(self):
        return self.state.rf_position

    def get_state_times(self):
        return self.state.state_times

    def get_tf_positions(self):
        return self.transform.tf_position_arr

    def get_tf_rotations(self):
        return self.transform.tf_rotation_arr

    def get_tf_times(self):
        return self.transform.tf_times

    def get_icp_tf_positions(self):
        return self.transform.icp_tf_position_arr

    def get_icp_tf_rotations(self):
        return self.transform.icp_tf_rotation_arr

    def get_icp_tf_times(self):
        return self.transform.icp_tf_times

    # return index of closest timestamp to given time
    def convert_value_to_index(self, data_arr, val):
        return (np.abs(data_arr - val)).argmin()

    def __del__(self):
        self.bag.close()
