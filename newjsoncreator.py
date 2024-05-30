import os
import json
from sklearn.model_selection import train_test_split

# Define the paths and categories
base_path = '/raid/biplab/taha/PatternNet/images'
categories = sorted([d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))])
"""ucmseced all_categories = [
    "agricultural",
    "airplane",
    "baseballdiamond",
    "beach",
    "buildings",
    "chaparral",
    "denseresidential",
    "forest",
    "freeway",
    "golfcourse",
    "harbor",
    "intersection",
    "mediumresidential",
    "mobilepark",
    "overpass",
    "parkinglot",
    "river",
    "runway",
    "sparseresidential",
    "storagetanks",
    "tenniscourt"
]"""

all_categories=[
    "airplane", "baseball_field", "basketball_court", "beach", "bridge", "cemetery",
    "chaparral", "christmas_tree_farm", "closed_road", "coastal_mansion", "crosswalk",
    "dense_residential", "ferry_terminal", "football_field", "forest", "freeway",
    "golf_course", "harbor", "intersection", "mobile_home_park", "nursing_home",
    "oil_gas_field", "oil_well", "overpass", "parking_lot", "parking_space", "railway",
    "river", "runway", "runway_marking", "shipping_yard", "solar_panel", "sparse_residential",
    "storage_tank", "swimming_pool", "tennis_court", "transformer_station", "wastewater_treatment_plan"
]

# Percentage split for train, val, and test sets
train_percentage = 0.6
val_percentage = 0.2
test_percentage = 0.2

# Initialize the lists for train, val, and test data
train_data = []
val_data = []
test_data = []

# Indexing for categories
category_index = {category: idx for idx, category in enumerate(all_categories)}

# Function to add data to the dataset list
def add_to_dataset(category, file_list, label, dataset_list):
    for file in file_list:
        dataset_list.append([f"{category}/{file}", label, category])

# Process each category
for category in all_categories:
    category_path = os.path.join(base_path, category)
    if not os.path.isdir(category_path):
        continue

    # Get list of all files in the category
    files = [f for f in os.listdir(category_path) if os.path.isfile(os.path.join(category_path, f))]

    # Determine the label from the category index
    label = category_index[category]

    # Split files into train/val/test datasets
    train_files, remaining_files = train_test_split(files, train_size=train_percentage, random_state=42)
    val_files, test_files = train_test_split(remaining_files, train_size=val_percentage/(1-train_percentage), random_state=42)
    
    # Add data to train, val, and test datasets
    add_to_dataset(category, train_files, label, train_data)
    add_to_dataset(category, val_files, label, val_data)
    add_to_dataset(category, test_files, label, test_data)

# Combine train, val, and test data into a single dictionary
dataset = {
    "train": train_data,
    "val": val_data,
    "test": test_data
}

# Save the dataset to a JSON file
with open('patternnet.json', 'w') as json_file:
    json.dump(dataset, json_file, indent=4)

print("Dataset JSON file created successfully.")
