import rosbag
import numpy as np
from scipy.spatial.transform import Rotation

class AnymalState:
    def __init__(self):
        self.rf_position = np.empty((0, 3), np.double)

    def load_messages(self, messages):
      for _, msg, t in messages:
        for contact in msg.contacts:
          if contact.name == "RF_FOOT":
            self.rf_position = np.append(self.rf_position, np.array(
                [[contact.position.x, contact.position.y, contact.position.z]]), axis=0)