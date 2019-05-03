# Ocean Optics Plotter
# Matt Cook
# 03 May 2019

# import required modules
import numpy as np
import glob
import os
import matplotlib.pyplot as plt

# set data directory
dataDir = "LIBS/"

# read in all data files
for file in glob.glob(dataDir+"*.txt"):
    plt.close(all)
    
    base = os.path.splitext(file)[0]
    figName = base+".png"

    dataIn = np.genfromtxt(file, skip_header=14, skip_footer=1)
    plt.plot(dataIn[:,0],dataIn[:,1])
    plt.xlabel("Wavelength ($\mu$m)")
    plt.ylabel("Intensity (arb.)")
    plt.title(base)
    plt.grid(True)
    plt.savefig(figName, dpi=750, format="png", orientation="landscape", bbox_inches="tight")
    # plt.show()