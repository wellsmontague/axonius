import json
import os
# This was written by Wells Montague 5/8/2024

# Prompt the user to enter the path to the input JSON file
input_file_path = input("Please enter the path to your JSON file: ")

# Generate the output file path by appending '_formatted' before the file extension
base, ext = os.path.splitext(input_file_path)
output_file_path = f"{base}_formatted{ext}"

# Load the JSON data from the file
with open(input_file_path, 'r') as file:
    data = json.load(file)

# Write the formatted JSON data to the output file
with open(output_file_path, 'w') as file:
    json.dump(data, file, indent=4)

print(f"JSON file has been formatted and saved to {output_file_path}")

