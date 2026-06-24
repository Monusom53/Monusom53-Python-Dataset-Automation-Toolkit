import os
import shutil

# Source directory where the brand folders currently are
source_dir = r"\Review"

# Destination directory where you want to move the folders
destination_dir = r"\Checking"

# List of brand folders to move
brands = [
  "Proscotto",
  "Castelmondo",
  "Spark",
  "Wilhelm Winery",
  "California Icons",
  "Dos Cabezas",
  "Lakeside",
  "Gioioso",
  "S.A. Prum Blue",
  "Rudi Wiest",
  "Bruno",
  "Bollig Lehnert",
  "Schloss Saarstein",
  "Weingut Brundlmayer",
  "Iron Heart Winery",
  "Salvalai",
  "San Nicola",
  "Villa Montecristo",
  "Hectare",
  "Casa Del Toro",
  "Costaross",
  "Enrico",
  "D And L Carinalli Vineyards",
  "Emotion",
  "Mapreco",
  "Diamarine",
  "Famega",
  "Chateau De Montgueret",
  "Spring Gate Vineyards",
  "Sancerre",
  "Dr Konstantin Frank",
  "Twisted River",
  "Marmalade",
  "Wines Of The San Juan",
  "Fox Run",
  "Olde Schoolhouse",
  "Grand River Cellars",
  "Oak Knoll",
  "Melrose",
  "Hinman",
  "The Winery At Wilcox",
  "Robert Eymel Monchhof",
  "Indian Creek",
  "Meiers",
  "Cavazza",
  "Casarsa Vineyards"
]
# Ensure destination directory exists
os.makedirs(destination_dir, exist_ok=True)

for brand in brands:
    src_path = os.path.join(source_dir, brand)
    dest_path = os.path.join(destination_dir, brand)
    
    if os.path.exists(src_path) and os.path.isdir(src_path):
        try:
            # If the folder already exists at destination, skip or overwrite
            if os.path.exists(dest_path):
                print(f"Destination already has '{brand}', skipping...")
                continue

            # Copy the entire folder (recursively)
            shutil.move(src_path, dest_path)
            #shutil.copytree(src_path, dest_path)
            #print(f"Copied '{brand}' from '{source_dir}' to '{destination_dir}'")
            print(f"Moved '{brand}' from '{source_dir}' to '{destination_dir}'")
        except Exception as e:
            print(f"Error moving '{brand}': {e}")
    else:
        print(f"Folder '{brand}' not found in source directory")
