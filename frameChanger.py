#!/usr/bin/env python3
from BagParser import BagParser
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


if __name__ == "__main__":

    print("Loading ROSbag")
    parser = BagParser(sys.argv[1])
    print("Parsing bag")
    parser.parse()

    contact_positions = parser.get_rf_position()
    contact_times = parser.get_state_times()

    tf_positions = parser.get_tf_positions()
    tf_rotations = parser.get_tf_rotations()
    tf_times = parser.get_tf_times()

    # icp_tf_positions = parser.get_icp_tf_positions()
    # icp_tf_rotations = parser.get_icp_tf_rotations()
    # icp_tf_times = parser.get_icp_tf_times()

    map_counter = 1
    file = open('/home/russell/sewer_probing_assets/mission3/re_processed_contact_maps/times.csv', "rU")
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        time = float(row[1])*1e-9
        print("Processing ", row[0], " at time ", time)
        contact_map = PlyData.read('/home/russell/sewer_probing_assets/mission3/re_processed_contact_maps/map' + str(map_counter) +'.ply')

        contact_time_idx_start = find_nearest_idx(contact_times, time)
        contact_time_idx_end = find_nearest_idx(contact_times, time + 3)

        colorized_counter = 0
        for contact_time_idx in range(0, 1, 4):
            tf_time_idx = find_nearest_idx(tf_times, contact_times[contact_time_idx][0])
            # print("tf_times", tf_times[0][0])
            # print("tf_time", tf_times[tf_time_idx][0], "contact_times[contact_time_idx][0]", contact_times[contact_time_idx][0])
            # print("tf_times", tf_times[-1][0])
            transformed_contact = np.array([0,0,0])
            if map_counter >= 0:
                x = np.median(contact_map['vertex']['x'])
                y = np.median(contact_map['vertex']['y'])
                z = np.median(contact_map['vertex']['z'])
                # Map to odom
                #rotation = Rotation.from_quat(tf_rotations[tf_time_idx])
                transformed_contact = np.array([x, y, z])
                #position = rotation.apply(position) + tf_positions[tf_time_idx]

                # nearest_contact_idx = find_nearest_idx(contact_positions[:,0], position[0])
                # contact_time_idx_start = nearest_contact_idx
                # contact_time_idx_end = find_nearest_idx(contact_times, contact_times[nearest_contact_idx][0] + 5)

            else:
                contact = contact_positions[contact_time_idx]

                rotation = Rotation.from_quat(tf_rotations[tf_time_idx]).inv()
                transformed_contact = rotation.apply(contact) - tf_positions[tf_time_idx]
                #print("TF position: ", tf_positions[tf_time_idx], "TF rotation: ", rotation)

                              
            #print("Contact ", contact_time_idx, "/", contact_time_idx_end)
            if contact_time_idx == contact_time_idx_start:
                print("Position in Map: ", transformed_contact)
                print("Original time: ", time)
                print("Conctact time: ", contact_times[contact_time_idx_start][0])
                print("Transform time: ", tf_times[tf_time_idx][0])

            local_colorized_counter = 0
            for point in contact_map.elements[0].data:
                dist = np.linalg.norm([point[0], point[1]]-transformed_contact[0:2])
                #dist = np.linalg.norm([point[0], point[1], point[2]]-transformed_contact)
                # if map_counter >= 14:
                #     print("Point: ", point, " transformed_contact ", transformed_contact)
                #     print("dist", dist)
                #     break
                if dist < 0.5:
                    point[3] = 255
                    local_colorized_counter = local_colorized_counter + 1
                    #print("Colorized point", [point[0], point[1], point[2]])
                # else:
                #     point[3] = 0
                point[4] = 0
                point[5] = 0

                # icp_point = np.array([point[0], point[1], point[2]])
                # # To odom
                # rotation = Rotation.from_quat(tf_rotations[tf_time_idx])
                # icp_point = rotation.apply(icp_point) + tf_positions[tf_time_idx]
                # # To icp_odom
                # rotation = Rotation.from_quat(icp_tf_rotations[tf_time_idx]).inv()
                # icp_point = rotation.apply(icp_point) - icp_tf_positions[tf_time_idx]

                # point[0] = icp_point[0]
                # point[1] = icp_point[1]
                # point[2] = icp_point[2]

                if local_colorized_counter > colorized_counter:
                  colorized_counter = local_colorized_counter

        print(colorized_counter, "points colorized")
        PlyData(contact_map, text=True).write('/home/russell/sewer_probing_assets/mission3/re_processed_contact_maps/processed_bags/map' + str(map_counter) +'_processed.ply')

        map_counter = map_counter + 1
        


    print("Finished")

