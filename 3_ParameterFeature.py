#-----------------------------------
# PARAMETER FEATURE 
#-----------------------------------
# Importing the libraries
import copy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2 ,os
import h5py

# Loading the image
dir_images = "./Dataset/Training/G1"
imgs = os.listdir(dir_images)
for imgnm in imgs:
    image = plt.imread(os.path.join(dir_images,imgnm))
    size = cv2.resize(image,(100,100),)
    image = cv2.cvtColor(size, cv2.COLOR_BGR2RGB)
    # Converting RGB to Gray scale
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    #Gaussain Blur Deleted noise
    gaussain = cv2.GaussianBlur(gray_image,(5,5),0)
    # Canny Edge Detection
    canny_image = cv2.Canny(gaussain,100,10)

   
    # Parameters for HOG descriptor
    cell_size = (6, 6)
    num_cells_per_block = (2, 2)
    h_stride = 1
    v_stride = 1
    num_bins = 9

    # Setting parameters for HOG descriptor

    # Block size
    block_size = (num_cells_per_block[0] * cell_size[0],
              num_cells_per_block[1] * cell_size[1])

    # Total number of cells in image
    x_cell = canny_image.shape[1] // cell_size[0]
    y_cell = canny_image.shape[0] // cell_size[1]

    # Block stride
    block_stride = (cell_size[0] * h_stride, 
                cell_size[1] * v_stride)

    # Window size
    win_size = (x_cell * cell_size[0],
            y_cell * cell_size[1])

    # Printing the parameters
    print("==========================================")
    print("| HOG Descriptor Parameters:")
    print("| ")
    print("| ==> Window size: ", win_size)
    print("| ==> Cell size: ", cell_size)
    print("| ==> Block size: ", block_size)
    print("| ==> Block stride of: ", block_stride)
    print("| ==> Number of bins: ", num_bins)
    print("==========================================\n")

    # Setting the parameters of HOG descriptor
    HOG = cv2.HOGDescriptor(win_size,                   # Size of detection window in pixels 
                        block_size,                     # Defines how many cells are in each block. 
                        block_stride,                   # Defines the distance between adjecent blocks
                        cell_size,                      # Determines the size fo your cell
                        num_bins)                       # Number of bins for the histograms.
                        #win_sigma = DEFAULT_WIN_SIGMA, # Default: Gaussian smoothing window parameter.
                        #threshold_L2hys = 0.2,         # Default: L2-Hys (Lowe-style clipped L2 norm) normalization method shrinkage. The L2-Hys method is used to normalize the blocks and it consists of an L2-norm followed by clipping and a renormalization.
                        #gamma_correction = True        # Default: Flag to specify whether the gamma correction preprocessing is required or not. 
                        #nlevels = DEFAULT_NLEVELS)     # Default: Maximum number of detection window increases.

    # Compute HOG descriptor for gray scale image
    HOG_descriptor = HOG.compute(canny_image) 

    print("==========================================")
    print("| ==> HOG Descriptor's shape: ", HOG_descriptor.shape)
    print("==========================================")
    print("| ==> HOG Features: ", HOG_descriptor)
    print("==========================================\n")

    for savetxt in imgs:
        #save = np.savetxt("output"+str(imgnm)+".txt",HOG_descriptor , '%f')
        save = np.savez("outputall.txt", save , '%f')

print("[STATUS] end of training..")


