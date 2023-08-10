from PIL import Image
import numpy as np
import pandas as pd
import tensorflow as tf


class_names = ['angry', 'disgusted', 'fearful',
               'happy', 'neutral', 'sad', 'surprised']


async def predict_emotion(img_array, model):
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    scoring = {}
    for i in range(len(class_names)):
        scoring[class_names[i]] = score[i].numpy()

    max_score = 100 * np.max(score)
    max_class_idx = np.argmax(score)
    max_class = class_names[max_class_idx]

    return max_class, max_score
