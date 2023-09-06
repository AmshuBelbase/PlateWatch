import os


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

if file_count is not None:
    print(f"Number of files in '{folder_path}': {file_count}")
