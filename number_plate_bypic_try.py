import cv2
import os
import time
harcascade = "model\haarcascade_russian_plate_number.xml"
min_area = 500
counting = 1


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
    img = cv2.imread('cars/car_'+str(counting)+'.jpeg')

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
            cv2.imwrite("plates/scaned_img_"+str(counting)+".jpg", img_roi)
            print("plates/scaned_img_"+str(counting)+".jpg")
            cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "Plate Saved", (50, 100),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
            # cv2.imshow("Results", img)
            counting += 1
            break
