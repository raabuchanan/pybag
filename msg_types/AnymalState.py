import rosbag
import numpy as np
from scipy.spatial.transform import Rotation


class AnymalState:
    def __init__(self):
        self.rf_position = np.empty((0, 3), np.double)
        self.state_times = np.empty((0, 1), np.double)

    def load_messages(self, messages):
        i = 0
        for msg in messages:
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