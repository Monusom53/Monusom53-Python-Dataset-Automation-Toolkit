import glob
import os
import shutil
from multiprocessing import Pool, cpu_count, Manager

# Load class names from the reference classes.txt file
def load_class_names():
    with open("C:/Users/Desktop/Dataset/classes.txt", "r") as my_file:
        data = my_file.read()
    return data.strip().split("\n")  # Corrected newline splitting

# Update class IDs in label files within a given directory
def update_classid(dir_path, old_id, new_id):
    for filepath in glob.iglob(os.path.join(dir_path, '*.txt')):
        if filepath.lower().endswith("classes.txt"):
            continue
        try:
            with open(filepath, 'r') as file:
                lines = file.readlines()

            modified = False
            updated_lines = []
            for line in lines:
                parts = line.strip().split()
                if parts and parts[0] == str(old_id):
                    parts[0] = str(new_id)
                    modified = True
                updated_lines.append(" ".join(parts) + "\n")

            if modified:
                with open(filepath, 'w') as file:
                    file.writelines(updated_lines)

        except Exception as e:
            print(f"❌ Error updating {filepath}: {e}")

# Process each directory: delete old classes.txt, copy reference, update labels
def process_directory(dir_info):
    source, class_name_list, dir_name, unmatched_folders = dir_info
    print("📁 Processing:", dir_name)

    # If folder name not in class list, add to unmatched and skip
    if dir_name not in class_name_list:
        print(f"⚠️ Folder name '{dir_name}' does not match any class in classes.txt")
        unmatched_folders.append(dir_name)
        return

    dir_path = os.path.join(source, dir_name)
    ref_classes_path = "C:/Users/Desktop/Dataset/classes.txt"
    dst_classes_path = os.path.join(dir_path, "classes.txt")

    # Delete existing classes.txt if present
    try:
        if os.path.exists(dst_classes_path):
            os.remove(dst_classes_path)
    except Exception as e:
        print(f"❌ Error deleting classes.txt in {dir_name}: {e}")
        return

    # Copy the reference classes.txt
    try:
        shutil.copy(ref_classes_path, dst_classes_path)
    except Exception as e:
        print(f"❌ Error copying classes.txt to {dir_name}: {e}")
        return

    # Update class IDs in label files
    new_class_id = class_name_list.index(dir_name)
    for file_name in os.listdir(dir_path):
        if file_name.endswith(".txt") and file_name.lower() != "classes.txt":
            file_path = os.path.join(dir_path, file_name)
            try:
                with open(file_path, "r") as file:
                    lines = file.readlines()
                if not lines:
                    continue
                first_line_parts = lines[0].strip().split()
                if not first_line_parts:
                    continue
                original_class_id = first_line_parts[0]
                if original_class_id != str(new_class_id):
                    update_classid(dir_path, original_class_id, new_class_id)
            except Exception as e:
                print(f"❌ Error reading file {file_path}: {e}")

# Main function to set up multiprocessing and process folders
def main():
    source = "C:/Monu Backup/DataSet/may_training/Captains/Checking/"
    class_name_list = load_class_names()

    all_dirs = [d for d in os.listdir(source) if os.path.isdir(os.path.join(source, d))]

    print(f"🔄 Processing {len(all_dirs)} folders using {cpu_count()} cores...")

    manager = Manager()
    unmatched_folders = manager.list()  # multiprocessing-safe shared list

    dir_info_list = [(source, class_name_list, d, unmatched_folders) for d in all_dirs]

    with Pool(processes=cpu_count()) as pool:
        pool.map(process_directory, dir_info_list)

    # After processing all folders, save unmatched folders to a file in source path
    unmatched_file_path = os.path.join(source, "unmatched_folders.txt")
    with open(unmatched_file_path, "w") as f:
        for folder_name in unmatched_folders:
            f.write(folder_name + "\n")

    print(f"⚠️ Unmatched folder names saved to: {unmatched_file_path}")
    print("✅ All folders processed.")

if __name__ == "__main__":
    main()
