
import numpy as np

opto_data_dir        = '/home/mrule/Desktop/Workspace2/CGID_manuscript_4/'
opto_dataset         = opto_data_dir+'TOMMY_MI_121101_full_trial_continuous_square_pulse_6mW001'
opto_dataset_compact = opto_dataset+'_compact'

print 'Known frequency bands for Tommy are as follows:'
print '\t45-51'
print '\t93-102'
print '\t110-126'
print '\t140-155'


electrode_spacing = 0.4


M = np.array([[66,  2, 84, 49, 51, 56, 58, 60, 64, 95],
           [79, 81, 82, 47, 44, 46, 52, 62, 31, 32],
           [77, 80, 45, 43, 42, 50, 54, 21, 29, 30],
           [75, 78, 41, 40,  0, 15, 19, 25, 27, 28],
           [ 0,  0,  0,  0,  0, 17, 13, 23, 20, 26],
           [73, 76, 39, 38,  5,  9, 11, 12, 16, 24],
           [71, 74, 37, 36,  7,  6,  8, 10, 14, 22],
           [69, 72, 35, 34,  4, 88, 90, 92, 93, 18],
           [67, 70, 33,  3, 85, 87, 89, 91, 94, 63],
           [65, 68,  1, 83, 86, 53, 55, 57, 59, 61]], dtype=np.uint8)


extent = np.array([.5,9.5,.5,9.5])*electrode_spacing
