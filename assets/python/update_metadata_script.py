"""Creates the metadata for this projects resources"""

import json
from datetime import datetime
from getpass import getuser

METADATA_FILE = "D:/Repositories/PEs/Algorithms/VL/conf/metadata.json"

# Read the metadata JSON file
with open(file=METADATA_FILE, mode="r", encoding="utf-8") as file:
    metadata = json.load(file)

# Update the metadata with auto-generated values
metadata["Author"] = getuser()
metadata["Date"] = datetime.now().strftime("%Y-%m-%d")

# Write the updated metadata back to the JSON file
with open(file=METADATA_FILE, mode="w", encoding="utf-8") as file:
    json.dump(metadata, file, indent=4)

print("Metadata updated.")
