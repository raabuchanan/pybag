import rosbag
import numpy as np
from scipy.spatial.transform import Rotation


class TFMessage:
    def __init__(self):
        self.tf_position_arr = np.empty((0, 3), np.double)
        self.tf_rotation_arr = np.empty((0, 4), np.double)
        self.tf_times = np.empty((0, 1), np.double)

    def load_messages(self, messages):
        for _, msg, t in messages:
            for transform in msg.transforms:
                if transform.header.frame_id == "odom" and transform.child_frame_id == "map":

                    self.tf_position_arr = np.append(self.tf_position_arr, np.array(
                        [[transform.transform.translation.x,
                          transform.transform.translation.y,
                          transform.transform.translation.z]]), axis=0)
                    self.tf_rotation_arr = np.append(self.tf_rotation_arr, np.array([[transform.transform.rotation.x,
                                            transform.transform.rotation.y, transform.transform.rotation.z,
                                            transform.transform.rotation.w]]), axis=0)
                    self.tf_times = np.append(self.tf_times, np.array(
                        [[t.secs + t.nsecs*1e-9]]), axis=0)

    def convert_quat_to_rpy(self, w, x, y, z):
        r = Rotation.from_quat([x, y, z, w])
        return r.as_euler('xyz', degrees=True)
