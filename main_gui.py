from tkinter import *
import easyocr
from IPython.display import Image, display
import os
import shutil
import cv2
import time
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='',database='epiz_32083127_traffic')
cur =  mydb.cursor()
harcascade = "model\haarcascade_russian_plate_number.xml"
min_area = 500
counting = 1
root = Tk()
root.title('Traffic Management')
root.iconbitmap('./model/OIP.jpg')
root.geometry("1200x600")

def count_files_in_folder(folder_path, transaction_type):
    file_count = 0
    folder_path = folder_path+transaction_type+'/'
    try:
        files = os.listdir(folder_path)
        for file in files:
            if os.path.isfile(os.path.join(folder_path, file)):
                file_count += 1
        return file_count
    except OSError as e:
        print("Error:", e)
        return 0

def rename_files(folder_path, new_prefix, transaction_type):
    try:
        folder_path = folder_path+transaction_type+'/'
        files = os.listdir(folder_path)
        for index, file in enumerate(files, start=1):
            file_extension = os.path.splitext(file)[1]
            new_name = f"{new_prefix}_{(index-1)}{file_extension}"
            old_path = os.path.join(folder_path, file)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed {file} to {new_name}")
    except OSError as e:
        print("Error:", e)

def move_file(transaction_type, new_prefix, counting):
    source_folder = "penalty_vehicles/"+transaction_type+"/"
    source_folder_plate = "penalty_vehicles/plates/"+transaction_type+"/"

    destination_folder = "penalty_paid_vehicles/"
    destination_folder_plate = "penalty_paid_vehicles/plates/"

    count_v = count_files_in_folder(destination_folder, transaction_type)
    count_p = count_files_in_folder(destination_folder_plate, transaction_type)

    destination_folder = "penalty_paid_vehicles/"+transaction_type+"/"
    destination_folder_plate = "penalty_paid_vehicles/plates/"+transaction_type+"/"

    file_to_move = new_prefix+'_'+str(counting)+'.jpeg' 
    count_p+=1
    count_v+=1
    new_file_name = "fined_"+new_prefix+'_'+str(count_v)+'.jpeg'
    shutil.move(
        os.path.join(source_folder, file_to_move),
        os.path.join(destination_folder, new_file_name)
    )
    new_file_name = "fined_"+new_prefix+'_'+str(count_p)+'.jpeg'
    shutil.move(
        os.path.join(source_folder_plate, file_to_move),
        os.path.join(destination_folder_plate, new_file_name)
    )  

def insert_data():
    print()

def operate(transaction_type):

    # counting files

    folder_path = "penalty_vehicles/"
    file_count = count_files_in_folder(folder_path, transaction_type)

    if (file_count != 0):

        # renaming files

        new_prefix = "vehicle"
        rename_files(folder_path, new_prefix, transaction_type)

        # saving number_plate

        for counting in range(file_count):
            img = cv2.imread(folder_path+transaction_type + '/' +
                             new_prefix+'_'+str(counting)+'.jpeg')

            plate_cascade = cv2.CascadeClassifier(harcascade)
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

            for (x, y, w, h) in plates:
                area = w*h

                if area > min_area:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(img, "Number Plate", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

                    img_roi = img[y: y+h, x: x+w]
                    # cv2.imshow("ROI", img_roi)
                    # time.sleep(5)
                    cv2.imwrite(folder_path+'plates/'+transaction_type + '/' +
                                new_prefix+'_'+str(counting)+'.jpeg', img_roi)
                    print(folder_path+'plates/'+transaction_type + '/' +
                          new_prefix+'_'+str(counting)+'.jpeg')
                    cv2.rectangle(img, (0, 200), (640, 300),
                                  (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, "Plate Saved", (50, 100),
                                cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
                    # cv2.imshow("Results", img)
                    counting += 1
                    break
        # easy-ocr

        for counting in range(file_count):
            # display(Image('plates/scaned_img_'+counting+'.jpg'))
            reader = easyocr.Reader(['en'])
            output = reader.readtext(folder_path+'plates/'+transaction_type + '/' +
                                     new_prefix+'_'+str(counting)+'.jpeg')
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
            texts = ''
            for text in extracted_texts:
                texts = texts+text
                texts = texts.replace(" ", "")
            print(texts)
            Label(
                root, text='Detected Number Plate of ' + new_prefix+'_'+str(counting)+'.jpeg' + ' : '+texts).pack()
            move_file(transaction_type, new_prefix, counting)
    else:
        print("No File in Folder")
        Label(root, text='No File in Folder').pack()

def selected(event):
    # mylabel = Label(root, text=clicked.get()).pack()
    if clicked.get() == 'Over Speed':
        mylabel = Label(
            root, text='Started Procedure for All Vehicles for : '+clicked.get()).pack()
        transaction_type = "over_speed"

    elif clicked.get() == 'Wrong Lane':
        mylabel = Label(
            root, text='Started Procedure for All Vehicles for : '+clicked.get()).pack()
        transaction_type = "wrong_lane"

    elif clicked.get() == 'Traffic Light':
        mylabel = Label(
            root, text='Started Procedure for All Vehicles for : '+clicked.get()).pack()
        transaction_type = "traffic_light"

    elif clicked.get() == 'No parking':
        mylabel = Label(
            root, text='Started Procedure for All Vehicles for : '+clicked.get()).pack()
        transaction_type = "no_parking"

    else:
        mylabel = Label(root, text="Select Any Option").pack()

    print(transaction_type)
    operate(transaction_type)


options = [
    " -- Select -- ",
    "Over Speed",
    "Wrong Lane",
    "Traffic Light",
    "No parking",
]
clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command=selected)
drop.pack(pady=20)

root.mainloop()
