import os
import shutil
from pathlib import Path

def copy_valid_pairs(main_folder, output_folder, max_pairs_per_folder=None, image_exts=(".jpg", ".jpeg", ".png")):
    """
    Copy image+txt pairs from each subfolder.

    Args:
        main_folder (str): Path to main folder
        output_folder (str): Destination folder
        max_pairs_per_folder (int or None):
            - None → copy ALL pairs
            - Number → copy up to that many pairs per folder
    """
    main_folder = Path(main_folder)
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    for subfolder in sorted(main_folder.iterdir()):
        if subfolder.is_dir():

            images = sorted([f for f in subfolder.iterdir() if f.suffix.lower() in image_exts])

            pair_count = 0

            for img in images:
                txt_file = img.with_suffix(".txt")

                if txt_file.exists():
                    shutil.copy(img, output_folder / img.name)
                    shutil.copy(txt_file, output_folder / txt_file.name)

                    pair_count += 1
                    print(f"Copied {img.name} & {txt_file.name} from {subfolder.name}")

                    # Stop if max limit reached
                    if max_pairs_per_folder and pair_count >= max_pairs_per_folder:
                        break

            if pair_count == 0:
                print(f"⚠️ No valid pairs in {subfolder.name}")
            else:
                print(f"✅ {pair_count} pairs copied from {subfolder.name}")

    print("\n🎉 Done! Files copied to:", output_folder)


if __name__ == "__main__":
    main_dir = r"D:\Checked Dataset\August Checking"
    output_dir = r"D:\Annotation Symbol images"

    # 🔧 SET LIMIT HERE:
    max_limit = 311   # change this value
    # max_limit = None  # ← use this to copy ALL pairs

    copy_valid_pairs(main_dir, output_dir, max_pairs_per_folder=max_limit)