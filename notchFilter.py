"""
Name:           Carlos Meza
Description:
 Applying a notch filer, plot values of csv file of the x, y and combination of two frequencies.
"""

import numpy as np
import matplotlib.pyplot as plt

def applyNotch(fs, dataFile) :
    # Read csv values and store in array to manipulate
    x = np.genfromtxt(dataFile, delimiter=',')
    x = np.array(x, dtype=float)
    
    # Declare constants for example, freq and sampling rate
    f = 17
    fs = 500
    # Replace w with 17hz signal over the 500 samples per second, W = 2 * pi * f(frequency)
    w = 2 * np.pi * f / fs
    # Stop values of length of data + 100
    N = len(x) + 100
    # Empty array of ones to populate with difference equation results
    y = np.ones(N)
    n = 0
      
    # Loop and place values in y, y[n] = 0 when n < 0
    # x[n] = 0 when n < 0 or N-1 < n
    for n in range(N):
        if(n >= 2 and n < len(x) - 1):
            # Output difference equation calculated by hand (Inverse z transform)
            y[n] = 2*(0.9372)*np.cos(w)*y[n-1] - 0.8783*y[n-2] + x[n] - 2*np.cos(w)*x[n-1] + x[n-2]
            
        elif(n >= 2 and n > len(x) - 1):
            y[n] = 2*(0.9372)*np.cos(w)*y[n-1] - 0.8783*y[n-2]
            
        else:
            y[n] = 0
    
    # Part i: Plot original signal of x with limits to x axis[-25, 625]
    plt.figure(0)
    axis = plt.gca()
    axis.set_xlim([-25, 625])
    plt.title('Original Signal')
    plt.plot(x)
    
    # Part ii: Plot filtered signal y with limits to y axis[-2.25, 2.25]
    plt.figure(1)
    axis = plt.gca()
    axis.set_ylim([-2.25, 2.25])
    plt.title('Filtered Signal')
    plt.plot(y)
    
    # Create arrange element to create 10Hz signal and 33Hz signal
    x = np.arange(0, 1, 1/fs)
    signal_10 = np.cos(2 * np.pi * 10 * x)
    signal_33 = np.cos(2 * np.pi * 33 * x)
    combined = signal_10 + signal_33
    
    
    # Part iii: Plot signal by combining a 10Hz and 33Hz signal with x limit[-25, 625]
    plt.figure(2)
    axis = plt.gca()
    axis.set_xlim([-25, 625])
    plt.title('Combined Signal(10Hz + 33Hz)')
    plt.plot(combined)
    
    # Show all the graphs
    plt.show()

############################################################
###########################  main  #########################
if __name__ == "__main__":
    fs = 500
    dataFileName = "notchData.csv"

    # write this function
    applyNotch(fs, dataFileName)
