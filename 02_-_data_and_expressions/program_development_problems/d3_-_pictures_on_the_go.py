#!/usr/bin/env python3
# Pictures on the Go
#
# Develop and test a Python that determines how many images can be stored on a
# given size USB flash drive. The size of the USB drive is to entered by the
# user in gigabytes (GB). The number of images that can be stored must be
# calculated for GIF, JPEG, PNG, and TIFF image file formats. The program
# output shoulbe formatted as given below.
#
#     Enter USB size (GB): 4
#
#     xxxx images in GIF format can be stored
#     xxxx images in JPEG format can be stored
#     xxxx images in PNG format can be stored
#     xxxx images in TIFF format can be stored
#
# The ultimate file size of a given image depends not only on the image format
# used, but also on the image itself. In addition, formats such as JPEG allow
# the user to select the degree of compression for the image quality desired.
# For this program, we assume the image compression ratios given below. Also
# assume that all the images have a resoultion of 800x600px. 
#
# Thus, for example, a 800x600px image with 16-bit (2 bytes) color depth would
# have a total number of bytes of 800 * 600 * 2 = 960,000. For a compression
# rate of 25:1, the total number of bytes needed to store the image would be
# 960000/25 = 38400. Finally, assume that a GB equals 1,000,000,000 bytes, as
# given in Figure 2.1.
#
# +---------------+----------------------------------------+-----------------------------------+-------------------+
# |    Format     |      Full Name                         |    Color Depth                    |    Compression    |
# +===============+========================================+===================================+===================+
# |      GIF      |  Graphics Interchange Format           |  256 colors, 8 bits               |   lossless, 5:1   |
# +---------------+----------------------------------------+-----------------------------------+-------------------+
# |     JPEG      |  Joint Photographic Experts Group      |  16 million colors, 24 bits       |     lossy, 25:1   |
# +---------------+----------------------------------------+-----------------------------------+-------------------+
# |      PNG      |  Portable Network Graphics             |  16 million colors, 24 bits       |   lossless, 8:1   |
# +---------------+----------------------------------------+-----------------------------------+-------------------+
# |     TIFF      |  Tagged Image File Format              |  280 trillion colors, 48 bits     |   lossless, n/a   |
# +---------------+----------------------------------------+-----------------------------------+-------------------+
#
# Note that a "lossless" compresssion is one in which no information is lost. A
# "lossy" compression does lose some of the original information.
#

