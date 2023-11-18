import easyocr
from IPython.display import Image, display
import os
import shutil
import cv2
import time
import mysql.connector
from datetime import date
# Get today's date
today = date.today()

# Print today's date 

mydb = mysql.connector.connect(host='localhost', user='root', password='root',database='epiz_32083127_traffic', port='3307', auth_plugin='mysql_native_password')

cur =  mydb.cursor()

harcascade = "model\haarcascade_russian_plate_number.xml"
min_area = 500
counting = 1

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
    new_file_name_p = "fined_"+new_prefix+'_'+str(count_p)+'.jpeg'
    shutil.move(
        os.path.join(source_folder_plate, file_to_move),
        os.path.join(destination_folder_plate, new_file_name_p)
    )  
    return new_file_name
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
            # print(texts) 
            new_file_name = move_file(transaction_type, new_prefix, counting)
            f_i = t_types.index(transaction_type)
            tt = str(options[t_types.index(transaction_type)])
            f = str(fine[f_i])
            s = "SELECT * FROM users WHERE numberplate = %s"
            cur.execute(s, (texts,))
            result = cur.fetchall()
            for rec in result:
                # print(rec[1])
                s = "INSERT INTO fines (name, email,uid, numberplate, description, type, amount, date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                values = (rec[1], rec[2],rec[0], rec[5], new_file_name, tt, f, today) 
                try:
                    cur.execute(s, values)
                    mydb.commit()
                    print("Data inserted successfully!")
                    # messagebox.showinfo("Alert", "Rec !") 
                except Exception as e:
                    mydb.rollback()  # Rollback the transaction if there's an error
                    print(f"Error inserting data: {str(e)}")
                    # messagebox.showinfo("Alert", "Sign Up Un Successfull !")
            # move_file(transaction_type, new_prefix, counting)
    else:
        print("No Vehicle Violated this Rule.")
def selected(option): 
    if option == 'Over Speed':
        transaction_type = "over_speed"

    elif option == 'Wrong Lane':
        transaction_type = "wrong_lane"

    elif option == 'Traffic Light':
        transaction_type = "traffic_light"

    elif option == 'No parking':
        transaction_type = "no_parking"

    print(transaction_type)
    operate(transaction_type)

fine = ["1000", "2000", "5000", "10000"]
t_types = ["over_speed", "wrong_lane", "traffic_light", "no_parking"]
options = [ 
    "Over Speed",
    "Wrong Lane",
    "Traffic Light",
    "No parking",
]

while(1):
    for option in options:
        selected(option)
    time.sleep(2)