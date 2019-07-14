import rosbag
import numpy as np
from scipy.spatial.transform import Rotation

class PoseWithCovariance:
    def __init__(self):
        self.position_arr = np.empty((0, 3), np.double)
        self.euler_rotation_arr = np.empty((0, 3), np.double)
        self.time_arr = np.empty((0, 1), np.double)

    def load_messages(self, messages):
      for _, msg, t in messages:
          [r, p, y] = self.convert_quat_to_rpy(
              msg.pose.pose.orientation.w, msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z)
          self.position_arr = np.append(self.position_arr, np.array(
              [[msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z]]), axis=0)
          self.euler_rotation_arr = np.append(self.euler_rotation_arr, np.array(
              [[r, p, y]]), axis=0)
          self.time_arr = np.append(self.time_arr, np.array(
              [[t.secs + t.nsecs*1e-9]]), axis=0)

    def convert_quat_to_rpy(self, w, x, y, z):
        r = Rotation.from_quat([x, y, z, w])
        return r.as_euler('xyz', degrees=True)