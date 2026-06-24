# --------------------------------------------------------------------------------
# This script rename the jpg or txt file of brands dataset. 
# dataset_path- Takes the root dir path where all the brands dataset is available.
# Rename multiple brands dataset files at time.
# Run Command- python file_rename.py
# built on Python 3.7
# (C) 2023 Raj Kumar, Droisys, India
# email raj.k@droisys.com
# --------------------------------------------------------------------------------

import os
dataset_path = r"C:\Desktop\Dataset\Rename\\"
def rename_files():
    '''rename_files - rename the image and coordinate file on brands with there specific brand name tag and count.(to resolve overriding problem)'''
    for dir in os.listdir(dataset_path):
        if "classes.txt" not in dir:           
            sub_dir=dataset_path+dir

            for count, filename in enumerate(os.listdir(sub_dir)):
                tag=dir
                if (filename.endswith(".jpg")) or (filename.endswith(".JPG")) or (filename.endswith(".jpeg")) or (filename.endswith(".png")) or (filename.endswith(".JPEG")) or (filename.endswith(".PNG")):
                    if not os.path.exists(sub_dir+'\\'+tag+"_"+str(count)+'.jpg'):
                        os.rename(sub_dir+'\\'+filename, sub_dir+'\\'+tag+"_"+str(count)+'.jpg')
                    else:
                        pass
                if filename.endswith('.txt') and "classes.txt" not in filename:
                    if not os.path.exists(sub_dir+'\\'+tag+"_"+str(count-1)+'.txt'):
                        os.rename(sub_dir+'\\'+filename, sub_dir+'\\'+tag+"_"+str(count-1)+'.txt')
                    else:
                        pass

rename_files()
