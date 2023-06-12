import os

# Define folder which contains all the necessary files
folder = r"PATH/TO/FOLDER"

formats = ["tif", "tiff", "jpg", "png", "bmp"]


# Dictionary containg the conversion from well numbers to actual names
# Need to be changed for different naming conventions
info = {
    "1": "5 mikM_B",
    "2": "3 mikM_B",
    "3": "1 mikM_B",
    "4": "NC_B",
    "5": "NC_B",
    "6": "1 mikM_B",
    "7": "3 mikM_B",
    "8": "5 mikM_B"
}

# Iterate over every file
for ind, file in enumerate(os.listdir(folder)):
    # Extract the file name and extension
    name_raw = os.path.basename(file)
    name, ext = name_raw.split(".")[0], name_raw.split(".")[1]
    print(f"#{ind}\tName:\t\t{name} Type: {ext}")
    # Check if the file is actually an image
    if ext in formats:
        # Extract the information stored in the file name
        f_info = name.split("_")
        # Get the slice index for the image
        sind = f_info[-1][1]
        # Get the tile index for the image
        tind = f_info[-1][-2:]
        # Create the new filename
        new_name = f"{f_info[0]}_{f_info[1]}_{info[sind]}_{tind}.{ext}"
        print(f"#{ind}\tRenamed to:\t{new_name}")
        # Rename the actual file
        os.rename(os.path.join(folder, name_raw), os.path.join(folder, new_name))
    
