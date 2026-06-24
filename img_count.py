import os

parent_folder = r"C:\Checking\Checked 1"

image_extensions = (".jpg", ".jpeg", ".png")

for folder_name in os.listdir(parent_folder):
    folder_path = os.path.join(parent_folder, folder_name)

    if os.path.isdir(folder_path):
        image_count = 0
        txt_count = 0

        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            if os.path.isfile(file_path):
                ext = os.path.splitext(file_name)[1].lower()

                if ext in image_extensions:
                    image_count += 1
                elif ext == ".txt":
                    txt_count += 1

        print(f"{folder_name} = ({image_count}, {txt_count})")
