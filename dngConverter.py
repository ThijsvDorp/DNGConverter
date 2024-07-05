import rawpy
import imageio
from PIL import Image
import os

def convert_dng_to_jpg(dng_file, jpg_file):
    with rawpy.imread(dng_file) as raw:
        rgb = raw.postprocess()

    temp_tiff = jpg_file.replace('.jpg', '.tiff')
    imageio.imsave(temp_tiff, rgb)

    with Image.open(temp_tiff) as img:
        img.save(jpg_file, 'JPEG')

        os.remove(temp_tiff)


def convert_all_dng_in_directory(directory):
    for file in os.listdir(directory):
        if file.endswith('.dng'):
            dng_file = os.path.join(directory, file)
            jpg_file = dng_file.replace('.dng', '.jpg')
            convert_dng_to_jpg(dng_file, jpg_file)
            print(f'Converted {dng_file} to {jpg_file}')


directory = ''  # Add the directory path here
convert_all_dng_in_directory(directory)