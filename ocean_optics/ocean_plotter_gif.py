# Ocean Optics Averaging Plotter
# Matt Cook
# 10 May 2019

# import required modules
import numpy as np
import glob
import os, os.path
import matplotlib.pyplot as plt

# set data directory
dataDir = "/Users/mcook/OneDrive - University of Tennessee/CeGa_Air/CeGa_3/"

# count number of files in directory
files = len([name for name in os.listdir(dataDir) if os.path.isfile(os.path.join(dataDir, name))])

# initialize array X channels long and Y number of files
specData = np.zeros(2047)

# read in all data files
for file in glob.glob(dataDir+"*.txt"):
    # split the base to get file names
    # read in the data
    wavelength = np.genfromtxt(file, skip_header=14, skip_footer=1, usecols=0)
    spectrum = np.genfromtxt(file, skip_header=14, skip_footer=1, usecols=1)
    specData = np.vstack((specData,spectrum))


avgSpec = np.average(specData, axis=0)

# plot the data
plt.plot(wavelength,avgSpec)
plt.xlabel("Wavelength (um)")
plt.ylabel("Intensity (arb.)")
plt.title("averaged spectrum")
plt.grid(True)
plt.savefig("cega_3.png", dpi=750, format="png", orientation="landscape", bbox_inches="tight")
# plt.show()
# print("done")

