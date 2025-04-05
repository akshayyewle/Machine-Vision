import os
import time 
import numpy as np

from scipy.spatial import KDTree 
import pyvista as pv

# Load Point Cloud
pcd = pv.read('Data/MLS_UTWENTE_super_sample.ply')
pcd.plot(eye_dome_lighting=True)