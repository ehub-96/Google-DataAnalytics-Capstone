import csv
import json

# Define the input and output file paths
csv_file_path = "JSON_DICT.csv"
json_file_path = "output.json"

# Initialize the nodes and links dictionaries
nodes = []
links = []

# Read the CSV file
with open(csv_file_path, newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        # Extract the source and target values from the current row
        source = row['SOURCE']
        target1 = row['TARGET 1']

        
        # Add the source and target nodes to the nodes dictionary if they don't exist
        if {'name': source} not in nodes:
            nodes.append({'name': source})
        if {'name': target1} not in nodes:
            nodes.append({'name': target1})

        
        # Add the links between the source and target nodes to the links dictionary
        links.append({'source': source, 'target': target1})


# Combine the nodes and links dictionaries into a single dictionary
json_data = {'nodes': nodes, 'links': links}

# Write the JSON data to a file
with open(json_file_path, 'w') as json_file:
    json.dump(json_data, json_file)
