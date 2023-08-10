from fastapi import File
from PIL import Image
import numpy as np
import pandas as pd
import tensorflow as tf


img_height = 48
img_width = 48

# Function to process the input image


async def process_input_image(image_file: File):

    img = Image.open(image_file)
    img = img.convert('RGB')
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    return img_array
