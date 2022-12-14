# import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import load_model
# from PIL import Image
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def getPrediction(filename):
#  Load the best model
    model = load_model("MobileNet_Model.h5")


    # print("Hi babe")

    # Random Check
    # path = 'static/images/'+filename #for 2nd code of app.py
    path = filename
    img = load_img(path, target_size=(224,224))
    # print(img)

    input_arr = img_to_array(img)/255
    # print(input_arr)

    input_arr = np.array([input_arr])
    # print(input_arr)

    pred = np.argmax(model.predict(input_arr))
    print("---------------Diagnosis is:", int(pred))
   
    return int(pred)
    # To display the image
    # plt.imshow(input_arr[0])
    # plt.title("Input image")
    # plt.show()

# pred = getPrediction('static/images/WBC-Malignant-Pre-001.jpg')


