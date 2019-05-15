# Ocean Optics Plotter
# Matt Cook
# 03 May 2019

# import required modules
import numpy as np
import glob
import os, os.path
import matplotlib.pyplot as plt
# import imageio

# set data directory
dataDir = "/Users/mcook/OneDrive - University of Tennessee/CeGa_Air/CeGa_4/"

# PNG directory
# pngDir = "png2gif/"

# read in all data files
for file in glob.glob(dataDir+"*.txt"):
    # split the base to get file names
    base = os.path.splitext(file)[0]
    figName = base+".png"
    # read in the data
    dataIn = np.genfromtxt(file, skip_header=14, skip_footer=1)
    # print(len(dataIn))
    # plot the data
    plt.plot(dataIn[:,0],dataIn[:,1])
    plt.xlabel("Wavelength (um)")
    plt.ylabel("Intensity (arb.)")
    # plt.title(base)
    plt.grid(True)
    plt.savefig(figName, dpi=500, format="png", orientation="landscape", bbox_inches="tight")
    plt.clf()
    # plt.show()

# with imageio.get_writer('test_movie.gif', mode='I') as writer:
#     for file in glob.glob(".png"):
#         image = imageio.imread(file)
#         writer.append_data(image)