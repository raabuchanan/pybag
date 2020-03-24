import rosbag
import numpy as np
from scipy.spatial.transform import Rotation


class AnymalState:
    def __init__(self):
        self.base_position = np.empty((0, 3), np.double)
        self.base_rotation = np.empty((0, 4), np.double)
        self.rf_position = np.empty((0, 3), np.double)
        self.state_times = np.empty((0, 1), np.double)

    def load_messages(self, messages):
        i = 0
        for msg in messages:
            self.base_position = np.append(self.base_position, np.array(
                [[msg.message.pose.pose.position.x,
                  msg.message.pose.pose.position.y,
                  msg.message.pose.pose.position.z]]), axis=0)
            self.base_rotation = np.append(self.base_rotation, np.array([[msg.message.pose.pose.orientation.x,
                                    msg.message.pose.pose.orientation.y, msg.message.pose.pose.orientation.z,
                                    msg.message.pose.pose.orientation.w]]), axis=0)
            if msg.message.contacts[1].state != 0:
                self.rf_position = np.append(self.rf_position, np.array(
                    [[msg.message.contacts[1].position.x, msg.message.contacts[1].position.y, msg.message.contacts[1].position.z]]), axis=0)
                self.state_times = np.append(self.state_times, np.array(
                    [[msg.timestamp.secs + msg.timestamp.nsecs*1e-9]]), axis=0)
            try:
                next(messages)
                next(messages)
                next(messages)
            except StopIteration:
                break
            if i % 100000 == 0:
                print(i, "messages processed")
            i = i + 4