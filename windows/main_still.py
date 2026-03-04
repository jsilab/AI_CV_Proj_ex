import numpy as np
import cv2
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
prototxt_path = os.path.join(base_dir, "assets", "models", "MobileNetSSD_deploy.prototxt")
model_path = os.path.join(base_dir, "assets", "models", "MobileNetSSD_deploy.caffemodel")

# img_path =  os.path.join(base_dir, "assets", '004545.jpg')
# img_path =  os.path.join(base_dir, "assets", '001763.jpg')
img_path =  os.path.join(base_dir, "assets", 'ace_radio.jpg')
# img_path =  os.path.join(base_dir, "assets", 'radio_ace.jpg')

### this is your confidence in how sure your model treats stuff
min_confidence = 0.2 

classes = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

### create random nums for each class
### by using nums from 0-254 w/ len of classes as iterations.
### do this 3 times; one for red, one for green, one for blue.
np.random.seed(543210)
colors = np.random.uniform(0,255, size=(len(classes), 3))

net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

image = cv2.imread(img_path)
height, width = image.shape[0], image.shape[1]
# height, weight = image.shape[:2]

# BLOB (Binary Large OBject) -> could tweak the scaleFactor and ddepth
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007, (300, 300), 130)

net.setInput(blob)
detected_objs = net.forward()

### the [][][0] represents the first object detected
### change this value to check the specific objects detected
# print(detected_objs[0][0][0])

for i in range(detected_objs.shape[2]):

    confidence = detected_objs[0][0][i][2]

    if confidence > min_confidence:
        class_index = int(detected_objs[0,0,i,1])

        upper_left_x = int(detected_objs[0,0,i,3] * width)
        upper_left_y = int(detected_objs[0,0,i,4] * height)
        lower_right_x = int(detected_objs[0,0,i,5] * width)
        lower_right_y= int(detected_objs[0,0,i,6] * height)

        pred_txt = f"{classes[class_index]}: {confidence:.2f}%"
        cv2.rectangle(image, (upper_left_x, upper_left_y), (lower_right_x, lower_right_y), colors[class_index], 3)
        cv2.putText(image, pred_txt, (upper_left_x, 
                    upper_left_y-15 if upper_left_y>30 else upper_left_y+15), # make sure this is in a tuple!!! like one above
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, colors[class_index], 2)
        
cv2.imshow("Detected Objs", image)
cv2.waitKey(0)
cv2.destroyAllWindows()