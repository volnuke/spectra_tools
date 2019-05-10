# Ocean Optics Plotter
# Matt Cook
# 03 May 2019

# import required modules
import numpy as np
import glob
import os, os.path
import matplotlib.pyplot as plt

# set data directory
dataDir = "LIBS/"

# count number of files in directory
files = len([name for name in os.listdir(dataDir) if os.path.isfile(os.path.join(dataDir, name))])
print(files)

# read in all data files
for file in glob.glob("*.txt"):
    # plt.close(all)
    # split the base to get file names
    base = os.path.splitext(file)[0]
    figName = base+".png"
    # read in the data
    dataIn = np.genfromtxt(file, skip_header=14, skip_footer=1)
    print(len(dataIn))
    # plot the data
    plt.plot(dataIn[:,0],dataIn[:,1])
    plt.xlabel("Wavelength (um)")
    plt.ylabel("Intensity (arb.)")
    plt.title(base)
    plt.grid(True)
    plt.savefig(figName, dpi=750, format="png", orientation="landscape", bbox_inches="tight")
    # plt.show()