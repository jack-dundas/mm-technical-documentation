# script to copy the folder structure of "docs" into "media"

import os
import shutil

def copyFolderStructure():
    dirname = os.path.dirname(__file__)
    inputPath = os.path.join(dirname, '_docs','docs')
    mediaPath = os.path.join(dirname, '_docs','media')

    for dirpath, dirnames, filenames in os.walk(inputPath):
        folderName = dirpath[len(inputPath):]

        structure = mediaPath + folderName

        # Check if the directory already exists, if not, make it
        if not os.path.isdir(structure):
             os.mkdir(structure)
    
        #move the input Path media contents to the media folder
        if "media" in folderName:
            for file_name in os.listdir(inputPath + folderName):
                full_file_name = mediaPath + folderName + file_name
                shutil.copy(full_file_name, structure)



copyFolderStructure()