import os
import shutil


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


def rename_files(folder_path, new_prefix):
    try:
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


folder_path = "cars/"
new_prefix = "car"
rename_files(folder_path, new_prefix)
