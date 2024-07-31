# -*- coding: utf-8 -*-
"""ass11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CCVSNx3SWd3luY6RbjncMOwO482tS69f
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histograms(image_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to open image file {image_path}")
        return

    # Convert the image from BGR to RGB format
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Calculate histograms for each color channel
    color_channels = ('r', 'g', 'b')
    histograms = {}
    for i, channel in enumerate(color_channels):
        histograms[channel] = cv2.calcHist([image_rgb], [i], None, [256], [0, 256])

    # Plot histograms
    plt.figure(figsize=(12, 6))
    for i, channel in enumerate(color_channels):
        plt.plot(histograms[channel], color=channel)
        plt.xlim([0, 256])
    plt.title('Color Channel Histograms')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.legend(['Red', 'Green', 'Blue'])
    plt.show()

# Example usage
plot_histograms('path_to_your_image.jpg')