#!/usr/bin/env python2.7
import sys
import numpy as np
import csv
from tf.transformations import *
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation


if __name__ == "__main__":

    file = open(sys.argv[1], "rU")
    reader = csv.reader(file, delimiter=',')
    initialized = False
    first_row = True

    gt_T0 = compose_matrix(None, None, None, None, None)
    odom_T0 = compose_matrix(None, None, None, None, None)
    contact_T0 = compose_matrix(None, None, None, None, None)

    odom_rpe = np.empty((0, 4), np.double)
    contact_rpe = np.empty((0, 4), np.double)



    for row in reader:

        if first_row:
            first_row = False
            continue
        
        if not initialized:

            gt_T0 = compose_matrix(None, None, [0,0,float(row[19])], [float(row[1]), float(row[7]), float(row[13])], None)
            odom_T0 = compose_matrix(None, None, [0,0,float(row[21])], [float(row[3]), float(row[9]), float(row[15])], None)
            contact_T0 = compose_matrix(None, None, [0,0,float(row[23])], [float(row[5]), float(row[11]), float(row[17])], None)

            initialized = True
            continue


        if ' ' in row:
            break
            

        gt_T1 = compose_matrix(None, None, [0,0,float(row[19])], [float(row[1]), float(row[7]), float(row[13])], None)
        odom_T1 = compose_matrix(None, None, [0,0,float(row[21])], [float(row[3]), float(row[9]), float(row[15])], None)
        contact_T1 = compose_matrix(None, None, [0,0,float(row[23])], [float(row[5]), float(row[11]), float(row[17])], None)

        odom_error =  np.linalg.inv(np.linalg.inv(gt_T0)*gt_T1)*(np.linalg.inv(odom_T0)*odom_T1)
        contact_error =  np.linalg.inv(np.linalg.inv(gt_T0)*gt_T1)*(np.linalg.inv(contact_T0)*contact_T1)

        if(numpy.linalg.norm(odom_error[0:3,3]) < 1.0):
            continue

        odom_rpe = np.append(odom_rpe, [[1e9*float(row[0]), np.absolute(odom_error[0,3]), np.absolute(odom_error[1,3]), np.absolute(odom_error[2,3])]], axis=0)
        contact_rpe = np.append(contact_rpe, [[1e9*float(row[0]), np.absolute(contact_error[0,3]), np.absolute(contact_error[1,3]), np.absolute(contact_error[2,3])]], axis=0)


    odom_median_x = np.median(odom_rpe[:,1])
    odom_median_y = np.median(odom_rpe[:,2])
    odom_median_z = np.median(odom_rpe[:,3])

    contact_median_x = np.median(contact_rpe[:,1])
    contact_median_y = np.median(contact_rpe[:,2])
    contact_median_z = np.median(contact_rpe[:,3])

    print("Odometry median RPE: (%f, %f, %f)"%(odom_median_x,odom_median_y,odom_median_z))
    print("Contact median RPE: (%f, %f, %f)"%(contact_median_x,contact_median_y,contact_median_z))
    print(contact_rpe.size)

    plt.subplot(3, 1, 1)
    plt.plot(odom_rpe[:,0], odom_rpe[:,1], 'r')
    plt.plot(contact_rpe[:,0], contact_rpe[:,1], 'b--')
    plt.title('Relative Pose Error')
    plt.ylabel('X component (m)')

    plt.subplot(3, 1, 2)
    plt.plot(odom_rpe[:,0], odom_rpe[:,2], 'r')
    plt.plot(contact_rpe[:,0], contact_rpe[:,2], 'b--')
    plt.ylabel('Y component (m)')

    plt.subplot(3, 1, 3)
    plt.plot(odom_rpe[:,0], odom_rpe[:,3], 'r')
    plt.plot(contact_rpe[:,0], contact_rpe[:,3], 'b--')
    plt.xlabel('Time (s)')
    plt.ylabel('Z component (m)')

    plt.show()