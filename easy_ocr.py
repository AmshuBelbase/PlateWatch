import easyocr
import os
# import matplotlib.pyplot as plt
# import cv2
from IPython.display import Image, display
import warnings

# Filter out the specific warning message


def count_files_in_folder(folder_path):
    file_count = 0

    try:
        files = os.listdir(folder_path)
        for file in files:
            if os.path.isfile(os.path.join(folder_path, file)):
                file_count += 1
        return file_count
    except OSError as e:
        print("Error:", e)
        return None


folder_path = "cars/"
file_count = count_files_in_folder(folder_path)


for counting in range(file_count):
    # display(Image('plates/scaned_img_'+counting+'.jpg'))

    reader = easyocr.Reader(['en'])

    output = reader.readtext('plates/scaned_img_'+str(counting)+'.jpg')
    warnings.filterwarnings(
        "ignore", message="Neither CUDA nor MPS are available - defaulting to CPU. Note: This module is much faster with a GPU.")

    # recognized_texts = [item[1] for item in output]
    # print(recognized_texts)

    # print(output)

    extracted_texts = []

    for item in output:
        text = item[1]
        if isinstance(text, str):
            extracted_texts.append(text)
        elif isinstance(text, list):
            sub_text = ' '.join(
                sub_item for sub_item in text if isinstance(sub_item, str))
            extracted_texts.append(sub_text)

    for text in extracted_texts:
        print(text)
