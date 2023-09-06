import easyocr
import matplotlib.pyplot as plt
import cv2
from IPython.display import Image, display
display(Image('plates/scaned_img_0.jpg')) 
reader = easyocr.Reader(['en'])
output = reader.readtext('plates/scaned_img_2.jpg')
output