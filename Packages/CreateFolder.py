import os
# Function used in several classes to create a folder

# Packages to create a folder
def createFolder(folderPath):
    # Check if the folder exists, if not create it
    if not os.path.exists(".//" + folderPath):
        os.makedirs(".//" + folderPath)