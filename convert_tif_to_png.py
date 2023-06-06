import numpy as np
from PIL import Image
import rasterio
from rasterio.windows import Window

# converts to 8 bits AFTER re-scaling bands
def s255(arr):
    arr_std = (arr - np.min(arr)) / (np.max(arr) - np.min(arr)) * 255
    # Convert the standardized array to integer values
    arr_std = arr_std.astype(np.uint8)
    return arr_std

# Multi bandas
# Open the input raster file
with rasterio.open(r'3bands_clipped_tif.tif') as src:

    # Calculate the height and width of the sub-rasters
    nHeight=1
    nWidth=1
    height = src.height // nHeight  # Divide the raster into 58 rows
    width = src.width // nWidth  # Divide the raster into 23 columns

    # Loop through each sub-raster and clip the data
    for i in range(nHeight):
        for j in range(nWidth):
            # Define the window to clip the sub-raster
            ymin = i * height
            ymax = (i + 1) * height
            xmin = j * width
            xmax = (j + 1) * width
            #print(ymin, ymax,xmin, xmax)
            window = Window.from_slices((ymin, ymax), (xmin, xmax))

            # Read the data within the window
            clipped_data_1 = s255(src.read(1, window=window))
            clipped_data_2 = s255(src.read(2, window=window))
            clipped_data_3 = s255(src.read(3, window=window))
            #clipped_data = src.read().astype(np.uint8)
            #print(clipped_data_1.shape)
            #print('clipped_data.shape', clipped_data.shape)
            # Stack the bands to create an RGB image array
            rgb_image = np.stack([clipped_data_1, clipped_data_2, clipped_data_3], axis=2)
            #rgb_image = np.stack([clipped_data_2, clipped_data_2, clipped_data_2], axis=2)
            #print('rgb_image.shape', rgb_image.shape)
            #rgb_image = clipped_data
            #print(rgb_image)

            # Convert the image array to a PIL Image
            image = Image.fromarray(rgb_image,mode='RGB')

            # Save the PIL Image as a PNG file
            output_file = f'image_{i}_{j}.png'
            image.save(output_file) 
