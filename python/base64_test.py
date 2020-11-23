import base64
import cv2
import io
import numpy as np
from PIL import Image

with open("161555330115_.pic_hd.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read()).decode('utf-8')
print(my_string)

imgdata = base64.b64decode(str(my_string))
image = Image.open(io.BytesIO(imgdata))
im0 = np.array(image)
im0 = cv2.cvtColor(im0, cv2.COLOR_RGB2BGR)
cv2.imwrite('test.jpg', im0)
